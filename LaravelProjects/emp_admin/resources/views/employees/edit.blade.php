<form method="POST" action="{{ route('employees.update', $employee) }}">
    @csrf
    @method('PUT')
    @include('employees.form', ['employee' => $employee])
    <button type="submit">تحديث</button>
</form>
