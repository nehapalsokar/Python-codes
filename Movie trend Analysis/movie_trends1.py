import requests
#from apikeys import TMDB_KEY
import apikeys
#print("Key is:", apikeys.TMDB_KEY)
KEY = apikeys.TMDB_KEY
#print(KEY)
# if __name__ == "__main__":
#     def main():
print("Enter any 5 genres in the form of comma separated genre id's: ")
print("genre options: \n 12: 'Adventure',\n  14: 'Fantasy',\n 16: 'Animation',\n 18: 'Drama',\n 27: 'Horror',\n 28: 'Action',\n 35: 'Comedy',\n 36: 'History',\n 37: 'Western',\n 53: 'Thriller',\n 80: 'Crime',\n  99: 'Documentary',\n  878: 'Science Fiction',\n 9648: 'Mystery',\n 10402: 'Music',\n 10749: 'Romance',\n 10751: 'Family',\n 10752: 'War'\n ,10770: 'TV Movie'")
                        
                        
print("Enter in the following format- 27,28,35,80,18")
#genre_list = input('--> ')
genre_list = [int(x) for x in input().split(",")]



# main()


#Request for genres:
CONFIG_PATTERN = 'https://api.themoviedb.org/3/genre/movie/list?language=en-US&api_key='+str(KEY)



url = CONFIG_PATTERN.format(key=KEY)
r = requests.get(url)
config1 = r.json()

#make a dictionary with genre id's and names:
f={config1['genres'][i]['id']:config1['genres'][i]['name'] for i in range(len(config1['genres']))}

#Requests for all months of 2017:
#Months:
Jan='https://api.themoviedb.org/3/discover/movie?language=en-US&primary_release_year=2017&page=1&primary_release_date.lte=2017-01-31&api_key='+str(KEY)

Feb='https://api.themoviedb.org/3/discover/movie?language=en-US&primary_release_year=2017&page=1&primary_release_date.gte=2017-02-01&primary_release_date.lte=2017-02-28&api_key='+str(KEY)
    
Mar='https://api.themoviedb.org/3/discover/movie?language=en-US&primary_release_year=2017&page=1&primary_release_date.gte=2017-03-01&primary_release_date.lte=2017-03-31&api_key='+str(KEY)
    
Apr='https://api.themoviedb.org/3/discover/movie?language=en-US&primary_release_year=2017&page=1&primary_release_date.gte=2017-04-01&primary_release_date.lte=2017-04-30&api_key='+str(KEY)
    
May='https://api.themoviedb.org/3/discover/movie?language=en-US&primary_release_year=2017&page=1&primary_release_date.gte=2017-05-01&primary_release_date.lte=2017-05-31&api_key='+str(KEY)

Jun='https://api.themoviedb.org/3/discover/movie?language=en-US&primary_release_year=2017&page=1&primary_release_date.gte=2017-06-01&primary_release_date.lte=2017-06-30&api_key='+str(KEY)

Jul='https://api.themoviedb.org/3/discover/movie?language=en-US&primary_release_year=2017&page=1&primary_release_date.gte=2017-07-01&primary_release_date.lte=2017-07-31&api_key='+str(KEY)

Aug='https://api.themoviedb.org/3/discover/movie?language=en-US&primary_release_year=2017&page=1&primary_release_date.gte=2017-08-01&primary_release_date.lte=2017-08-31&api_key='+str(KEY)

Sep='https://api.themoviedb.org/3/discover/movie?language=en-US&primary_release_year=2017&page=1&primary_release_date.gte=2017-09-01&primary_release_date.lte=2017-09-30&api_key='+str(KEY)

Oct='https://api.themoviedb.org/3/discover/movie?language=en-US&primary_release_year=2017&page=1&primary_release_date.gte=2017-10-01&primary_release_date.lte=2017-10-31&api_key='+str(KEY)

Nov='https://api.themoviedb.org/3/discover/movie?language=en-US&primary_release_year=2017&page=1&primary_release_date.gte=2017-11-01&primary_release_date.lte=2017-11-30&api_key='+str(KEY)

Dec='https://api.themoviedb.org/3/discover/movie?language=en-US&primary_release_year=2017&page=1&primary_release_date.gte=2017-12-01&primary_release_date.lte=2017-12-31&api_key='+str(KEY)



def genre_month(input_month,input_genre):
    month=input_month+"&with_genres="+str(input_genre)
    #print(month)
    KEY = 'KEY'
    url = month.format(key=KEY)
    r = requests.get(url)
    config = r.json()
    #print(config)
    count_releases=config['total_results']
    #print(count_releases)
    return(count_releases)


month_list=[Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]
def data_each_genre(genre):
    all_months_data=[]
    for month in month_list:
        count_g=genre_month(month,genre)
        print(".",end=" ",flush = True)
        all_months_data.append(count_g)
    return list(all_months_data)   

#genre_list=[27,28,35,80,18]

def all_data():
    list_of_list=[]
    for each in genre_list:

        save=data_each_genre(each)
        list_of_list.append(save)
        #print(save)
    return(list_of_list)


from bokeh.plotting import figure, output_file, show

def visualization():
    output=all_data()

    x = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    #print(x)
    y0 = output[0]
    y1 = output[1]
    y2 = output[2]
    y3 = output[3]
    y4 = output[4]
    #y_plt= data_each_genre()
    output_file("genre_by_season.html")
    
    # add some renderers
    #p.line(x, x, legend="y=x")
    p = figure(x_range=x)
    p.line(x, y0, legend=f[genre_list[0]], line_width=3)
    p.line(x, y1, legend=f[genre_list[1]], line_color="red",line_width=3)
    p.line(x, y2, legend=f[genre_list[2]], line_color="orange",line_width=3)
    p.line(x, y3, legend=f[genre_list[3]], line_color="Green",line_width=3)
    p.line(x, y4, legend=f[genre_list[4]], line_color="Pink",line_width=3)

    p.yaxis.axis_label = 'Releases'
    p.xaxis.axis_label = 'Months'
    show(p)



visualization()