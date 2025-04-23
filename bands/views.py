from django.shortcuts import render,get_object_or_404
from bands.models import musician

def Musician(request,musician_id):
    Musician = get_object_or_404(musician, id=musician_id)
    data = {
        'Musician':Musician,
    }
    return render(request,'musician.xhtml',data)


