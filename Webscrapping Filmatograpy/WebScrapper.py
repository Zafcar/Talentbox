import requests
from bs4 import BeautifulSoup

def actor_name_input():
    #input of the actor to search.
    actor_name = input("Enter the actor name: ")
    url = "https://www.rottentomatoes.com/celebrity/" + actor_name.replace(" ", "_")

    #accessing the data of the html site.
    site = requests.get(url)
    return(site.status_code, url)

def scrapping_table(url):

    #gets the entire html of the site.
    html_site = requests.get(url).text

    #passing the html_site to bs4.BeautifulSoup
    soup = BeautifulSoup(html_site, 'html.parser')

    #only getting the movies table form the site of the url.
    table = soup.find('tbody', class_='celebrity-filmography__tbody')

    # storing the movie's title and the year of list in there respective list.
    movies = []
    year_of_release = []

    #for loop iterators over each line which contains the the tag tr.
    for row in table.find_all('tr'):    
        #for loop iterators to each line which contains the the tag td and stores it as a list in column.
        column = row.find_all('td')

        #getting the lines which contains the movie name and the year of release and storing them in list movies and year_of_release.
        movies.append(column[2].text.strip())
        year_of_release.append(column[5].text.strip())
    return(movies, year_of_release)

def display(movies, year_of_release):
    #printing the entire list in a form of a table.
    print ("\n{:<17} {:<15}\n".format('Year of release', 'Title of movie'))
    for i, j in zip(year_of_release, movies):
        print ("{:<17} {:<15}".format(i, j))

def main():
    status_code, url = actor_name_input()
    if(status_code == 200):
        movies, year_of_release = scrapping_table(url)
        display(movies, year_of_release)
    else:
        print("\nCheck the name of the actor")
        print("-----------OR-------------")
        print("Give proper spacing of the actor's name.")
        print("For example, instead of typing Leonardo DiCaprio, type it as Leonardo Di Caprio")
main()
  
