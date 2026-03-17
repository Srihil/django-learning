from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

  dest1 = Destination()
  dest1.name = 'Mumbai'
  dest1.desc = 'Nulla pretium tincidunt felis, nec.'
  dest1.img = 'Destination_1.jpg'
  dest1.price = 701
  dest1.offer = False

  dest2 = Destination()
  dest2.name = 'Hyderabad'
  dest2.desc = 'Nulla pretium tincidunt felis, nec.'
  dest2.img = 'Destination_2.jpg'
  dest2.price = 891
  dest2.offer = True

  dest3 = Destination()
  dest3.name = 'Chennai'
  dest3.desc = 'Nulla pretium tincidunt felis, nec.'
  dest3.img = 'Destination_3.jpg'
  dest3.price = 801
  dest3.offer = False

  dest = [dest1, dest2, dest3]
  return render(request, "index.html", {'dest': dest})