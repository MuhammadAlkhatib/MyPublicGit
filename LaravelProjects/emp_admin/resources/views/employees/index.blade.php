<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>إدارة الموظفين</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container">
    @if(session('success'))
        <div class="alert alert-success">{{ session('success') }}</div>
    @endif

    <a href="{{ route('employees.create') }}" class="btn btn-primary mb-3">إضافة موظف</a>

    <table class="table table-bordered table-striped">
        <thead class="table-dark">
            <tr>
                <th>الاسم</th>
                <th>الوظيفة</th>
                <th>البريد</th>
                <th>الهاتف</th>
                <th>المدينة</th>
                <th>الراتب</th>
                <th>القسم</th>
                <th>الوصف</th>
                <th>إجراءات</th>
            </tr>
        </thead>
        <tbody>
            @foreach($employees as $employee)
            <tr>
                <td>{{ $employee->first_name }} {{ $employee->last_name }}</td>
                <td>{{ $employee->rank }}</td>
                <td>{{ $employee->email }}</td>
                <td>{{ $employee->phone }}</td>
                <td>{{ $employee->city }}</td>
                <td>{{ $employee->salary }}</td>
                <td>{{ $employee->department }}</td>
                <td>{{ $employee->description }}</td>
        
                <td>
                    <a href="{{ route('employees.edit', $employee) }}" class="btn btn-sm btn-warning">تعديل</a>
                    <form action="{{ route('employees.destroy', $employee) }}" method="POST" class="d-inline">
                        @csrf @method('DELETE')
                        <button type="submit" class="btn btn-sm btn-danger">حذف</button>
                    </form>
                </td>
            </tr>
            @endforeach
        </tbody>
    </table>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
