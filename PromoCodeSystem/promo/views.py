import json
import random
import string
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PromoCode
from .serializers import PromoCodeSerializer
import uuid

class GeneratePromoCodeView(APIView):
    def post(self, request):
        code = str(uuid.uuid4()).replace('-', '').upper()[:8]
        promo_code = PromoCode.objects.create(code=code, discount = 60.0)
        return Response(PromoCodeSerializer(promo_code).data, status=status.HTTP_201_CREATED)
    
class GeneratePromoCodeWithDiscountView(APIView):
    def post(self, request, *args, **kwargs):
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON.'}, status=400)

            discount = data.get('discount', None)

            # Validate the discount amount
            if not discount:
                return JsonResponse({'error': 'Discount amount is required.'}, status=400)
            try:
                discount = float(discount)
            except ValueError:
                return JsonResponse({'error': 'Invalid discount amount.'}, status=400)

            if not (0 <= discount <= 100):
                return JsonResponse({'error': 'Discount amount must be between 0 and 100.'}, status=400)

            # Generate a random promo code
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

            # Create and save the promo code with the specified discount
            promo_code = PromoCode.objects.create(code=code, discount=discount)
            promo_code.save()

            return Response(PromoCodeSerializer(promo_code).data, status=status.HTTP_201_CREATED)
class ApplyPromoCodeView(APIView):
     def post(self, request, code):
        try:
            # Retrieve the promo code object
            promo_code = PromoCode.objects.get(code=code)
            
            # Increment the usage count
            promo_code.usage_count += 1
            promo_code.save()
            
            # Return success response with discount and usage count
            return Response({
                'message': 'Promo code applied successfully!',
                'discount': promo_code.discount,
                'usage_count': promo_code.usage_count
            }, status=status.HTTP_200_OK)
        except PromoCode.DoesNotExist:
            # Handle case where promo code does not exist
            return Response({'message': 'Invalid promo code.'}, status=status.HTTP_400_BAD_REQUEST)