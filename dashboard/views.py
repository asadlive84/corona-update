from django.shortcuts import render
import bangla
import corona_info as corona
import requests
import json
from django.views.generic.base import TemplateView






class DashboardView(TemplateView):
    template_name = "index.html"


    coronaSummaryResult = requests.get('https://corona.lmao.ninja/all').json()
    countryWiseSummary = requests.get('https://corona.lmao.ninja/countries').json()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        
        context['cases'] = bangla.convert_english_digit_to_bangla_digit(int(self.coronaSummaryResult['cases']))
        context['deaths'] = bangla.convert_english_digit_to_bangla_digit(int(self.coronaSummaryResult['deaths']))
        context['recovered'] = bangla.convert_english_digit_to_bangla_digit(int(self.coronaSummaryResult['recovered']))
        context['countryWiseSummary'] = self.countryWiseSummary
        
        return context



# # Create your views here.
# def dashboard(request):
#     coronaSummaryResult = requests.get('https://corona.lmao.ninja/all').json()
#     countryWiseSummary = requests.get('https://corona.lmao.ninja/countries').json()
#     context = {
#         'cases': bangla.convert_english_digit_to_bangla_digit(int(coronaSummaryResult['cases'])),
#         'deaths': bangla.convert_english_digit_to_bangla_digit(int(coronaSummaryResult['deaths'])),
#         'recovered': bangla.convert_english_digit_to_bangla_digit(int(coronaSummaryResult['recovered'])),
#         'countryWiseSummary': countryWiseSummary
#     }
#     return render(request, 'index.html', context)
