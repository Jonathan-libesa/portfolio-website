from django.shortcuts import render
from.models import*
from django.contrib import messages
from django.core.mail import EmailMessage,send_mail
import threading


# Create your views here.

# To MAKE EASIER FOR EMAILING A USER
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()
        #self.email.send(fail_silently=False)

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
      

	

def contact(request):
    pages = Page.objects.all()
    about = About.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        email_subject = f'New Message from {data["name"]}'
        email_message = f'''
        Name: {data["name"]}
        Email: {data["email"]}
        Subject: {data["subject"]}

        Message:
        {data["message"]}
        '''

        send_mail(email_subject, email_message, email, ['jonathanlibesa@gmail.com'])
        messages.add_message(request, messages.SUCCESS, 'We have received your message. Our team will respond to you soon.')
        return render(request, 'main/contact.html')
    else:
        context = {'pages': pages, 'about': about}  
        return render(request, 'main/contact.html', context)




def homeview(request):
    pages = Page.objects.all()
    about = About.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        country = request.POST['country']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        data = {
            'name': name,
            'country': country,
            'email': email,
            'phone': phone,
            'message': message
        }

        email_subject = f'New Message from {data["name"]}'
        email_message = f'''
        Name: {data["name"]}
        Email: {data["email"]}
        Phone: {data["phone"]}
        Quotation: {data["country"]}

        Message:
        {data["message"]}
        '''

        send_mail(email_subject, email_message, email, ['jonathanlibesa@gmail.com'])
        messages.add_message(request, messages.SUCCESS, 'We have received your email. Our team will respond to you soon.')
        return render(request, 'main/home.html')
    else:
        context = {'pages': pages, 'about': about}  
        return render(request, 'main/home.html', context)