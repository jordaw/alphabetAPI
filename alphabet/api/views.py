from cgi import test
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    test = {'foo':'bar', 'bar':'foo'}
    return Response(test)