from psbSDK.movieSDK import Movies
from psbSDK.movieFilters import Filters

# Create a Filter Object with suitable filters.
# The filter operations include
# "eq": "=", ----------> equals
# "neq": "!=", --------> not equals
# "not": "!", ---------> not
# "gte": ">=", --------> greater than equal
# "lte": "<=", --------> less than equal
# "gt": ">", ----------> greater than
# "lt": "<" -----------> less than
fObj = Filters()
fObj.add_filter(field="name", oper="eq", value="/The/i")
fObj.add_filter(field="budgetInMillions", oper="lt", value="100")
fObj.sort(field="id", isAsc=True)
fObj.is_exist(field="id", isExist=True)

# Set page, offset and limit using the below functions.
fObj.set_limit(6)
fObj.set_page(1)
fObj.set_offset(0)

# Create a Movie object and pass the filter object to it.
# Use your One API token to hit the calls.

# Movie object has three types 
# "MovieList" (Default) -> get movies list
# "MovieId" -> get movie by ID
# "MovieQuotes" -> get quotes from specific movies using ID.

movie = Movies(Token="< YOUR TOKEN >", Type="MovieQuotes", MovieId="5cd95395de30eff6ebccde5b", FilterObj=fObj)

print(movie.get_movie())

movie = Movies(Token="< YOUR TOKEN >")

print(movie.get_movie_by_name("The Two Towers"))