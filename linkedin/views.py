import json
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


class LinkedinApi(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LinkedinApi, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        print("GET Method", request)
        return JsonResponse({"data": "GET"}, safe=False)

    def post(self, request):
        print("POST Method", request)
        return JsonResponse({"data": "POST"}, safe=False)