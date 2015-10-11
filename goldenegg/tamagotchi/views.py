from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render

from .models import User, Pet


# def index(request):
#     richest_pet_list = Pet.objects.order_by('virtual_gold')[:5]
#     highest_level_pet_list = Pet.objects.order_by('level','experience')[:5]
#     context = {
#         'richest_pet_list': richest_pet_list,
#         'highest_level_pet_list': highest_level_pet_list,
#     }
#     return render(request, 'tamagotchi/index.html', context)

def index(request):
    user = Pet.objects.order_by('virtual_gold')[0]
    context = {
        'user': user,
    }
    return render(request, 'tamagotchi/index.html', context)


def choose(request):
    context = {}
    return render(request, 'tamagotchi/choose-character.html', context)

def homepage(request):
    user = Pet.objects.order_by('virtual_gold')[0].user
    context = {
        'user': user,
    }
    return render(request, 'tamagotchi/homepage.html', context)

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'tamagotchi/user.html', {'user': user})

def pet(request, user_id):
    owner = get_object_or_404(User, pk=user_id)
    return render(request, 'tamagotchi/pet.html', {'owner': owner})
