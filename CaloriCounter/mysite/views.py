from django.shortcuts import render, redirect
from .models import Food, Consume

# Create your views here.

def index(request):

    if request.method =="POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        food = Food.objects.all()

        return redirect('home')


    else:
        food = Food.objects.all()

    consumed_food = Consume.objects.all()
    return render(request, 'mysite/index.html', {
        'foods':food,
        'consumed_food':consumed_food,
    })

def delete_item(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'mysite/delete.html')
