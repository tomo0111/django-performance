from django.http import HttpResponse
from rest_framework.views import APIView

class HelloView(APIView):

    def get(self, request):
        hello = {'key': 'hello world'}
        return HttpResponse(hello)