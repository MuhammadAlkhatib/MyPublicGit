<div>
    @if($errors->any())
        <div>
            <ul>@foreach($errors->all() as $error)<li>{{ $error }}</li>@endforeach</ul>
        </div>
    @endif
    <input type="text" name="first_name" value="{{ old('first_name', $employee->first_name ?? '') }}" placeholder="الاسم الأول" required>
    <input type="text" name="last_name" value="{{ old('last_name', $employee->last_name ?? '') }}" placeholder="الاسم الأخير" required>
    <input type="text" name="rank" value="{{ old('rank', $employee->rank ?? '') }}" placeholder="المرتبة" required>
    <input type="email" name="email" value="{{ old('email', $employee->email ?? '') }}" placeholder="البريد الإلكتروني" required>
    <input type="text" name="phone" value="{{ old('phone', $employee->phone ?? '') }}" placeholder="الهاتف" required>
    <input type="text" name="city" value="{{ old('city', $employee->city ?? '') }}" placeholder="المدينة" required>
    <input type="number" name="salary" value="{{ old('salary', $employee->salary ?? '') }}" placeholder="الراتب" required>
    <input type="text" name="department" value="{{ old('department', $employee->department ?? '') }}" placeholder="القسم" required>
    <textarea name="description" placeholder="الوصف">{{ old('description', $employee->description ?? '') }}</textarea>
</div>
