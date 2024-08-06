from django.urls import path
from .views import GeneratePromoCodeView, ApplyPromoCodeView,GeneratePromoCodeWithDiscountView

urlpatterns = [
    path('generate/', GeneratePromoCodeView.as_view(), name='generate-promo-code'),
    path('generate-discount/', GeneratePromoCodeWithDiscountView.as_view(), name='generate-promo-code-discount'),
    path('apply/<str:code>/', ApplyPromoCodeView.as_view(), name='apply-promo-code'),
]
# path('promo/generate/', PromoCodeCreateView.as_view(), name='generate_promo_code'),GeneratePromoCodeWithDiscountView