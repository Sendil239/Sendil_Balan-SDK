# Overview

psbSDK is a Python package that provides an interface for accessing movie-related data from the API provided by 'The One API'. The package consists of three modules: movieAPI, movieFilters, and movieSDK.

The movieAPI module is responsible for making HTTP requests to the API and returning the corresponding JSON responses. The movieFilters module is responsible for building the filtering, sorting, and pagination options that can be applied to the API requests. Finally, the movieSDK module provides a high-level interface for users to interact with the API and retrieve movie-related data.

# Modules
## movieAPI
The movieAPI module is responsible for handling HTTP requests to the API and returning the corresponding JSON responses. The module provides a single class named MovieAPI that takes a movieObj object as a parameter. The movieObj object contains information such as the API token, the type of movie data to retrieve, the movie ID, and any filter options. The MovieAPI class is responsible for building the API request URL based on the information in the movieObj object. The class also handles any API request errors and returns a human-readable error message if necessary.

## movieFilters
The movieFilters module is responsible for building the filtering, sorting, and pagination options that can be applied to the API requests. The module provides a single class named Filters that contains methods for building the different filter options. The Filters class maintains a dictionary that maps filtering operators (e.g., "eq", "neq", "gte", "lte") to their corresponding symbols (e.g., "=", "!=", ">=", "<="). The Filters class also has methods for adding filters, checking if a field exists or not, sorting, and pagination.

## movieSDK
The movieSDK module provides a high-level interface for users to interact with the API and retrieve movie-related data. The module provides a single class named Movies that takes a Token parameter as well as other optional parameters such as Type, MovieId, and FilterObj. The Movies class is responsible for creating a movieObj object that contains the relevant information for building the API request URL. The class also provides two methods: get_movie and get_movie_by_name. The get_movie method retrieves movie data based on the movieObj object and returns a JSON-formatted string. The get_movie_by_name method retrieves movie data based on the movie name provided as a parameter and returns a JSON-formatted string.


# Class Diagram

The class diagram below illustrates the relationships between the classes in the MovieSDK package:
```
+-----------+           +------------+
|  Movies   |           |   Filters  |
+-----------+           +------------+
| +Token    |           | +filters   |
| +Type     |           | +add_filter|
| +MovieId  |           | +is_exist  |
| +FilterObj|           | +sort      |
| +get_movie|           | +set_offset|
| +get_movie|           | +set_limit |
| +by_name  |           | +set_page  |
+-----------+           +------------+
        |                         |
        |   +-------------+      |
        +---|   MovieAPI  |      |
            +-------------+      |
            | -base_url   |      |
            | -headers   <--------+
            | -MovieId    |
            | -MovieType  |
            | -filterObj  |
            | +parse_filter |
            | +form_url  |
            | +get

```

# Requirements

Python 3.6 or above

Requests library (https://requests.readthedocs.io/en/master/)

The One API token (https://the-one-api.dev/sign-up)

# Details of the SDKs
## Create a Filter Object.
- The filter operations include
    - "eq": "=", ----------> equals
    - "neq": "!=", --------> not equals
    - "not": "!", ---------> not
    - "gte": ">=", --------> greater than equal
    - "lte": "<=", --------> less than equal
    - "gt": ">", ----------> greater than
    - "lt": "<" -----------> less than

## Create a Movie object.
- Initialize movie object with below
    - Token: The One API token.
    - Type: The type of movie search to perform, default value is "MovieList".
    - MovieId: The ID of the movie to retrieve.
    - FilterObj: A Filters object containing filters to apply to the query.
- Use your One API token to hit the calls.
- Movie object has three types 
    - "MovieList" (Default) -> get movies list
    - "MovieId" -> get movie by ID
    - "MovieQuotes" -> get quotes from specific movies using ID.

### Multiple params support is given so you can add multiple filters to same object and hit API calls.