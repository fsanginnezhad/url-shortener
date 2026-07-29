from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Link
from .serializers import LinkSerializer

from rest_framework.permissions import IsAuthenticated

class LinklistCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        links = Link.objects.filter(owner=request.user)
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LinkSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LinkDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk, user):
        return get_object_or_404(Link, pk=pk, owner=user)

    def get(self, request, pk):
        link = self.get_object(pk, request.user)
        serializer = LinkSerializer(link)
        return Response(serializer.data)

    def put(self, request, pk):
        link = self.get_object(pk, request.user)
        serializer = LinkSerializer(link, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        link = self.get_object(pk, request.user)
        link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)