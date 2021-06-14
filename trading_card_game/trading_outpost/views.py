from django.shortcuts import render, redirect
import requests
from .models import Queens, My_Card
from .forms import *
import random
from django.views import generic
from django.contrib.auth.decorators import login_required

def get_queens(request):
    all_queens= {}

    url= 'http://www.nokeynoshade.party/api/queens/all'
    response = requests.get(url)
    data = response.json()
    print(data)
    queens= data

    for i in queens:
        queen_data = Queens(
            name = i['name'],
            winner = i['winner'],
            missCongeniality = i['missCongeniality'],
            quote = i['quote'],
            image_url = i['image_url']
        )
        queen_data.save()
        all_queens = Queens.objects.all().order_by('-id')

    return render (request, 'homepage.html', { "all_queens": all_queens} )
        

def my_queen_card(request):
    
    my_queen= My_Card.objects.all().order_by('-id')
    return render(request, 'profile.html', {'my_queen': my_queen})


def my_offers(request):
    if request.method =='GET':
        my_queens= My_Card.objects.all()
        return render(request, 'my_offers.html', {'my_queens': my_queens})

    if request.method=='POST':
        data=request.POST
        print(data)
        card_to_update= My_Card.objects.get(id= data['id'])
        card_to_update.status=data['status']
        card_to_update.save()
    
        return redirect('my_cards')

def my_exchange(request):
    if request.method =='GET':
        my_queens= My_Card.objects.filter(status='O')
        return render(request, 'transaction.html', {'my_queens': my_queens})

    if request.method == 'POST':
        data=request.POST
        print(data)
        my_card_update= My_Card.objects.get(id= data['queen_card_id'])
        my_card_update.profile=request.user.profile
        my_card_update.save()
    
        return redirect('my_offers')



@login_required
def accept_offer(request):
    if request.method == 'GET':
        queen_offered=My_Card.objects.filter(status='G')
        return render(request, 'profile.html', {'queen_offered': queen_offered})

    if request.method == 'POST':
        data= request.POST
        my_card_update= My_Card.objects.get(id= data['queen_card_id'])
        my_card_update.profile= request.user.profile
        my_card_update.save()

        return redirect('my_cards')


# def transaction_view(request):
#     all_cards=My_Card.objects.filter(status='O')
#     print(all_cards)
#     for card in all_cards:
#         print(card.queen.image_url)
#     return render(request, 'transaction.html', context={'all_cards':all_cards})