from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models


# Bosh sahifaning funksiyasi. Bu ichida Construction va Project degan modellarni ichiga oladi 
# va sahifaga malumot qo`yib boradi.`
def index(request):

    data = models.Construction.objects.all()
    images = models.Project.objects.all()
    return render(request, 'index.html', {'data':data, 'images':images})

def sample_inner_page(request):
    return render(request, 'sample-inner-page.html')

# Bu blog sahifaning funksiyasi. Bu ichida Blog degan modelni olib kelgan malumotlarni sahifaga qo`yib ketadi.` 
def blog(request):
    blogs = models.Blog.objects.all()
    return render(request, 'blog.html', {'blogs':blogs})

def blog_details(request):
    return render(request, 'blog-details.html')

# Bu Contact sahifaning funksiyasi. 
def contact(request):
    if request.method == "POST":
        models.Contact.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            message = request.POST['message']
        )
        return redirect('contact')
    return render(request, 'contact.html')


# Bu Project sahifaning funksiyasi. Bu o`z ichiga ListProject degan modelni oladi va malumotlarnii sahifaga qo`yib ketadi 
def projects(request):
    pngs = models.ListProject.objects.all()
    return render(request, 'projects.html', {'pngs':pngs})

def project_details(request):
    return render(request, 'project-details.html')

# Bu Service sahifaning funksiyasi.
def service(request):
    return render(request, 'services.html')

def service_details(request):
    return render(request, 'service-details.html')


# templeti ichidagi - blog-details
#                   - project-details
#                   - sample-inner-page
#                   - service-details 
# lar qo`shimcha sahifalar shuning uchun ichi o`zgartirilmagan
