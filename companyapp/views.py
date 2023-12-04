from django.shortcuts import render,redirect
from . models import UserInfo
from . forms import UserForm

# Create your views here.

def user_info_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            cname=form.cleaned_data.get("company_name")
            uname=form.cleaned_data.get("username")
            pswrd=form.cleaned_data.get("password")

            if UserInfo.objects.filter(company_name=cname,username=uname,password=pswrd):
                return render(request,"success.html")
            
            else:
                return render(request,"error.html")

    else:
        form=UserForm()       
    return render(request,"user_info.html",{"form":form})        


