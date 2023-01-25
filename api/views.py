from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article
from rest_framework.response import Response
from . serializers import ArticleSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, status, mixins
from rest_framework.decorators import api_view, renderer_classes, APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
from django.contrib.auth.models import User

'''lots of commented code to demonstrate different ways CREATE Django REST API. Finally used ModelViewSet for simplicity'''

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

# class UserView(APIView):
#     serializer = UserSerializer

#     def get(self, request, *args, **kwargs):
#         users = User.objects.all()
#         ser = self.serializer(users, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response({'detail':ser.data}, status=status.HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         ser = self.serializer(data=data)
#         if ser.is_valid(raise_exception=True):
#             ser.save()
#             return Response({'detail':ser.data}, status=status.HTTP_201_CREATED)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response({'detail':ser.errors}, status=status.HTTP_400_BAD_REQUEST)



# class ArticleList(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]
#     serializer = ArticleSerializer

#     def get(self, request):
#         articles = Article.objects.all()
#         ser = self.serializer(articles, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response({'detail':ser.data}, status=status.HTTP_200_OK)

#     def post(self, request):
#         # data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({'detail':serializer.data}, status=status.HTTP_201_CREATED)
#             # return JsonResponse(serializer.data, status=201)
#         # return JsonResponse(serializer.errors, status=400)
#         return Response({'detail':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetail(APIView):

#     def get_object(self, id):
#         try:
#             article = Article.objects.get(id=id)
#             return article
#             # return Response({'detail':serializer.data}, status=status.HTTP_200_OK)

#         except Article.DoesNotExist:
#             return Response({'detail': 'Article does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article)
#         return Response({'detail':serializer.data}, status=status.HTTP_200_OK)

#     def put(self, request, id):
#         # data = JSONParser().parse(request)
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({'detail':serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({'detail':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#         # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         article = self.get_object(id)
#         article.delete()
#         return Response({'detail':'article deleted'}, status=status.HTTP_204_NO_CONTENT)




# class ArticleViewSet(viewsets.ViewSet):

#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({'detail':serializer.data}, status=status.HTTP_200_OK)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'detail':serializer.data}, status=status.HTTP_201_CREATED)
#         return Response({'detail':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response({'detail':serializer.data}, status=status.HTTP_200_OK)



# class ArticleList(generics.GenericAPIView, mixins.ListModelMixin,
#                 mixins.CreateModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     authentication_classes = (TokenAuthentication,)

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)

# class ArticleDetail(generics.GenericAPIView, mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     lookup_field ='id'
#     # lookup_url_kwarg = 'id'

#     def get(self, request, id):
#         return self.retrieve(request, id=id)

#     def put(self, request, id):
#         return self.update(request,id=id)
    
#     def delete(self, request, id):
#         return self.destroy(request,id=id)



''' use again
# Create your views here.
@api_view(('GET','POST'))
def article_list(request):

    # get all articles
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response({'detail':serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'detail':serializer.data}, status=status.HTTP_201_CREATED)
            # return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)
        return Response({'detail':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET','PUT','DELETE'))
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
        # return Response({'detail':serializer.data}, status=status.HTTP_200_OK)

    except Article.DoesNotExist:
        return Response({'detail': 'Article does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        # return Response({'detail':serializer.data}, status=status.HTTP_200_OK)
        return Response({'detail':serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'detail':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'detail':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response({'detail':'article deleted'}, status=status.HTTP_204_NO_CONTENT)

'''