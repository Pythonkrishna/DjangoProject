from django.shortcuts import render
def showIndex(request):
    return render(request,"index.html")
def showdetails(request):
    username=request.POST.get("uname")
    password=request.POST.get("upass")
    d={"uname":username,"upass":password}
    return render(request,"show.html",d)
