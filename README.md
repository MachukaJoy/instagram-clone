#  Instagram Clone

### A clone of the website for the popular photo app Instagram

#### By **Joy Machuka**

+ [Description](#Description)
+ [How to run the code](#Setup)
+ [Live Site](#Live-Site)
+ [Technologies](#Technologies-and-Languages-Used)
+ [Authors Info](#Author)
+ [Licence](#Licence)

# Description
This is a Django application that tries to replicate instagram. it allows users create profile and add, update and delete p0sts. It also allows liking and commenting like is the norm on instagram.

## Live-Site
[View Site](https://machukagram.herokuapp.com/)


## BDD
* As a user, I would like to Sign in to the application to start using.
* As a user, I would like to Upload my pictures to the application.
* As a user, I would like to See my profile with all my pictures.
* As a user, I would like to Follow other users and see their pictures on my timeline.
* As a user, I would like to Like a picture and leave a comment on it.

## Setup

To get the project .......  
  
##### Fork then Clone the repository:  
 ```bash 
git clone https://github.com/MachukaJoy/instagram-clone.git 
```
##### Navigate into the folder
 ```bash 
cd instagram-clone
```
##### Create and activate virtual environment  
 ```bash 
pipenv –-three
```
##### Activate Virtual Environment
 ```bash 
pipenv shell 
```  
##### Install Dependencies  
 ```bash 
 pipenv  install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations gram
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test gram
```
Open the application on your browser `127.0.0.1:8000`.


## Known Bugs
There are not any known bugs as at now. But feel free to let us know should you find any.

## Technologies-and-Languages-Used
* Python
* Visualstudio
* Django
* postgress sql

## Support and contact details
Should you have any issues or questions, ideas or concerns feel free to reach out to me. Also feel free to make contribution to the code and can contact me at machukajoy@gmail.com
## Author

- [Joy Machuka](https://github.com/MachukaJoy)
### Licence
[MIT LICENSE](https://github.com/MachukaJoy/instagram-clone/blob/main/LICENSE)<br>


** <br>
Copyright (c) {2022} [Joy Machuka ](https://github.com/MachukaJoy)