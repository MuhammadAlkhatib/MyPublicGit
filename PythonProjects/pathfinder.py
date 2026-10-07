import tkinter as tk
from tkinter import messagebox
import tkintermapview
import math
import heapq

class AStarMapProject:
    def __init__(self, root):
        self.root = root
        self.root.title("pathfinding")
        self.root.geometry("1100x700")
        
        self.nodes = {}  # حفظ الاحداثيات
        self.edges = {}  # حفظ الطرق بين العقد
        
        # الحالات الخاصة بالمستخدم
        self.start_node = None
        self.goal_node = None
        self.restricted_nodes = set()  # المناطق المحظورة
        
        # حفظ النقاط
        self.node_markers = {}
        self.edge_lines = []          # لتخزين خطوط الطرق العادية
        self.current_path_line = None  # لتخزين خط المسار الأقصر الناتجة من الخوارزمية
        
        # تتبع العقدة الأولى عند التوصيل بين عقدتين
        self.first_edge_node = None
        self.current_mode = tk.StringVar(value="add_node")
        
        self.setup_gui()

    def setup_gui(self):
        """إعداد واجهة المستخدم الرسومية"""
        # لوحة التحكم الجانبية (Control Panel)
        self.control_panel = tk.LabelFrame(self.root, text=" لوحة التحكم والعمليات ", font=("Arial", 12, "bold"), padx=10, pady=10)
        self.control_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        # تعليمات الاختيار
        tk.Label(self.control_panel, text="اختر الإجراء المطلوب أولاً:", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=5)
        
        # الأوضاع الديناميكية الجديدة لبناء الشبكة
        tk.Radiobutton(self.control_panel, text="➕ إضافة عقدة جديدة (انقر على الخريطة)", variable=self.current_mode, value="add_node", font=("Arial", 10), fg="blue").pack(anchor=tk.W, pady=2)
        tk.Radiobutton(self.control_panel, text="🔗 إضافة طريق/وصلة (انقر على عقدتين متتاليتين)", variable=self.current_mode, value="add_edge", font=("Arial", 10), fg="purple").pack(anchor=tk.W, pady=2)
        
        # أوضاع التعيين والحظر السابقة
        tk.Label(self.control_panel, text="----------------------------------------", fg="gray").pack(pady=5)
        tk.Radiobutton(self.control_panel, text="🟢 تعيين كنطقة بداية", variable=self.current_mode, value="start", font=("Arial", 10)).pack(anchor=tk.W, pady=2)
        tk.Radiobutton(self.control_panel, text="🔴 تعيين كنطقة نهاية", variable=self.current_mode, value="goal", font=("Arial", 10)).pack(anchor=tk.W, pady=2)
        tk.Radiobutton(self.control_panel, text="⚫ تبديل حالة الحظر (محظورة/متاحة)", variable=self.current_mode, value="restrict", font=("Arial", 10)).pack(anchor=tk.W, pady=2)
        
        # أزرار العمليات
        self.btn_run = tk.Button(self.control_panel, text="حساب المسار الأقصر (*A)", command=self.find_and_draw_path, bg="#2ecc71", fg="white", font=("Arial", 11, "bold"), height=2, width=22)
        self.btn_run.pack(pady=15)
        
        self.btn_reset = tk.Button(self.control_panel, text="إعادة تعيين الخريطة بالكامل", command=self.reset_map, bg="#e74c3c", fg="white", font=("Arial", 10), width=22)
        self.btn_reset.pack(pady=5)
        
        # شاشة لعرض حالة النظام والنتائج
        self.status_box = tk.Text(self.control_panel, height=12, width=28, font=("Arial", 9), bg="#f8f9fa", state=tk.DISABLED)
        self.status_box.pack(pady=15)

        # ويدجيت الخريطة الحية
        self.map_frame = tk.Frame(self.root)
        self.map_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # تحديد مركز الخريطة الابتدائي 
        self.map_widget = tkintermapview.TkinterMapView(self.map_frame, corner_radius=10)
        self.map_widget.set_position(24.7136, 46.6753) 
        self.map_widget.set_zoom(13)
        self.map_widget.pack(fill=tk.BOTH, expand=True)
        
        # ربط حدث النقر المباشر 
        self.map_widget.add_left_click_map_command(self.on_map_click)

    def log_message(self, text):
        """تحديث صندوق النصوص الجانبي بالمعلومات الحالية"""
        self.status_box.config(state=tk.NORMAL)
        self.status_box.delete('1.0', tk.END)
        self.status_box.insert(tk.END, text)
        self.status_box.config(state=tk.DISABLED)

    def on_map_click(self, coords):
        """حدث النقر المباشر على الخريطة (لإضافة عقدة جديدة)"""
        if self.current_mode.get() == "add_node":
            # توليد اسم تلقائي للعقدة (A, B, C... ثم N26, N27 في حال تخطي الحروف)
            if len(self.nodes) < 26:
                node_id = chr(65 + len(self.nodes))
            else:
                node_id = f"N{len(self.nodes)}"
                
            # حفظ العقدة في هياكل البيانات
            self.nodes[node_id] = coords
            self.edges[node_id] = []
            
            # رسم العقدة كـ Marker قابل للنقر
            marker = self.map_widget.set_marker(
                coords[0], coords[1], 
                text=f"العقدة {node_id}", 
                command=lambda m, nid=node_id: self.on_node_click(nid)
            )
            self.node_markers[node_id] = marker
            self.log_message(f"تم إضافة [العقدة {node_id}] بنجاح.\nالإحداثيات:\n{coords[0]:.4f}, {coords[1]:.4f}")
        else:
            if self.current_mode.get() == "add_edge":
                self.log_message("تنبيه: لإضافة طريق، يرجى النقر مباشرة على 'العقد الدائرية' وليس على الفراغ في الخريطة.")

    def on_node_click(self, node_id):
        """التعامل مع حدث النقر على عقدة معينة بناءً على الوضع المختار"""
        mode = self.current_mode.get()
        
        # إذا تغير الوضع، نقوم بإلغاء أي تحديد معلق للربط
        if mode != "add_edge":
            self.first_edge_node = None

        if mode == "add_edge":
            if not self.first_edge_node:
                self.first_edge_node = node_id
            else:
                if self.first_edge_node == node_id:
                    self.first_edge_node = None
                    self.log_message("تم إلغاء تحديد العقدة الأولى.")
                    return
                
                # التحقق من عدم وجود الطريق مسبقاً لمنع التكرار
                if node_id not in self.edges[self.first_edge_node]:
                    self.edges[self.first_edge_node].append(node_id)
                    self.edges[node_id].append(self.first_edge_node) # طريق ذو اتجاهين
                    
                    # رسم الخط الرمادي الممثل للطريق على الخريطة
                    pos1 = self.nodes[self.first_edge_node]
                    pos2 = self.nodes[node_id]
                    line = self.map_widget.set_path([pos1, pos2], color="gray", width=3)
                    self.edge_lines.append(line)
                    
                    self.log_message(f"تم إنشاء طريق بنجاح بين:\nالعقدة {self.first_edge_node} ↔ العقدة {node_id}")
                else:
                    self.log_message(f"الطريق بين {self.first_edge_node} و {node_id} موجود بالفعل!")
                
                self.first_edge_node = None 
                
        elif mode == "start":
            if node_id in self.restricted_nodes:
                messagebox.showwarning("تنبيه", "لا يمكن تعيين عقدة محظورة كنطقة بداية!")
                return
            if self.start_node:
                self.update_marker_appearance(self.start_node)
            self.start_node = node_id
            self.node_markers[node_id].set_text(f"البداية ({node_id})")
            self.node_markers[node_id].change_color("green", "white")
            
        elif mode == "goal":
            if node_id in self.restricted_nodes:
                messagebox.showwarning("تنبيه", "لا يمكن تعيين عقدة محظورة كنطقة نهاية!")
                return
            if self.goal_node:
                self.update_marker_appearance(self.goal_node)
            self.goal_node = node_id
            self.node_markers[node_id].set_text(f"الهدف ({node_id})")
            self.node_markers[node_id].change_color("red", "white")
            
        elif mode == "restrict":
            if node_id == self.start_node or node_id == self.goal_node:
                messagebox.showwarning("تنبيه", "لا يمكن حظر عقدة البداية أو النهاية الحالية!")
                return
            if node_id in self.restricted_nodes:
                self.restricted_nodes.remove(node_id)
                self.update_marker_appearance(node_id)
            else:
                self.restricted_nodes.add(node_id)
                self.node_markers[node_id].set_text(f"محظورة ({node_id})")
                self.node_markers[node_id].change_color("black", "yellow")
        
        # تحديث صندوق نص الحالة
        if mode not in ["add_edge", "add_node"]:
            status_text = f"البداية المحددة: {self.start_node}\nالهدف المحدد: {self.goal_node}\n"
            status_text += f"العقد المحظورة: {list(self.restricted_nodes)}"
            self.log_message(status_text)

    def update_marker_appearance(self, node_id):
        """إعادة الماركر لشكله الطبيعي الافتراضي بناءً على حالته الحالية"""
        if node_id in self.restricted_nodes:
            self.node_markers[node_id].set_text(f"محظورة ({node_id})")
            self.node_markers[node_id].change_color("black", "yellow")
        elif node_id == self.start_node:
            self.node_markers[node_id].set_text(f"البداية ({node_id})")
            self.node_markers[node_id].change_color("green", "white")
        elif node_id == self.goal_node:
            self.node_markers[node_id].set_text(f"الهدف ({node_id})")
            self.node_markers[node_id].change_color("red", "white")
        else:
            self.node_markers[node_id].set_text(f"العقدة {node_id}")
            self.node_markers[node_id].change_color("blue", "white")

    def calculate_distance(self, coord1, coord2):
        """حساب المسافة الحقيقية بين نقطتين جغرافيتين باستخدام صيغة هافيرسين"""
        lat1, lon1 = coord1
        lat2, lon2 = coord2
        R = 6371.0  # نصف قطر الأرض بالكيلومترات
        
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        
        a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    def a_star_algorithm(self, start, goal):
        """تنفيذ خوارزمية *A الديناميكية وتجنب المناطق المحظورة"""
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        
        g_score = {node: float('inf') for node in self.nodes}
        g_score[start] = 0
        
        f_score = {node: float('inf') for node in self.nodes}
        f_score[start] = self.calculate_distance(self.nodes[start], self.nodes[goal])
        
        while open_set:
            current_f, current = heapq.heappop(open_set)
            
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path, g_score[goal]
            
            for neighbor in self.edges.get(current, []):
                if neighbor in self.restricted_nodes:
                    continue
                
                tentative_g = g_score[current] + self.calculate_distance(self.nodes[current], self.nodes[neighbor])
                
                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    h_score = self.calculate_distance(self.nodes[neighbor], self.nodes[goal])
                    f_score[neighbor] = tentative_g + h_score
                    
                    if not any(item[1] == neighbor for item in open_set):
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        
        return None, float('inf')

    def find_and_draw_path(self):
        """استدعاء الخوارزمية ورسم المسار الناتج بلون مميز"""
        if not self.start_node or not self.goal_node:
            messagebox.showerror("خطأ في المدخلات", "يرجى تحديد نقطتي البداية والنهاية أولاً بالضغط على العقد المتاحة.")
            return
            
        # مسح أي مسار قديم مرسوم
        if self.current_path_line:
            self.current_path_line.delete()
            self.current_path_line = None
            
        path, total_cost = self.a_star_algorithm(self.start_node, self.goal_node)
        
        if path:
            coordinates_path = [self.nodes[node] for node in path]
            self.current_path_line = self.map_widget.set_path(coordinates_path, color="blue", width=6)
            
            result_msg = f" تم العثور على المسار بنجاح!\n\n"
            result_msg += f"المسار: {' -> '.join(path)}\n\n"
            result_msg += f"إجمالي المسافة الفعلية:\n{total_cost:.3f} كم\n\n"
            result_msg += f"عدد العقد المقطوعة: {len(path)}"
            self.log_message(result_msg)
        else:
            self.log_message(" النتيجة:\nللأسف، لا يوجد مسار متاح!\n\nتحقق من وجود طرق واصلة بين البداية والهدف، أو أن القيود تقطع جميع الطرق.")
            messagebox.showwarning("تعذر العثور على مسار", "لا يمكن الوصول للهدف بناءً على شبكة الطرق الحالية.")

    def reset_map(self):
        """إعادة تعيين ومسح كل شيء وبناء النظام من جديد"""
        # مسح خط المسار الأقصر
        if self.current_path_line:
            self.current_path_line.delete()
            self.current_path_line = None
            
        # تصفير البيانات تماماً
        for line in self.edge_lines:
            line.delete()
        self.edge_lines.clear()
        for marker in self.node_markers.values():
            marker.delete()
        self.node_markers.clear()
        self.nodes.clear()
        self.edges.clear()
        self.start_node = None
        self.goal_node = None
        self.restricted_nodes.clear()
        self.first_edge_node = None

if __name__ == "__main__":
    root = tk.Tk()
    app = AStarMapProject(root)
    root.mainloop()