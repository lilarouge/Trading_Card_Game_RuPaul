from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('addADiscussion/',views.addADiscussion,name='addADiscussion'),
    path('addAComment/<int:pk>',views.addAComment,name='addAComment'),
    path('single_discussion/<int:discussion_id>', views.single_discussion, name='single_discussion'),

]