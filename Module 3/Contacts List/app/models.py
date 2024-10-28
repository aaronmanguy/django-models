from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.TextField()
    is_favorite = models.BooleanField(default=False)


def create_contact(name, email, phone, is_favorite=False):
    contact = Contact.objects.create(name=name, email=email, phone=phone, is_favorite=is_favorite)
    return contact

def all_contacts():
    return Contact.objects.all()

def find_contact_by_name(name):
    contact = Contact.objects.filter(name=name)
    if not contact:
        return None
    else:
        return contact[0]

def favorite_contacts():
    contact = Contact.objects.filter(is_favorite=True)
    if not contact:
        return None
    else:
        return contact

def update_contact_email(name, new_email):
    try:
        contact = find_contact_by_name(name)
        if contact:
            contact.email = new_email
            contact.save()
            return contact
    except Exception as error:
        return str(error)
    

def delete_contact(name):
    contact = Contact.objects.get(name=name).delete()
    return contact