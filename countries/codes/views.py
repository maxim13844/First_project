from django.http import HttpResponse

from codes.models import Country


def get_country_name(request):
    if 'code' not in request.GET:
        return HttpResponse('code param is required')
    code_input = request.GET['code'].upper()
    return HttpResponse(Country.objects.filter(code=code_input).first() or 'Country not found')




