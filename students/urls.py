from django.urls import path
from . import views


urlpatterns=[
    path('',views.indexView,name="index_url"),
    path('courses/',views.coursesView,name="courses_url"),
    path('GDcoursedetails/',views.GDcoursedetailsView,name="GDcoursedetails_url"),
    path('dashboard/',views.dashboardView,name="dashboard_url"),
    path('stat/',views.statView,name="stat_url"),
    path('softdev/',views.softdevView,name="softdev_url"),
    path('IT/',views.ITView,name="IT_url"),
    path('accounting/',views.accountingView,name="accounting_url"),
    path('cs/',views.csView,name="cs_url"),
    path('about/',views.aboutView,name="about_url"),
    path('contact/',views.contactView,name="contact_url"),
    path('trainers/',views.trainersView,name="trainers_url"),
    path('register/',views.registerView, name="register_url"),
    
]