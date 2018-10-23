# FoodTruckFinder
This is a simple web API to get the nearest food trucks from a csv file. The output will be list of 5 closest food trucks that haven't been visited before. 

## Process flow
For this matter the app gets the geolocation of the person who's running the application. Other inputs are list of the food trucks that have been visited before and list of all the food trucks. The algorithm fisrt clears the list and finds the ones that haven't been visted before and then calculates the distance between the person and the Food Trucks in that list. Finally it gives top 5 new Food Trucks as the output. 

## Output representation
The service is a GET request that gets a list of new Food Trucks and turns it into JSON format. 
To make it easier for the user the output will be shown in a web app. 
The web app loads on locadhost port: 5000 so the homepage will be: [homepage](http://localhost:5000/home) 

## Languages and APIs
The service and the algorithm are written in Python. To run the app in the backend, required libraries are listed in the imports just in case they are not already installed. 
Flask is used to connect the python app to web app.
Google map API is used to show the location of the user. The web app and layout are html and css. 

The service is  a GET on /home/response/truck
As it's mentioned before the response is a JSON format.

For the input files on the happy path, it is assumed that they are downloaded in a specific directory. App will look for the big list of trucks from the city in "fullList/Mobile_Food_Facility_Permit.csv"
And it will look into "dumpdata/Mobile_Food_Facility_Permit.csv" for the used ones.

The python code contains two different .py codes, foodTruck.py and main.py. dooftruck.py gets two files find the differences and creates a list of the "new" or "non-visited" Food Trucks. I assumed any food truck that contains a new type of food even if it shares the same company as some others would be a new or non-visited foodtruck. Then it gets the distance from user's geolocation and the ones in the list. It finds the top 5 closest ones to the user and show selective information to send as JSON response to the output. 

## future enhancements
1. The web app should show the location of the food trucks on Google map API which due to the time constaint it hasn't been implemented into the app.  A list from the latitude and longitude of the output is lready created. We can send them using "render_template" to a javascript and loop through them in the web app to mark those locations. 
2. The service should get the lists from the city rather than read from a static point. There was no direct access in this project. 
3. The project can be uploaded to a server so that in future users can hit web url and access to the web app to run the application.

## To run the application
"main.py" contains the main method. After running that in commandpromt/Spyder,... you can open localhost to get the request. 
The web app loads on locadhost port: 5000 so the homepage will be: [homepage](http://localhost:5000/home) 





