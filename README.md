# DATABOT Ecommerce API

**Installation**
```xml
pip install pipenv
pipenv shell
```

```xml
pipenv install django djangorestframework pillow django-cors-headers djangorestframework-simplejwt
```

`to start the app`
```xml
django-admin startproject databot ./

python manage.py startapp authentication
python manage.py startapp product
python manage.py startapp order
```

`for running TestCase`
```xml
pipenv install coverage 

coverage run manage.py test && coverage report && coverage html
```


`for swagger`
*currently having problem with the swagger I Installed, so pls make use of postman or Install ThunderClient on your VSCode*
```xml
pipenv install  drf-yasg
```

### Description of project
The project about building an API that keep record of our clients that visited our sites to purchase a particular product. 
In respect to this, the client login details, orders history and payment history are been stored.

**In The Authentication Section**
- In the models.py, 
- I implementated the registeration and login models and routes(even though I had to skip it), I did it so any user can register and login, then upload data to the API without having to go through the admin section to do it
- added logout ability to the API.
-  a user can change password 
-  a user can edit their profile

    `*for authenticated users*` -->  use http://127.0.0.1:8000/auth/

    ('register/', RegisterAPIView.as_view(), name='register')

    ('login/', LoginAPIView.as_view(), name='login')

    ('logout/',LogoutView.as_view(), name='logout')

    ("update_password/", updatePassword, name="updateUser")

    ('update/<str:pk>/', updateUser, name='user-profile-update')

    ('profile/', getUserProfile, name="user-profile")

    `*for admin user*` use http://127.0.0.1:8000/auth/

    ('users/', getUsers, name="users")

    ('user/<str:pk>', getUserById, name="user") 

    ('delete_user/<str:pk>', deleteUser, name="delete-User")  

**In The Product Section**
- In the product section, I Created a Route where a user can get a get products
- get top products
- even create reviews

    `*for authenticated user*` use http://127.0.0.1:8000/product/

    path('', getProducts, name="products")

    path('<str:pk>/reviews/', createProductReview, name="create-review")

    path('top/', getTopProducts, name='top-products')

    path('<str:pk>/', getProduct, name="product")

    `*for admin user*` use http://127.0.0.1:8000/product/

    path('update/<str:pk>/', updateProduct, name="product-update")

    path('delete/<str:pk>/', deleteProduct, name="product-delete")

    path('create/', createProduct, name="product-create")

    path('upload/', uploadImage, name="image-upload")
]

**In The Order Section**
- get all orders
- get a particular order
- update order and even link for payment but I didn't add a payment gateway, left it for frontend engs.

   
    `*for authenticated user*` use http://127.0.0.1:8000/order/

    ('add/', addOrderItems, name='orders-add')

    ('myorders/', getMyOrders, name='myorders')

    ('<str:pk>/', getOrderById, name='user-order')

    ('<str:pk>/pay/', updateOrderToPaid, name='pay')

    `*for admin user*` use http://127.0.0.1:8000/order/
    
    ('', getOrders, name='orders')

    ('<str:pk>/deliver/', updateOrderToDelivered, name='order-delivered')

    
    


