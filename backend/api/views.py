from rest_framework.response import Response
from rest_framework.decorators import api_view  


@api_view(['GET'])
def getData(request):
    person = { 'name': 'John', 'age': 31 }
    response = Response(person);
    response["Access-Control-Allow-Origin"] = "*"
    return  response
