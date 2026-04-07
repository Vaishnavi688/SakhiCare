# main/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Basic pages
    path("", views.home_view, name="home"),
    path("about/", views.about, name="about"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("signup/", TemplateView.as_view(template_name="signup.html"), name="signup"),

    # Informational pages
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("terms-of-use/", views.terms_of_use, name="terms_of_use"),
    path("contact-us/", views.contact_us, name="contact_us"),
    path("email/", views.email_page, name="email_page"),

    # Menstrual Cycle main page
    path("menstrual/", views.menstrual_home, name="menstrual_home"),

    # Menstrual Cycle Subpages
    path("menstrual/period-tracker/", views.menstrual_period_tracker, name="menstrual_period_tracker"),
    path("menstrual/yoga/", views.menstrual_yoga, name="menstrual_yoga"),
    path("menstrual/nutrition/", views.menstrual_nutrition, name="menstrual_nutrition"),
    path("menstrual/carefree/", views.menstrual_carefree, name="menstrual_carefree"),
    path("menstrual/donation/", views.menstrual_donation, name="menstrual_donation"),

    path("menstrual/carefree/how-to-use-pads/", views.how_to_use_pads, name="how_to_use_pads"),
    path("menstrual/carefree/best-products/", views.best_products, name="best_products"),
    path("menstrual/carefree/personal-hygiene/", views.personal_hygiene, name="personal_hygiene"),
    path("menstrual/carefree/comfort-and-selfcare/", views.comfort_selfcare, name="comfort_selfcare"),
    path("menstrual/carefree/myths-and-facts/", views.myths_facts, name="myths_facts"),

    # Pregnancy main page
    path('prepregnancy_home/', views.prepregnancy_home, name='prepregnancy_home'),
    path('p_book_appointment/', views.p_book_appointment, name='p_book_appointment'),
    path('prepregnancy_nutrition/', views.prepregnancy_nutrition, name='prepregnancy_nutrition'),
    path('prepregnancy_dos_donts/', views.prepregnancy_dos_donts, name='prepregnancy_dos_donts'),
    path('prepregnancy_yoga/', views.prepregnancy_yoga, name='prepregnancy_yoga'),
    path('prepregnancy_emotional_support/', views.prepregnancy_emotional_support, name='prepregnancy_emotional_support'),

    # Post-Pregnancy Section
    path('postpregnancy_home/', views.postpregnancy_home, name='postpregnancy_home'),
    path('post_book_appointment/', views.post_book_appointment, name='post_book_appointment'),
    path('post_breastfeeding_guidance/', views.post_breastfeeding_guidance, name='post_breastfeeding_guidance'),
    path('baby_vaccines/', views.baby_vaccines, name='baby_vaccines'),
    path('baby_care/', views.baby_care, name='baby_care'),
    path('baby-care/shampoo-soap/', views.baby_shampoo_soap, name='baby_shampoo_soap'),
    path('baby-care/lotion-oil/', views.baby_lotion_oil, name='baby_lotion_oil'),
    path('baby-care/diapers-wipes/', views.diapers_wipes, name='diapers_wipes'),
    path('baby-care/clothing-blankets/', views.clothing_blankets, name='clothing_blankets'),
    path('baby-care/colic-gas/', views.colic_gas, name='colic_gas'),
    path('baby-care/diaper-rashes/', views.diaper_rashes, name='diaper_rashes'),
    path('baby-care/fever-vaccination/', views.fever_vaccination, name='fever_vaccination'),
    path('baby-care/cradlecap-dry-skin/', views.cradlecap_dry_skin, name='cradlecap_dry_skin'),
]



