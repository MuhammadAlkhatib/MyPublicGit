<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    // ريجيستر لتنزيل المكتبة
    // يخضع لامر معين ثم يقف
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap any application services.
     */
    // بوت لتشغيل المكتبة
    // يستمر باستلام ريكويستات حتى ينتهي
    public function boot(): void
    {
        // دوال
    }
}
