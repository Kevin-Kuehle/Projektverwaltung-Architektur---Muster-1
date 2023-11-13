from rest_framework.response import Response
from rest_framework.decorators import api_view  


@api_view(['GET'])
def getData(request):
    print("request")
    person = { 'name': 'John', 'age': 31 }
    print(person)
    return  Response(person, status=200)
