"""
URL configuration for gymapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from home import views as home_views
from exercises import views as exercises_views
from registerworkouts import views as rw_views
from workoutsessions import views as ws_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('signup/', home_views.signup, name='signup'),
    path('signin/', home_views.signin, name='signin'),
    path('logout/', home_views.signout, name='logout'),
    path('exercises/', exercises_views.exercises_list, name='exercises_list'),
    path('register_workouts/', rw_views.register_workouts, name='register_workouts'),
    path('register_workouts/<int:registerworkout_id>/', rw_views.register_workout_detail, name='register_workout_detail'),
    path('register_workouts/<int:registerworkout_id>/delete/', rw_views.register_workout_delete, name='register_workout_delete'),
    path('workout_sessions/', ws_views.workout_sessions, name='workout_sessions'),
    path('workout_sessions/<int:workout_session_id>/', ws_views.workout_session_detail, name='workout_session_detail'),
    path('workout_sessions/<int:workout_session_id>/delete/', ws_views.delete_workout_session, name='delete_workout_session'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
