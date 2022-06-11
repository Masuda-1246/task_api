
from rest_framework import generics
from .serializers import PostSerializers
from .models import Post

class PostView(generics.ListCreateAPIView ):
  queryset = Post.objects.all()
  serializer_class = PostSerializers
  
class CreateView(generics.CreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializers

class PostDetailView(generics.RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializers
    
