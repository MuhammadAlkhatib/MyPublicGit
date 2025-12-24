<?php

use App\Http\Controllers\CategoriesController;
use Illuminate\Contracts\View\View;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('home');
});


Route::get('/about',function(): View{

    return view('about');

});

Route::get('/services',function(): View{

    return view('services');

});
Route::get('/dashboard',function(): View{

    return view('dashboard');

});


            //  url                          class name                               method/action
// route::get('/categories', [App\Http\Controllers\CategoriesController::class,'index']);

route::get('/categories',[CategoriesController::class,'index']);

// route::post() add data
// route::put() update data id ==1
// route::delete() delete data
// route::patch() update data auth id ==1

route::get('/categories/create',[CategoriesController::class,'create']);