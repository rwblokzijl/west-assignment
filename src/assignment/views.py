from django.http.response   import HttpResponse, HttpResponseBadRequest

from sympy.ntheory import factorint

def smallest_number_divisible(start, stop):

    # Extract all common factors
    factors = dict()
    for i in range(start, stop+1):
        if i == 0:
            continue
        for prime, amount in factorint(i).items():
            prime = abs(prime)
            factors[prime] = max(amount, factors.get(prime, 0))

    # Multiply them together
    answer = 1
    for factor, amount in factors.items():
        answer *= (factor ** amount)

    return answer

def return_smallest(request, start, stop):
    if stop < start:
        return HttpResponseBadRequest("Please provide 2 numbers in increasing order")
    return HttpResponse(smallest_number_divisible(start, stop))

