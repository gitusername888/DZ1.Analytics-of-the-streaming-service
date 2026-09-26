import math


def average_rating(movies):
    """Функция average_rating(movies) возвращает среднюю оценку по каталогу,
      округленную до одного знака (round)."""
    count = 0
    sum_rating = 0
    for word in movies:
        count += 1
        sum_rating = word.get("rating") + sum_rating   
    return round(sum_rating / count, 1)

def catalog_age_stats(movies, current_year=2026):
    """Функция catalog_age_stats(movies, current_year=2026) возвращает
      кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее),
      где среднее округлено вверх до целого с помощью math.ceil."""
    count = 0
    sum_age = 0
    tuple = ()
    max_year = 0
    min_year = 100
   
       
    for word in movies:
        count += 1
        year = current_year - word.get("year") 
        sum_age = year + sum_age
        
        if year > max_year:
            max_year = year
            name_old_film = word.get("title")
        elif year < min_year:
            min_year = year
            name_new_film = word.get("title")
    sr_year = math.ceil(sum_age/ count)
    
    tuple = (name_old_film, name_new_film, sr_year)
    return tuple

def duration_in_hours(minutes):
    """Функция duration_in_hours(minutes) переводит минуты в формат "2ч 35м", 
    используя целочисленное деление и остаток от деления."""
    hours = minutes // 60
    min_at_houres = minutes % 60
    string_min = str(hours) + 'ч ' + str(min_at_houres) + 'м'

    return string_min

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", 
                                                    "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
] 

print(average_rating(movies))
print(catalog_age_stats(movies, 2026))
print(duration_in_hours(98))