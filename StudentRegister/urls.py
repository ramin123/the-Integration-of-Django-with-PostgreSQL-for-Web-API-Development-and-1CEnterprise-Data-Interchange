from django.urls import path
from StudentRegister import views

urlpatterns = [
    path('',views.Add_Info, name='Add_Info'),
    path('delete/<int:id>',views.Delete_Info, name='Delete_Info'),
    path('view/<int:id>',views.View_Info, name='View_Info'),
    path('edit/<int:id>',views.Edit_Info, name='Edit_Info'),
    # path('yes',views.handle_new_row, name='yes'),
    path('show',views.show, name='show'),
    path('showFiltered',views.showFiltered, name='showFiltered'),

]