from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Contact
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
        contacts = Contact.objects.all().filter(status=1)
        context = {
                'contacts' : contacts,
        }
        return render(request, 'index.html', context=context)

def addnew(request):
        if request.POST:
                data = request.POST
                name = data['name']
                email = data['email']
                address = data['address']
                phone = data['phone']
                contact = Contact(name=name,email=email,address=address,phone=phone)
                contact.save()
                return HttpResponseRedirect(reverse('home'))
        
        return render(request, 'addnew.html')

def editexisting(request):
        contacts = Contact.objects.all().filter(status=1)
        context = {
                'contacts' : contacts,
        }
        return render(request, 'edit.html', context=context)

def delete(request):
        contacts = Contact.objects.all().filter(status=1)
        context = {
                'contacts' : contacts,
        }
        return render(request, 'delete.html', context=context)

@csrf_exempt
def deletecontact(request):
        id = request.POST.get('id')
        contact = get_object_or_404(Contact, id=id)
        print(contact)
        contact.status = False
        contact.save()
        return HttpResponseRedirect(reverse('delete'))

def editContact(request, id):
        if request.POST:
                mname = request.POST['name']
                memail = request.POST['email']
                maddress = request.POST['address']
                mphone = request.POST['phone']
                contact = get_object_or_404(Contact, id=id)
                contact.name = mname
                contact.email = memail
                contact.address = maddress
                contact.phone = mphone
                contact.save()
                return HttpResponseRedirect(reverse('edit'))

        contact = get_object_or_404(Contact, id=id)
        context = {
                'contact' : contact
        }
        return render(request, 'editcontact.html', context=context)

def contact(request, id):
        contact = get_object_or_404(Contact, id=id)
        context = {
                'contact' : contact
        }
        return render(request, 'contact.html', context=context)