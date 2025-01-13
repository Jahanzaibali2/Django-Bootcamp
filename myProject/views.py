from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render

# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    from django.http import HttpResponse
    

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # You can save the form data here if needed

        return JsonResponse({'success': True, 'message': f'Thank you, {name}. We have received your message.'})

    return render(request, 'website/contact.html')

