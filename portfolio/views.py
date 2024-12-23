from django.shortcuts import redirect, render
from portfolio.models import Contact,Blogs
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

# def about(request):
#     return render(request,'about.html')

def about(request):
    context = {
        'about_text': "Enthusiastic and dedicated Python Developer with a solid foundation in Python, Django, HTML5, CSS3, and MySQL. Eager to kickstart a career in software development, leveraging a passion for coding to contribute effectively to innovative projects. Committed to ongoing growth, embracing new challenges, and staying abreast of industry advancements through continuous learning.",
        'profile_info': {
            'name': 'Manjula Jatavath',
            'birthday': '17 Aug',
            'city': 'Hyderabad, Telangana',
            'degree': 'BSC',
            'email': 'manjulajatavath554@gmail.com',
        }
    }
    return render(request, 'about.html', context)

def resume(request):
    return render(request,'resume.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('num')
        message = request.POST.get('message')

        messages.success(request, 'Your message has been successfully submitted.')
        return redirect('home')

    return render(request, 'contact.html')



def blog(request):

    posts=Blogs.objects.all()
    context={"posts":posts}
    
    return render(request, 'blog.html',context)