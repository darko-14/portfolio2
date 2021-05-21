from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Work
from .serializers import WorkSerializer

class WorkView(APIView):

    def get(self, request):
        work = Work.objects.all()
        serializer = WorkSerializer(work, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkDetailsAPIView(APIView):

    def get_object(self, id):
        try:
            return Work.objects.get(id=id)
        except Work.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        work = self.get_object(id)
        serializer = WorkSerializer(work)
        return Response(serializer.data)

    def put(self, request, id):
        work = self.get_object(id)
        serializer = WorkSerializer(work, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        work = self.get_object(id)
        work.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
