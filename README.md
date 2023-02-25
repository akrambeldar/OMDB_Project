# OMDB_Project
A python program to extract data from a REST API and transform it to relevant data set and store it in an excel sheet.

# REST API
A set of limitations for using in the development of web services are defined by the architectural style known as Representational State Transfer (REST). REST API is a straightforward and flexible method of accessing web services without any processing. As REST requires less bandwidth and is more suitable for internet use, it is often preferred. It is utilised to obtain or provide data from an online service. Via the REST API, only HTTP requests are used for communication.

# FUNCTIONS USED 

GET: To read (or retrieve) a representation of a resource, use the HTTP GET technique. When using the safe route, GET returns the user-requested representation in XML or JSON along with an HTTP response code of 200. (OK). It typically returns a 404 (NOT FOUND) or 400 in an error event (BAD REQUEST).

# METHODOLOGY
* The response.json() gives you an object containing everything that was there in the response
* In this particular scenario - the information that we required was placed in an array, accessible by hitting the key named "data" in the json. Which is why we assign response.json()['Search'] to our variable data.
* The variable data here now contains an array of objects.
* The to extract the keys of the first object in the array, type-cast it into a list for ease of access and store it in the variable called _headers_.
* So to get the values; the RHS  of every object in the array, we iterate over every object in the array and call their ".values()" function to extract the values.
* The later part uses the Pandas library to write to an excel sheet that contains the headers and data. The excel file name is given with the file destination.
