"# book-api" 

virtualenv [name]
pip install -r requirements.txt


----------------------------------------------------------------
https://www.quora.com/What-is-the-difference-between-the-Django-and-Django-REST-frameworks

Django and DRF( Django Rest Framework ) are different in the way they are being used. If you want to create a web application django will be helpful for that and if you want to create APIs only then DRF can be useful.
Yes you can create API kind of a structure in django as well but DRF will provide many more functions to make it easier for you like serializers , filtering and OAuth support, or Markdown, PyYAML, defusedxml for Markdown, YAML, XML content types support etc.
So basically you can say if you want to create APIs only you should be using DRF. and if you have to create web application you should be using Django.


https://stackoverflow.com/questions/49109791/django-or-django-rest-framework

Django Rest Framework makes it easy to use your Django Server as an REST API.

REST stands for "representational state transfer" and API stands for application programming interface.

You can build a restful api using regular Django, but it will be very tedious. DRF makes everything easy.

https://stackpython.co/tutorial/django-rest-framework-api-python

ทำไมต้อง Django REST Framework
มี serializers ที่ช่วยในการแปลง Django, Python object ไปเป็น JSON ได้อย่างง่ายดาย
Browsable API คือมีหน้า Interface ในการเรียกดู ทดสอบ API ในตัว ทำให้ง่ายและสะดวกขึ้นมาก


https://www.quora.com/Can-someone-compare-advantages-and-disadvantages-of-using-Django-REST-framework-Piston-and-Tastypie
Tastypie:
Advantages:
Easy to get started with and provides basic functionalities OOB (out of the box)
Most of the time you won’t be dealing with Advanced Django concepts like CBVs, Forms etc
More readable code and less of magic!
If your models are NON-ORM, go for it.

Disadvantages:
Doesn’t strictly follow idiomatic Django (mind well python and django’s philosophies are quite different)
Probably bit tough to customize APIs once you go big
No O-Auth


DRF:

Follows idiomatic Django. (If you know Django inside out, and are very comfortable with CBVs, Forms etc, go for it without any doubt)
Provides out of the box REST functionality using ModelViewSets. At the same time, provides greater control for customization using CustomSerializer, APIView, GenericViews etc.
Better authentication. Easier to write custom permission classes. Works very well and importantly very easy to make it work with 3rd party libraries and OAuth. DJANGO-REST-AUTH is worth mentioning LIBRARY for Auth/SocialAuthentication/Registration.
Disadvantages:

If you don’t know Django very well, don’t go for this.
Magic! Some time very hard to understand magic. Because its been written on top of Django’s CBV which are in turn quite complex in nature.
Has steep learning curve.