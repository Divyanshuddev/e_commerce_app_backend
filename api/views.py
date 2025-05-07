from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User,Product
from .serializer import UserSerializer,ProductSerializer
from django.db.models import Sum
import uuid
@api_view(['GET'])
def get_user(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def sign_up_user(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def authentication(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if User.objects.filter(email=email).exists() and User.objects.filter(password=password).exists():
        return Response("Login Successfully", status=status.HTTP_200_OK)
    else:
        return Response("Invalid email or password",status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_product(request):
    products=Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_product(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_wish_list(request):
    product_id = request.data.get('id')
    wish_list_value = request.data.get('like')
    if not product_id:
        return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        product_id=uuid.UUID(product_id)
        product = Product.objects.get(product_id=product_id)
    except Product.DoesNotExist:
        return Response({'error':"Product not found"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product,data={'wish_list':wish_list_value},partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def count_likes(request):
    product= Product.objects.filter(wish_list=True)
    serializer= ProductSerializer(product,many=True)
    if serializer != None:
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_add_to_cart(request):
    product_id=request.data.get('id')
    cart=request.data.get('cart')
    if not product_id:
        return Response({'error':'Product ID is required'})
    try:
        product_id=uuid.UUID(product_id)
        product=Product.objects.get(product_id=product_id)
    except Product.DoesNotExist:
        return Response({'error':"Product not found"},status=status.HTTP_404_NOT_FOUND)
    serializer= ProductSerializer(product,data={'cart':cart},partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def count_cart(request):
    product= Product.objects.filter(cart=True)
    serializer= ProductSerializer(product,many=True)
    if serializer != None:
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_product_by_id(request, product_id):
    product_id=uuid.UUID(product_id)
    try:
        product = Product.objects.get(pk=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({'error': "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_total_price(request):
    all_list=Product.objects.filter(cart=True).values_list('quantity','price')
    sum=0
    for i in all_list:
        sum+=i[0]*i[1]
    return Response(sum, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_quantity(request):
    product_id=request.data.get('product_id')
    quantity=request.data.get('quantity')
    if not product_id:
        return Response({'error':"Product ID is required"})
    try:
        product_id=uuid.UUID(product_id)
        product=Product.objects.get(product_id=product_id)
    except Product.DoesNotExist:
        return Response({'error':"Product not found"},status=status.HTTP_404_NOT_FOUND)
    serializer= ProductSerializer(product,data={'quantity':quantity},partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_product_by_category(request, type):
    try:
        products = Product.objects.filter(category=type)
        if not products.exists():
            return Response({'error': "No products found in this category"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PATCH'])
def change_category(request,product_id):
    category=request.data.get('category')
    product_id=uuid.UUID(product_id)
    try:
        product=Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'error':"Product not found"},status=status.HTTP_404_NOT_FOUND)
    serializer=ProductSerializer(product,data={'category':category},partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

