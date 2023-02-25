# Homework Flask
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

# Home Work Flask and SQL
Use SQL features first and only then python.
 Old views should be in a separate blueprint, new ones in a new one.  Don't forget to fix the old views so that they continue to work.

 1. The view function should display the number of unique artists from the tracks table.
 PATH: /names/

 2. The view function should display the number of records from the tracks table.
 PATH: /tracks/

 3. The view function should take the name of the genre of the track and output the number of records of this genre (genre) from the tracks table.
 PATH: /tracks/<genre>

 4. The view function should output all track titles (title) and the corresponding track duration in seconds (length) from the tracks table.
 PATH: /tracks-sec/

 5. The view function should output the average duration of a track and the total duration of all tracks in seconds from the tracks table.
 PATH: /tracks-sec/statistics/

 you need to add one table tracks to the database
 it should have the following columns
 id - unique identifier, number
 title - track title, string
 artist - artist name, string
 genre - genre name, string
 length - composition duration in seconds, number
