from django.http import HttpResponse

from .models import User, Pet


def index(request):
    richest_pet_list = Pet.objects.order_by('virtual_gold')[:5]
    highest_level_pet_list = Pet.objects.order_by('level','experience')[:5]
    output = ', '.join([pet.user.user_name for pet in highest_level_pet_list])
    return HttpResponse(output)




def user(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)

def pet(request, user_id):
    response = "You're looking at the pet of user  %s."
    return HttpResponse(response % user_id)
