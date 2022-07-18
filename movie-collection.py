import json
import os
import sys

# ******** VARIABLES AND DATA STRUCTURES ********

movies = []
genre_categories = {'action': 0, 
    'adventure': 0, 
    'animation': 0, 'comedy': 0, 'crime': 0, 'drama': 0, 
    'fantasy': 0, 'experimental': 0, 'horror': 0, 'mystery': 0, 
    'romance': 0, 'sci-fi': 0, 'thriller': 0,
  }


menu = '''

		     MOVIE COLLECTION DATABASE		


		 ************ OPTIONS ************
		===================================

		[1]  Display Movie Titles
		[2]  Find Movie Title
		[3]  Find Movies by Director
		[4]  Find Movies by Genre
		[5]  Add Movie to Database
		[6]  Delete Movie
		[7]  Display Movie Category Stats
										
		===================================
		
		   Select Option or 'q' to Quit		
'''


# ******** FUNCTION DEFINITIONS ********

def open_collection():
    '''Open/create json file for movie collection and populates movie list.'''
    try:
        with open('db_movie_collection.json', 'r') as fp:
            current_movies = json.load(fp)
            for movie in current_movies:
                movies.append(movie)
    except FileNotFoundError:
        with open('db_movie_collection.json', 'w') as fp:
            json.dump(movies, fp)


def display_menu():
    '''Function allowing user to choose different options.'''
    os.system('clear')
    print(menu)
    menu_choice = input("Enter your option: ")
    
    if menu_choice == '1':
        display_movie_titles()
    elif menu_choice == '2':
        movie_title = input("Enter movie title: ").lower()
        movies_found = search_for_movies(movie_title)
        show_movies_found(movies_found)
    elif menu_choice == '3':
        director_name = input("Enter director's name (First Last): ").lower()
        movies_found = search_for_movies(director_name)
        show_movies_found(movies_found)
    elif menu_choice == '4':
        genre = input("Enter movie genre: ").lower()
        movies_found = movies_by_genre(genre)
        show_movies_found(movies_found)
    elif menu_choice == '5':
        add_movie()
    elif menu_choice == '6':
        user_title = input("Enter movie title to be deleted: ").lower()
        delete_movie(user_title)
    elif menu_choice == '7':
        get_collection_summary()
    elif menu_choice == 'q':
        sys.exit()

# MENU OPTION 1: Display Movie Titles
def display_movie_titles():
    '''Shows all movie titles in the json database.'''
    index = 1
    print("\nMOVIE TITLES")
    print("--------------------------------")
    for movie in movies:
        for k, v in movie.items():
            if k == 'Title':
                print(f'{index:3} {v.title()}')
                index += 1
    back_to_menu()

# MENU OPTION 2/3: Search for movie based on user's option
def search_for_movies(searched_value):
    '''Searching for movies in the dictionary.'''
    movie_titles = []
    for movie in movies:
        for value in movie.values():
            if  value == searched_value:
                movie_titles.append(movie)
    if movie_titles:
        return movie_titles
    else:
        return None 


def show_movies_found(movies_found):
    '''Print movies found.'''
    if movies_found:
        for movie in movies_found:
            display_movie_info(movie)
            print('\n--------------------------------')
        back_to_menu()
    else:
        print("I have not found movies matching your search criteria.")
        back_to_menu()


def display_movie_info(movie_found):
    '''Display movie information'''
    for k, v in movie_found.items():
        if k == 'Genre':
            print(f'{k:14}:')
            for genre in v:
                print(f'  - {genre}')
        else:
            print(f'{k:14}: {v.title()}')


# OPTION 4: Searching movies by given genre
def movies_by_genre(user_genre):
    '''Searches movie database and findes particular genre.'''
    movie_titles = []
    for movie in movies:
        for movie_genre in movie['Genre']:
            if user_genre == movie_genre:
                movie_titles.append(movie)
    if movie_titles:
        return movie_titles
    else:
        return None


# OPTION 5: Adding and Saving Movie Information in the Database.
def add_movie():
    while True:
        create_movie_information()
        answer = input("\nAdd another movie [y/n]? ").lower()
        if answer != 'y':
            save_collection()
            break
    back_to_menu()


def create_movie_information():
    '''Collecting user information about a movie.'''
    print("\nProvide the following information:")
    movie_title = input("Movie title: ").lower()
    director = input("Director: ").lower()
    year = input("Year: ")
    rating = input("Parent rating: ").lower()
    length = input("Length: ").lower()
    genre = input("Genre (words separated with comma): ").lower()
    genre = genre.split(', ')
    movie_info = collect_movie_info(movie_title, director,
        year, rating, length, genre)

    movies.append(movie_info)


def collect_movie_info(movie_title, director, year,
    rating, length, genre):
    '''Function collecting information about a movie.'''
    movie_info = {
      'Title': movie_title,
      'Director': director,
      'Year': year,
      'Parent Rating': rating,
      'Length': length,
      'Genre': genre
      }

    return movie_info


def save_collection():
    '''Save current movie list into the json file.'''
    with open('db_movie_collection.json', 'w') as fp:
        json.dump(movies, fp)


# OPTION 6: Deleting movie from the Database.
def delete_movie(user_title):
    '''Deletes movie (dictionary) from the database.'''
    movie_index = 0
    for movie in movies:
        for k, v in movie.items():
            if k == 'Title':
                movie_title = v
        if movie_title == user_title:
            answer = input(f'Are you sure you want to remove movie "{user_title}" [y/n]: ')
            if answer == 'y':
                del movies[movie_index]
                save_collection()
                print(f'Movie "{user_title}" has been removed from the database.')
                break
        else:
            movie_index += 1
    back_to_menu()


# OPTION 7: Collect movie genre statistics.
def get_collection_summary():
    '''Displays movie collection summary.'''
    for movie in movies:
        for k, v in movie.items():
            if k == 'Genre':
                movie_categories = v
        for category in movie_categories:
            genre_categories[category] = genre_categories[category] + 1
    display_category_summary()


def display_category_summary():
    '''Prints movie category summary.'''
    print("\n ******** MOVIE CATEGORY SUMMARY ******\n")
    for category, number in genre_categories.items():
        print(f'  {category.upper():14} \t{number}')
    print('--------------------------------------')
    back_to_menu()


def back_to_menu():
    '''Pauses after a task before displaying menu.'''
    answer = input("\nPress any key to continue... ")
    display_menu()


# ******** CODE ********
# open_collection - create/open json file 
open_collection()
display_menu()
