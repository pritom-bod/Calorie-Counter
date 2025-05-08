from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib.auth.decorators import login_required


# Home page - food add
@login_required
def index(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        return redirect('home')
    else:
        food = Food.objects.all()
        consumed_food = Consume.objects.filter(user=request.user)
        return render(request, 'mysite/index.html', {
            'foods': food,
            'consumed_food': consumed_food,
        })

# Delete food
@login_required
def delete_item(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('home')
    return render(request, 'mysite/delete.html')

# Dashboard view
@login_required
def required_view(request):
    return render(request, 'mysite/index.html')
