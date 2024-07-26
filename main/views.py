from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tutorial,TutorialCategory,TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import NewUserFrom

def single_slug(request,single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        series_urls = {}

        series_category = matching_series[0].tutorial_category   
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            series_urls[m] = part_one.tutorial_slug

        return render(request,
                      "main/category.html",
                      {"part_ones":series_urls,
                       "series_category":series_category}
                      )
    
    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]

    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tutorials_from_series = Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by('tutorial_published')
        this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)

        return render(request = request,
                      template_name='main/tutorial.html',
                      context = {"tutorial":this_tutorial,
                                "sidebar": tutorials_from_series,
                                "this_tut_idx": this_tutorial_idx})
    
    
    messages.info(request,f"{single_slug} doesnot exist")
    return redirect("main:homepage")


# Create your views here.

# always pass 'request' as a parameter when caling an actual view function like homepage here
def homepage(request):
    # return HttpResponse("Wow you have done a <strong>great Job</strong>")

    #template_name -> tells where to look for which specific template
    #Django searches for all the templates present in the app and it could lead to overlapping names problem
    #so we create a main subfolder in template folder to avoid collision

    #tutorials -> variable that stores info we want to send to the template and is accessible via this variable name now
    # return render(request=request,
    #               template_name="main/home.html",
    #               context={"tutorials":Tutorial.objects.all})

    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories":TutorialCategory.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"New Account Created: {username}")
            login(request,user)
            messages.info(request,f"You are now logged in as {username}")
            return redirect("main:homepage")
        
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])


    form = NewUserFrom
    return render(request,
                  "main/register.html",
                  context={"form":form}
                )

def logout_request(request):
    logout(request)
    messages.info(request,"Logged out successfully!!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                messages.info(request,f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request,"Invalid username or password. Please check again!!")
        else:
            messages.error(request,"Invalid username or password. Please check again!!")
            
    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form":form})