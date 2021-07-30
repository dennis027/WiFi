## WiFi App

## Author
Dennis Kimani
  
# Description  
a web application that provides user interface on how to subscribe to diffrent wifi bundles
##  Live Link  
 Click [View Site](https://den-wifi.herokuapp.com/)  to visit the site
  

 
## User Story  
* Sign in with the application to start using.
* Set up a profile about me 
* Find a list of different wifi packages
* Find Contact Information for wifi packages
* subscribe for your request to be added to database
* Change My package anytime.

  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/dennis027/WiFi.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd project-awwards pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations instagram
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
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  

 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* when a user create a new subscription it does not update it creates a list 
  
## Contact Information   
If you have any question or contributions, please email me at [machariad196@gmail.com]  
  
## License 
This project is under the  [MIT](LICENSE) licence