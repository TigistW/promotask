from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PromoCode
from .serializers import PromoCodeSerializer
import uuid

class GeneratePromoCodeView(APIView):
    def post(self, request):
        code = str(uuid.uuid4()).replace('-', '').upper()[:8]
        promo_code = PromoCode.objects.create(code=code, discount=60.0)
        return Response(PromoCodeSerializer(promo_code).data, status=status.HTTP_201_CREATED)

class ApplyPromoCodeView(APIView):
    def post(self, request, code):
        try:
            promo_code = PromoCode.objects.get(code=code)
            promo_code.usage_count += 1
            promo_code.save()
            return Response({
                'message': 'Promo code applied successfully!',
                'discount': promo_code.discount
            }, status=status.HTTP_200_OK)
        except PromoCode.DoesNotExist:
            return Response({'message': 'Invalid promo code.'}, status=status.HTTP_400_BAD_REQUEST)
