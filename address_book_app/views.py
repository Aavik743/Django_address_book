from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import BadRequest

from .models import Person
from .serializers import PersonSerializer


class AddressBookAPI(APIView):
    def post(self, request):
        person_data = request.data
        try:
            serialized_data = PersonSerializer(data=person_data)
            if not serialized_data.is_valid():  # custom is_valid check
                raise Exception
            serialized_data.save()
            return Response({'Message': 'Contact Added', 'Status Code': 200})
        except BadRequest:
            return Response({'Error': "Something went wrong", 'Status Code': 400})

    def get(self, request, id_num=None):
        try:
            if id_num:
                person_data = Person.objects.get(pk=id_num)
                serialized_data = PersonSerializer(person_data)
                return Response({'Contacts': serialized_data.data, 'Status Code': 200})
            if not id_num:
                data = Person.objects.all()
                serialized_data = PersonSerializer(data, many=True)
                return Response({'Contacts': serialized_data.data, 'Status Code': 200})
        except BadRequest:
            return Response({'Error': "Something went wrong", 'Status Code': 400})

    def delete(self, request, id_num):
        try:
            person_data = Person.objects.get(pk=id_num)
            person_data.delete()
            return Response({'Message': 'Contact Deleted', 'Status Code': 200})
        except BadRequest:
            return Response({'Error': "Something went wrong", 'Status Code': 400})

    def put(self, request, id_num):
        try:
            person_data = Person.objects.get(pk=id_num)
            serialized_data = PersonSerializer(person_data, data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response({'Message': 'Contact Updated', 'Status Code': 200})
        except BadRequest as e:
            return Response({'Error': str(e), 'Status Code': 400})

