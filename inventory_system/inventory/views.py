from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from inventory.models import Product
from inventory.serializers import ProductSerializer

# Create your views here.
"""def server_status_view(request):
    
    context = {
        "status":"Inventory loaded successfully",
        "machine":"macintosh",
        "low_stock_item":[
            {"name":"M1 chip", "quantity":2},
            {"name":"oneplus mobile", "quantity": 1},
            {"name":"Django projects", "quantity":3}
        ],
        "trainer_msg":"This is the first backend server site."
    }
    return render(request, "dashboard.html", context)"""

def orders(request):
    orders_details = {
        "results":[
            {"product":"biscuit", "price": 500, "date":"20 May 2026"}
        ]
    }
    return render(request, "dashboard.html", orders_details)




def server_status_view(request):
    # 2. Use the ORM to fetch EVERY single row currently sitting in your database
    # This automatically runs "SELECT * FROM inventory_product" under the hood!
    db_products = Product.objects.all()
    
    context = {
        "status": "LIVE DATABASE CONNECTED",
        "low_stock_item": db_products  # 3. Pass the live database rows straight to the HTML
    }
    return render(request, "dashboard.html", context)



@api_view(['GET','POST']) 

def product_api_List(request):
    if request.method == 'GET':
        db_records = Product.objects.all()
        serializer = ProductSerializer(db_records, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT', 'DELETE'])

@api_view(['GET', 'PUT', 'DELETE'])
def product_api_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response({"message": "Product successfully deleted"}, status=status.HTTP_204_NO_CONTENT)



class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all().order_by('-date_added')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name']