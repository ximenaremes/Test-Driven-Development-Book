from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.

# home_page = None
def home_page(request):
    # return render(request, 'home.html')

    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')

    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()

    # if request.method == 'POST':
    #     new_item_text = request.POST['item_text']  
    #     Item.objects.create(text=new_item_text)  
    # else:
    #     new_item_text = ''  
    # return render(request, 'home.html', {
    #     # 'new_item_text': request.POST['item_text'],
    #     # 'new_item_text': request.POST.get('item_text', ''),
    #     # 'new_item_text': item.text
    #     'new_item_text': new_item_text, 
    # })

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    # return render(request, 'home.html')
    return render(request, 'home.html', {'items': items})