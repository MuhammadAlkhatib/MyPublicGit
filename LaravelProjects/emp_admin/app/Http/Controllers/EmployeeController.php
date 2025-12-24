<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Employee;

class EmployeeController extends Controller
{
    public function index() {
        $employees = Employee::all();
        return view('employees.index', compact('employees'));
    }

    public function create() {
        return view('employees.create');
    }

    public function store(Request $request) {
        $validated = $request->validate([
            'first_name' => 'required|string|max:50',
            'last_name' => 'required|string|max:50',
            'rank' => 'required|string',
            'email' => 'required|email|unique:employees',
            'phone' => 'required|numeric',
            'city' => 'required|string|max:50',
            'salary' => 'required|numeric',
            'department' => 'required|string|max:50',
            'description' => 'required|string|max:500',
        ]);

        Employee::create($validated);

        return redirect()->route('employees.index')->with('success', 'تم إضافة الموظف بنجاح');
    }

    public function edit(Employee $employee) {
        return view('employees.edit', compact('employee'));
    }

    public function update(Request $request, Employee $employee) {
        $validated = $request->validate([
            'first_name' => 'required|string|max:50',
            'last_name' => 'required|string|max:50',
            'rank' => 'required|string',
            'email' => 'required|email|unique:employees,email,' . $employee->id,
            'phone' => 'required|numeric',
            'city' => 'required|string|max:50',
            'salary' => 'required|numeric',
            'department' => 'required|string|max:50',
            'description' => 'required|string|max:500',
        ]);

        $employee->update($validated);

        return redirect()->route('employees.index')->with('success', 'تم التعديل');
    }

    public function destroy(Employee $employee) {
        $employee->delete();
        return redirect()->route('employees.index')->with('success', 'تم الحذف');
    }
}
