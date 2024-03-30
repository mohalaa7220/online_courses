from .models import Contact_inf

def contact_info(request):
    contact = Contact_inf.objects.all()  
    return {'contact_info': contact}