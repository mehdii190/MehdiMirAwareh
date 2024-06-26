from django.shortcuts import render
from django.http import HttpResponse
from .models import Info, Resume, Contact



def page(request):
    my_info = Info.objects.all().last()
    my_resume = Resume.objects.all()

    if my_info.status == True:
        my_info.status = 'در دسترس'
    else:
        my_info.status = 'غیر فعال'

    # contact_us page view
    full_name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    if request.method == 'POST':
        Contact.objects.create(name=full_name, email=email, message=message)

    return render(request, 'index.html', {'info': my_info, 'resume': my_resume})


def post(request):
    
    
    return HttpResponse("You're voting on question")