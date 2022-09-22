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

**In The Product Section**
- In the product section, I Created a Route where a user can get a get products,
- get top products, 
- even create reviews

**In The Order Section**
-  get a particular order
- update order and even link for payment but I didn't add a payment gateway, left it for frontend engs.


