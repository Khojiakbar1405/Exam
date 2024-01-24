from django.urls import path
from . import views

urlpatterns = [
    # Bosh sahifa
    path('', views.index, name='index'),
    path('sample-inner-page/', views.sample_inner_page, name='sample-inner-page'),
    # Blog sahifa
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blog-details'),
    # Xizmatlar sahifa
    path('service/', views.service, name='service'),
    path('service-details/', views.service_details, name='service-details'),
    # Loyixalar sahifa
    path('projects/', views.projects, name='projects'),
    path('project-details/', views.project_details, name='project-details'),
    # Bo`g`lanish sahifa
    path('contact/', views.contact, name='contact'),
]