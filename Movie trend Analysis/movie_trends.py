# import required modules
import requests
import datetime
import apikeys
from bokeh.plotting import figure, output_file, show

KEY = apikeys.TMDB_KEY
BASE_URI = "https://api.themoviedb.org/3"

def get_last_day_of_month(any_day):
    """Function to return the last day of the month for any day entered.
    Args:
        any_day: Any day of the month.
    Returns:
        Last day of the month for the day entered.
    """
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  
    return next_month - datetime.timedelta(days=next_month.day)

def get_genre_month_data(input_month,input_genre,year_var):
    """Function to fetch the count of releases for a particular month of a year for the genre selected.
    Args:
        input_month: Month of the year.
        input_genre: Genre from the list of genres entered by user.
        year_var: Year entered by the user
    Returns:
        Details in JSON format
    """
    input_date = datetime.date(int(year_var), input_month, 1)
    gte=datetime.date.strftime(input_date,'%Y-%m-%d')

    base_uri='https://api.themoviedb.org/3/discover/movie'
    query_params = {"language":'en-US',
                    "primary_release_year":year_var,
                    "primary_release_date.gte":gte,
                    "primary_release_date.lte":get_last_day_of_month(datetime.date(int(year_var),input_month, 1)),
                    "api_key":KEY,
                    "with_genres":input_genre}
    
    response = requests.get(base_uri,query_params)
    response_json = response.json()
    count_releases=response_json['total_results']
    return(count_releases)

def get_data_each_genre(genre, year_var):
    """Function to count number of releases for genre entered for every month of the year.
    Args:
        genre: Single genre from list of genres
        year_var: Year entered by the user
    Returns:
        A list of count of releases for the genre chosen for all twelve months.
    """
    all_months_data=[]
    
    for month in range(1,13):
        count_genre=get_genre_month_data(month,genre,year_var)
        print(".",end=" ",flush = True)
        all_months_data.append(count_genre)
    return list(all_months_data)   

def get_all_data(genre_list, year):
    """Function to return a list of count of releases for every genre for the year selected by the user.
    Args:
        genre_list: List of 5 genres entered by the user
        year: Year entered by the user
    Returns:
        A list of count of releases for all five genres for the year chosen.
    """
    list_of_genres=[]
    for each in genre_list:
        genre_data=get_data_each_genre(each, year)
        list_of_genres.append(genre_data)
    return(list_of_genres)

def create_genre_visualization(year_var, genre_dict, genre_list):
    """Function to create the plot for releases by genre.
    Args:
        year_var: Year entered by the user
        genre_dict:Dictionary of all genres ID's and corresponding names
        genre_list: List of 5 genres entered by the user
    Returns:
        None.
    """
    output=get_all_data(genre_list, year_var)
    months_in_year = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    output_file("genre_by_season.html")
    line_colors=["Black","Red","Blue","Green","Orange"]
 
    p = figure(x_range=months_in_year,plot_width=800, plot_height=600, title="Releases by Genre:"+str(year_var))
    for i in range(len(genre_list)):
         p.line(months_in_year, output[i], legend=genre_dict[genre_list[i]], line_color = line_colors[i], 
         line_width=3)
    
    p.yaxis.axis_label = 'Releases'
    p.xaxis.axis_label = 'Months'
    show(p)

def get_genre_data():
    """Function to fetch information about the different types of genre.
    Args:
        None.
    Returns:
       Dictionary of all genres ID's and corresponding names.
    """
    base_uri = 'https://api.themoviedb.org/3/genre/movie/list'
    params = {'language':'en-US', 'api_key': KEY}
    genre_response = requests.get(base_uri, params).json()
    # make a dictionary with genre id's and names:
    genre_dict = {genre_response['genres'][i]['id']:genre_response['genres'][i]['name'] for i in range(len(genre_response['genres']))}
    return genre_dict

def get_genre_inputs(genre_dict):
    """Function to display information for the user and return the year and list of genres entered by the user.
    Args:
        genre_dict: Dictionary of all genres ID's and corresponding names.
    Returns:
        Year and list of 5 genres entered by the user.
    """
    year = input("Enter the year:")
    for item in genre_dict:
        print(item, ":", genre_dict[item])
    genre_input = input("Enter any 5 genres in the form of comma separated genre id's: ")          
    genre_list = [int(x) for x in genre_input.split(",")]
    return year, genre_list

def get_actor_id(actor_name):
    """Function to fetch and return the ID for an actor based on the actor name argument.
    Args:
        actor_name: The name of the actor.
    Returns:
        The ID for the actor, or None in case the actor was not found
    """
    resource_path = "/search/person"
    params = {'api_key': KEY, 
              'query': actor_name}
    response = requests.get(BASE_URI + resource_path, params).json()
    if len(response['results']) == 0:
        # actor not found
        return None
    return response['results'][0]['id']

def fetch_movie_details(movie_id):
    """Function to fetch the details for a movie based on its ID.
    Args:
        movie_id: The ID of the movie.
    Returns:
        Movie details in JSON format
    """
    resource_path = "/movie/" + str(movie_id)
    params = {'api_key': KEY }
    return requests.get(BASE_URI + resource_path, params).json()

def get_profit(movie_details):
    """Function to compute profit based on the passed movie details.
    Args:
        movie_details: Dictionary of information about the movie.
    Returns:
        Profit made by the movie.
    """
    budget = movie_details['budget'] # extract budget
    revenue = movie_details['revenue'] # extract revenue
    if budget < 1000 or revenue < 1000:
        # Return None in case the budget and revenue values seem unrealistic
        return None
    return revenue-budget

def get_movie_data_by_actor(actor_name):
    """Function to fetch and return movie data for an actor (release dates and profits).
    Args:
        actor_name: Name of the actor.
    Returns:
        A tuple of two lists, one comprising of movie release dates,
        and the other, the corresponding profits.
    """
    actor_id = get_actor_id(actor_name)  # Fetch actor ID for given name
    if actor_id is None:
        print("Actor not found")  # Return if actor not found
        return 
    dates = []
    profits = []
    resource_path = "/discover/movie"
    params = {'api_key': KEY, 'language': 'en_US', 'with_cast': actor_id, 
              'sort_by': 'primary_release_date.asc', 'page': 1}
    while(True):
        response = requests.get(BASE_URI + resource_path, params).json()  # Fetch movie data for actor
        for result in response['results']:  # For each movie in response
            print(".", end=" ", flush = True) # Show progress bar
            movie_details = fetch_movie_details(result['id']) # Fetch details for this movie
            profit = get_profit(movie_details) # Compute the profit
            if profit is not None:  # If profit data was present and valid
                release_date = movie_details['release_date']  # Extract release date
                dates.append(datetime.datetime.strptime(release_date,'%Y-%m-%d')) # Add to dates list
                profits.append(get_profit(movie_details))  # Compute & add profit to profits list
        if response['page'] == response['total_pages']:  # Break if current page in response was the last page
            break
        params['page'] += 1  # Otherwise, increment the page number to fetch in the next iteration
    return dates, profits

def create_popularity_plot(dates, profits, actor_name):
    """Function to create the actor popularity plot.
    Args:
        dates: A list of movie release dates for the actor
        profits: A list of corresponding profits made by the movie
        actor_name: Name of the actor.
    Returns:
        None.
    """
    output_file("actor_popularity.html")
    plot = figure(plot_width=800, plot_height=600, x_axis_type='datetime',
                    title = actor_name + " Popularity Over Time",
                    x_axis_label = "Date",
                    y_axis_label = "Revenue$")
    plot.line(dates, profits, line_width=2)
    show(plot)

def perform_actor_analysis():
    """Function to initiate actor popularity analysis.
    Args:
    Returns:
        None.
    """
    actor_name = input("Enter the name of an actor: ") # Get user input for actor name
    dates, profits = get_movie_data_by_actor(actor_name) # Extract actor information
    create_popularity_plot(dates, profits, actor_name) # Plot the actor information

def get_user_input():
    """Function to get user input for initiating analysis.
    Args:
    Returns:
        None.
    """
    while True:
        input_string1 = "Which visualization do you want to create?\n"
        input_string2 = "Enter a number (1 or 2)\n1. Releases by Genre  2. Actor Popularity \n"
        choice = input(input_string1 + input_string2)
        if choice == '1': # Genre Analysis
            genre_dict = get_genre_data()
            year, genre_list = get_genre_inputs(genre_dict)
            create_genre_visualization(year,genre_dict, genre_list)
            break
        elif choice == '2': # Actor Popularity Analysis
            perform_actor_analysis()
            break
        else: 
            print("Invalid Choice, please try again")

# Only perform the actor/genre analysis if the program is run directly as a top level script.
if __name__ == "__main__":
    get_user_input()