from django.shortcuts import render

# Create your views here.
def kitob(request):
    return render(request, 'kitob/kitob.html')
from django.shortcuts import render, redirect
import requests

BOT_TOKEN = "8610336722:AAE3fKp8R_NMVHpmz6rKxKgdzvPHGHer25k"
CHAT_ID = "8907142720"

def kitob(request):
    return render(request, 'kitob/kitob.html')

def sotib_olish(request, kitob_nomi):
    if request.method == "POST":
        matn = f" Yangi buyurtma!\nKitob: {kitob_nomi}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": matn})
    return redirect('kitob')