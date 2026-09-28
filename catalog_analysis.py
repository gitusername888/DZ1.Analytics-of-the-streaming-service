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

def catalog_age_stats(movies:list, current_year=2026) ->tuple:
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

def duration_in_hours(minutes:int) -> str: 
    """Функция duration_in_hours(minutes) переводит минуты в формат "2ч 35м", 
    используя целочисленное деление и остаток от деления."""
    hours = minutes // 60
    min_at_houres = minutes % 60
    string_min = str(hours) + 'ч ' + str(min_at_houres) + 'м'

    return string_min

def rating_tier(rating:float) ->str:

    """Напишите функцию rating_tier(rating), которая по оценке возвращает категорию: 
\"шедевр\" (≥9), \"хорошо\" (7–8.9), \"средне\" (5–6.9), \"слабо\" (<5). 
Реализуйте ее через if/elif, а внутри используйте тернарный оператор хотя 
бы один раз."""
    return "шедевр" if rating >= 9 else ("слабо" if rating < 5 else 
                                        ("средне" if rating < 7 else "хорошо"))

def decade_label(year:int) -> str:
    """Напишите функцию decade_label(year), которая через оператор match 
возвращает метку "новые" (после 2020), "недавние" (2015–2020) или 
"старые" (раньше 2015)."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year < 2015:
            return "старые"
        case _:
            return "недавние"

def necomedy (movies):
    """С помощью for и continue выведите на экран (print) названия всех фильмов, 
которые НЕ относятся к жанру "comedy". stage 3"""
    result = []
    for word in movies:
        g = word.get("genres")
        if "comedy" in g:
            continue
        else:
            result.append(word.get("title"))
    return result

def rating_9 (movies):
    """С помощью while и break найдите первый по порядку в 
    списке фильм с рейтингом выше 9.0; если такого фильма нет, цикл 
    должен завершиться веткой else с сообщением "Шедевров не найдено"."""
    count = 0
    rating = 9
    while count < len(movies):
        element = movies[count]
        if element.get("rating") > rating:
            return element.get("title")
            break
        count += 1
    else:
        return "Шедевров не найдено"

def count_long_movies(movies, threshold=120):
    """Напишите функцию count_long_movies(movies, threshold=120), которая через 
    for с накопительной переменной считает количество фильмов длиннее 
    threshold минут."""
    result = 0
    for element in movies:
        g = element.get("duration_min")
        if g > threshold:
            result += 1
        
    return result

def normalize_title(title):

    """Напишите функцию normalize_title(title), которая приводит строку 
    к формату Title Case (каждое слово с заглавной буквы) без использования 
    str.title() напрямую: разбейте строку по пробелам и соберите заново 
    вручную, меняя первую букву каждого слова через срез 
    (word[0].upper() + word[1:])."""
    list_title = title.split(" ")
    sting_title = ""
    count = 0
    for word in list_title:
        norm_title = word[0].upper() + word[1:]
        count += 1
        if count < len(list_title):
            sting_title = sting_title + norm_title + ' '
        else:
            sting_title = sting_title + norm_title
    return sting_title

def make_slug(title):

    """Напишите функцию make_slug(title), которая превращает нормализованное
      название в «слаг» вида the-quiet-algorithm."""

    down_title = title.lower()
    slug_text = down_title.replace(' ', '-')

    return slug_text

def format_report_line(movie:set) -> str:

    """Напишите функцию format_report_line(movie), возвращающую единую 
    строку с описанием фильма.
    '"The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi'"""

    result = f'"{movie.get("title")}" ({movie.get("year")})' 
    result = result + f' — {movie.get("rating")}/10, '
    result = result + f'{duration_in_hours(movie.get("duration_min"))}, '
    gan = sorted(movie.get("genres"))
    result = result + f'жанры: {', '.join(gan)}'
    return result

def titles_sorted_by_rating(movies: list) -> list:

    """Напишите функцию titles_sorted_by_rating(movies), возвращающую список 
    названий фильмов, отсортированных по убыванию рейтинга."""
    result = []
    sorted_list = sorted(movies, key= lambda x: x['rating'], reverse= True)
    for element in sorted_list:
        g = element.get("title")
        result.append(g) 
        
    return result

def top_n_by_rating(movies:list, n=3) -> list:
    """Напишите функцию top_n_by_rating(movies, n=3), возвращающую список 
    из n кортежей (title, rating) — топ по рейтингу."""
    result = []
    sorted_list = sorted(movies, key= lambda x: x['rating'], reverse= True)
    count  = 0
    for count in range (n):
        tuple = (sorted_list[count].get("title"), sorted_list[count].get("rating"))
        result.append(tuple) 
        
    return result

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

movies_9 = [
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
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
] 




#print(average_rating(movies)) # stage 1
#print(catalog_age_stats(movies)) # stage 1
#print(duration_in_hours(98)) # stage 1
#print(rating_tier(4)) # stage 2
#print(decade_label(2016)) # stage 2
#print(necomedy(movies)) # stage 3
#print(rating_9(movies)) # stage 3
#print(rating_9(movies_9)) # stage 3
#print(count_long_movies(movies, 120)) # stage 3
#print(normalize_title("midnight in oslo")) # stage 4
#print(make_slug("Midnight In Oslo")) # stage 4
#print(format_report_line({"title": "The Dune Chronicles", "year": 2021, 
#    "genres": {"sci-fi", "drama"}, "rating": 8.6, "duration_min": 155,
#    "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]})) # stage 4
print(titles_sorted_by_rating(movies)) # stage 5
print(top_n_by_rating(movies, 5)) # stage 5