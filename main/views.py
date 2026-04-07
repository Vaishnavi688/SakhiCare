# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import RegisterForm
from .models import Category

# -----------------------------
# AUTHENTICATION & BASIC VIEWS
# -----------------------------
def home_view(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

# main/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ Creates and saves the user in the database
            messages.success(request, "Your account has been created successfully! Please log in.")
            return redirect("login")  # Redirect to login after successful registration
        else:
            print(form.errors)  # Debugging output
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

@login_required
def dashboard_view(request):
    categories = Category.objects.prefetch_related("items").order_by("order")
    return render(request, "dashboard.html", {"categories": categories})

# -----------------------------
# STATIC INFO PAGES
# -----------------------------
def privacy_policy(request):
    return render(request, "privacy_policy.html")

def terms_of_use(request):
    return render(request, "terms_of_use.html")

def contact_us(request):
    return render(request, "contact_us.html")

def email_page(request):
    return render(request, "email_page.html")

# -----------------------------
# MENSTRUAL CYCLE SECTION
# -----------------------------
@login_required
def menstrual_home(request):
    return render(request, 'menstrual_home.html')

@login_required
def menstrual_period_tracker(request):
    return render(request, 'menstrual_period_tracker.html')

@login_required
def menstrual_yoga(request):
    return render(request, 'menstrual_yoga.html')

@login_required
def menstrual_nutrition(request):
    return render(request, 'menstrual_nutrition.html')

@login_required
def menstrual_carefree(request):
    return render(request, 'menstrual_carefree.html')

@login_required
def menstrual_donation(request):
    return render(request, 'menstrual_donation.html')

# -----------------------------
# PRE-PREGNANCY SECTION
# -----------------------------
@login_required
def prepregnancy_home(request):
    return render(request, 'prepregnancy_home.html')

@login_required
def p_book_appointment(request):
    return render(request, 'p_book_appointment.html')

@login_required
def prepregnancy_nutrition(request):
    return render(request, 'prepregnancy_nutrition.html')

@login_required
def prepregnancy_dos_donts(request):
    return render(request, 'prepregnancy_dos_donts.html')

@login_required
def prepregnancy_yoga(request):
    return render(request, 'prepregnancy_yoga.html')

@login_required
def prepregnancy_emotional_support(request):
    return render(request, 'prepregnancy_emotional_support.html')


from django.shortcuts import render

@login_required
def postpregnancy_home(request):
    return render(request, 'postpregnancy_home.html')

# Book Appointment
@login_required
def post_book_appointment(request):
    return render(request, 'post_book_appointment.html')


@login_required
def post_breastfeeding_guidance(request):
    return render(request, 'post_breastfeeding_guidance.html')

@login_required
def baby_vaccines(request):
    return render(request, 'baby_vaccines.html')

@login_required
def baby_care(request):
    return render(request, 'baby_care.html')



@login_required
def how_to_use_pads(request):
    return render(request, 'how_to_use_pads.html')

@login_required
def best_products(request):
    return render(request, 'best_products.html')

@login_required
def personal_hygiene(request):
    return render(request, 'personal_hygiene.html')

@login_required
def comfort_selfcare(request):
    return render(request, 'comfort_selfcare.html')

@login_required
def myths_facts(request):
    return render(request, 'myths_facts.html')

@login_required
def baby_shampoo_soap(request):
    return render(request, 'baby_shampoo_soap.html')

@login_required
def baby_lotion_oil(request):
    return render(request, 'baby_lotion_oil.html')

@login_required
def diapers_wipes(request):
    return render(request, 'diapers_wipes.html')

@login_required
def clothing_blankets(request):
    return render(request, 'clothing_blankets.html')

@login_required
def colic_gas(request):
    return render(request, 'colic_gas.html')

@login_required
def diaper_rashes(request):
    return render(request, 'diaper_rashes.html')

@login_required
def fever_vaccination(request):
    return render(request, 'fever_vaccination.html')

@login_required
def cradlecap_dry_skin(request):
    return render(request, 'cradlecap_dry_skin.html')

