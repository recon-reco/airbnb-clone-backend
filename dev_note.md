> 프로젝트가 실행되는 환경에 대한 정보를 가지고 있다.  
> 버블 안으로 들어가는 방법 :

```
$poetry init
$poetry add django

//in
$poetry shell
$django-admin

//out
$exit
```

Pylance?  : python server for VScode   
select python 옆의 가상환경    
formatter black    

각 파일의 의미

```
django-admin startproject config .

```

extension

django is oop framework

about OOP

```
//class
// __init__(self):
모든 Python class 안에 있는 모든 메서드는 첫 번쨰 인자로 self를 넘겨받는다.
//inheritance :
nico = Fan("nico", "blue") <- Fan class의 __init__을 호출
property /attribute

메소드 오버라이딩
underScore method
클래스가 문자열로 보이는 방식을 커스터마이징 : __str__(self) <- 클래스 인스턴스(객체)가 보이는 방식을 정의
default : 너의 객체가 어디에 존재하는지 알려준다.
super().__str__()

document

dir(jia) <- 객체의 클레스의 메소드, property를 확인
```

## Django Basic

terminal에서 Django를 실행하기 위한 파일 : manage.py

```
pytho manage.py runserver
```

about port

logger

django_session

migration / migration file apply/ modify shape

```
python manage.py migration
```

super user

```
python manage.py createsuperuser
```

Framework vs Library  
you call Library
framework call our code  
프레임워크는 코드가 작성된 위치를 보고, 코드가 올바른 위치에 있다면,  
우리의 코드를 호출한다.

applications : apps  
장고 app은 application logic과 dataf를 합쳐서 캡슐화한다.  
각각 분리시킬 수 있는 module seperate!!!

## Django Model

**Model** : application에서 데이터의 형태를 정의한 것

```
python manage.py startapp houses
//models.py
//admin.py
python manage.py makemigrations
python manage.py migrate
```

## User App

공식문서 참고 : set up User Model! extend! from the start!

model을 변경할 때마다 makemigrations -> migrate   
=> for Python코드에 있는 모델 구조와 데이터베이스의 구조를 서로 동기화하기 위해서

field set : 필드 순서대로 