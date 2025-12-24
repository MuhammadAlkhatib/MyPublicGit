<?php

namespace App\Http\Controllers;

use App\Models\Category;
use Illuminate\Http\Request;

class CategoriesController extends Controller
{
    public function index(): string 
    {
        // $name = "laravel";
        // return $name;

        // return __METHOD__;

        $name = "mohammad";
        $title = "all categories";
        $age = 22;

        // return view('categories.index',compact('name', "title"));
        // return view('categories.index')->with(key:[
        //     'title' => $title,
        //      'name' => $name
        //     ]);
        // return view ('categories.index', compact('title', 'name'));
        return view ('categories.index')->with([
            'categories' => Category::all(),
            'title' => $title,
            'name' => $name,
            'age' => $age
        ]);
    }
    public function create(): string 
    {
        return view('categories.create');
    }
}
