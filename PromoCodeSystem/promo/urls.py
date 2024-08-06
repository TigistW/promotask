from django.urls import path
from .views import GeneratePromoCodeView, ApplyPromoCodeView

urlpatterns = [
    path('generate/', GeneratePromoCodeView.as_view(), name='generate-promo-code'),
    path('apply/<str:code>/', ApplyPromoCodeView.as_view(), name='apply-promo-code'),
]
