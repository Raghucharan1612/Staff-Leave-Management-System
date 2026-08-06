from . import views
from django.urls import path
urlpatterns = [
    path('apply/',views.apply_leave,name='apply_leave'),
    path('my-leaves/',views.my_leave,name='my_leaves'),
    path('view/',views.view_leaves,name='view_leaves'),
    path('leave/approve_leave/<int:id>/',views.approve_leave,name='approve_leave'),
    path('leave/reject_leave/<int:id>/',views.reject_leave,name='reject_leave'),
]