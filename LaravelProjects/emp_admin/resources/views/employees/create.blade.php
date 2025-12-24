<form method="POST" action="{{ route('employees.store') }}">
    @csrf
    @include('employees.form')
    <button type="submit" style="color: red;">حفظ</button>
</form>
