from rest_framework import generics

from newsletter.models import Join
from .serializers import JoinSerializer

class JoinCreateAPIView(generics.CreateAPIView):
	queryset            	= Join.objects.all()
	serializer_class    	= JoinSerializer
	permisssion_classes 	= []
	authentication_classes 	= []  
