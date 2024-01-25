from django.shortcuts import render, get_object_or_404, redirect
from .models import*
from .forms import* 
from django.core.mail import EmailMessage,send_mail
import threading
from django.contrib import messages

# Create your views here.



MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
# To MAKE EASIER FOR EMAILING A USER


def Door_product(request):
	about=Door.objects.all()
	context ={'about':about }
	return render(request,'product/product-door.html',context )


def Window_product(request):
	about=Window.objects.all()
	context ={'about':about }
	return render(request,'product/window.html',context )

def Gate_product(request):
	about=Gate.objects.all()
	context ={'about':about }
	return render(request,'product/Gate.html',context )




class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def send_quotation(request, door_id):
    door = get_object_or_404(Door, pk=door_id)
    
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            quotation = form.save(commit=False)
            quotation.door = door
            quotation.save()

            # Send email
            subject = 'Quotation Request'
            message = f"Customer Name: {quotation.customer_name}\nCustomer Email: {quotation.customer_email}\nCustomer Phone_number: {quotation.customer_Phone}\nMessage: {quotation.message}"

            # Attach the door picture to the email
            door_picture_path = quotation.door.image.path
            with open(door_picture_path, 'rb') as picture_file:
                door_picture_content = picture_file.read()

            email = EmailMessage(subject, message, 'jonathanlibesa@gmail.com', ['jonathanlibesa@gmail.com'])
            email.attach('door_picture.png', door_picture_content, 'image/png')

            # Create an EmailThread instance and start the thread
            email_thread = EmailThread(email)
            email_thread.start()

            messages.add_message(request, messages.SUCCESS, 'We have received your Quotation. Our team will contact you soon.')
            return redirect('product_door')  # Redirect to a thank you page
    else:
        form = QuotationForm()
    return render(request, 'product/quotation_form.html', {'form': form, 'door': door})



def send_quotation1(request, window_id):
    window = get_object_or_404(Window, pk=window_id)
    
    if request.method == 'POST':
        form = QuotationForm1(request.POST)
        if form.is_valid():
            quotation = form.save(commit=False)
            quotation.window = window
            quotation.save()

            # Send email
            subject = 'Quotation Request'
            message = f"Customer Name: {quotation.customer_name}\nCustomer Email: {quotation.customer_email}\nCustomer Phone_number: {quotation.customer_Phone}\nMessage: {quotation.message}"

            # Attach the door picture to the email
            window_picture_path = quotation.window.image.path
            with open(window_picture_path, 'rb') as picture_file:
                window_picture_content = picture_file.read()

            email = EmailMessage(subject, message, 'jonathanlibesa@gmail.com', ['jonathanlibesa@gmail.com'])
            email.attach('window_picture.png', window_picture_content, 'image/png')

            # Create an EmailThread instance and start the thread
            email_thread = EmailThread(email)
            email_thread.start()

            messages.add_message(request, messages.SUCCESS, 'We have received your Quotation. Our team will contact you soon.')
            return redirect('product_window')  # Redirect to a thank you page
    else:
        form = QuotationForm1()
    return render(request, 'product/quotation_form1.html', {'form': form, 'window': window})





def send_quotation2(request, gate_id):
    gate = get_object_or_404(Gate, pk=gate_id)
    
    if request.method == 'POST':
        form = QuotationForm2(request.POST)
        if form.is_valid():
            quotation = form.save(commit=False)
            quotation.gate = gate
            quotation.save()

            # Send email
            subject = 'Quotation Request'
            message = f"Customer Name: {quotation.customer_name}\nCustomer Email: {quotation.customer_email}\nCustomer Phone_number: {quotation.customer_Phone}\nMessage: {quotation.message}"

            # Attach the door picture to the email
            gate_picture_path = quotation.gate.image.path
            with open(gate_picture_path, 'rb') as picture_file:
                gate_picture_content = picture_file.read()

            email = EmailMessage(subject, message, 'jonathanlibesa@gmail.com', ['jonathanlibesa@gmail.com'])
            email.attach('gate_picture.png', gate_picture_content, 'image/png')

            # Create an EmailThread instance and start the thread
            email_thread = EmailThread(email)
            email_thread.start()

            messages.add_message(request, messages.SUCCESS, 'We have received your Quotation. Our team will contact you soon.')
            return redirect('product_gate')  # Redirect to a thank you page
    else:
        form = QuotationForm2()
    return render(request, 'product/quotation_form2.html', {'form': form, 'gate': gate})