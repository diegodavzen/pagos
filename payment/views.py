from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def previous_view(request):
    return render(request, 'payment/previous.html')
# Create your views here.
@csrf_exempt
def validate_credit_card(request):
    card_number = request.POST.get('card number')
    expirary_month = request.POST.get('expirary month')
    expirary_year = request.POST.get('expirary_year')
    cw = request.POST.get('cw')

#Se realiza el cheque de validar la tarjeta
    is_valid = validate_credit_card_details(card_number,expirary_month,expirary_year,cw)

    #retorna o regresa la validacion del resultado de la API o respuesta json
    response = {'valid': is_valid}
    return JsonResponse(response)


def validate_credit_card_details(card_number, expiry_month, expiry_year, cw):
# Implement the credit card validation algorithm here
# Perform checks based on the provided criteria and return True or False accordingly
# You can implement points 1 to 3, and optionally try implementing point 4 (Luhn's algorithm)

    if card_number.startswith("34") or card_number.startswith("37"):
        if len(cw) != 4:
            return False
    else:
        if len(cw) != 3:
            return False

# Check the length of the card number
    if not 16 <= len(card_number) <= 19:
        return False

# Apply Luhn's algorithm to validate the card number
    digits = [int(x) for x in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]

    checksum = sum(odd_digits)
    for digit in even_digits:
        checksum += sum(divmod(2 * digit, 10))

    return checksum % 10 == 0