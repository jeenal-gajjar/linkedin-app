import json
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class LinkedinApi(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LinkedinApi, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body.decode("UTF-8"))
        print(data)
        return data