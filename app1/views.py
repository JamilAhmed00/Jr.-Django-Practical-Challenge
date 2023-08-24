from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from . import models
from . models import AssetModel, AssetCheckOutModel


# Create your views here.

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash





def check_out_asset(request, asset_id):
    asset = AssetModel.objects.get(pk=asset_id)
    if request.method == 'POST':
        
        if asset.is_valid ():
            employee = request.user
            condition = request.POST.get('condition')
            asset.current_condition = condition
            asset.save()
            AssetCheckOutModel.objects.create(asset=asset, employee=employee, check_out=True, condition=condition)
            return redirect('show_asset')
        
        else:
            return render(request, 'check_out_form.html', {'asset': asset})
        
    return render(request, 'check_out_form.html', {'asset': asset})




def check_in_asset(request, asset_id):
    asset = AssetModel.objects.get(pk=asset_id)
    if request.method == 'POST':
        
        if asset.is_valid ():
            employee = request.user
            condition = request.POST.get('condition')
            asset.current_condition = condition
            asset.save()
            AssetCheckOutModel.objects.create(asset=asset, employee=employee, check_out=False, condition=condition)
            return redirect('show_asset')
        
        else:
            return render(request, 'check_in_form.html', {'asset': asset})
            
            
    return render(request, 'check_in_form.html', {'asset': asset})




