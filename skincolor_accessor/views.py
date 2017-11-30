from django.http import Http404
from .models import skintone
from django.shortcuts import render, get_object_or_404

# in index.html, variables are to be written within two pairs of curly braces
def index(request):
    all_skintones = skintone.objects.all()
    context = {'all_skintones': all_skintones}
    return render(request, 'skincolor_accessor/index.html', context) #Has an inbuilt http response

def detail(request, skintone_id):
    # below is a condensed statement for try and except block
    skntne = get_object_or_404(skintone, pk=skintone_id)
    return render(request, 'skincolor_accessor/detail.html', {'skntne': skntne})
