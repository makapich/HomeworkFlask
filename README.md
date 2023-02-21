# HomeworkFlask
1. Return the contents of a file with python packages (requirements.txt):
 PATH: /requirements/ - open the requirements.txt file and return its contents

 2. Display 100 randomly generated users (mail + name)
 For example - 'Dmytro aasdasda@mail.com'
 (you can use - https://pypi.org/project/Faker/ )
 PATH: /generate-users/ + GET parameter that controls the number of users (/generate-users/?count=100)

 3. Display average height, average weight (cm, kg) (from the attached file hw.csv)
 PATH: /mean/
 PAY ATTENTION TO THE UNITS OF MEASUREMENT

 4. Display the number of astronauts at the moment
 (API source http://api.open-notify.org/astros.json )
 (use the library https://pypi.org/project/requests/ )
 PATH: /space/


 3rd Party API Request Example
 import requests
 r = requests.get('https://api.github.com/repos/psf/requests')
 r.json()["description"]
