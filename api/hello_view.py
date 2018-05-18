from django.http import HttpResponse
from rest_framework.views import APIView

class HelloView(APIView):

    def get(self, request):
        return HttpResponse('hello, World')