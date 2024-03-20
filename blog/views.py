from .models import *
from .serializers import *

from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        
