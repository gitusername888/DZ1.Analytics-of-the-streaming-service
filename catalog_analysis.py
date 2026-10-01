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

    result = f'"{normalize_title(movie.get("title"))}" ({movie.get("year")})' 
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

def count_by_genre(movies):
    """Напишите функцию count_by_genre(movies), возвращающую словарь {жанр: 
    количество фильмов}, построенный вручную через цикл и метод dict.get() 
    (без Counter)."""


    genre_counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts
        


def actor_filmography(movies):
    """Напишите функцию actor_filmography(movies), возвращающую словарь
      {актер: [список названий фильмов]}."""
    genre_counts = {}
    for movie in movies:
            for actor in movie["actors"]:
                films = genre_counts.get(actor)
                if films is None:
                    films = []
                    genre_counts[actor] = films

                films.append(movie["title"])
    return genre_counts

def high_rated_movies(movies):
    """С помощью генератора словаря (dict comprehension) постройте словарь 
    {title: rating} только для фильмов с рейтингом выше среднего (используйте
      average_rating из этапа 1)."""
    return { 
    movie["title"]: movie["rating"]
    for movie in movies
    if movie["rating"] > average_rating(movies)}

def all_genres(movies):
    """Напишите функцию all_genres(movies), возвращающую множество 
    всех уникальных жанров каталога."""
    genres_set = set()
    for movie in movies:
        # Добавляем все жанры из списка фильма в множество
        genres_set.update(movie.get("genres", []))
    return genres_set

def common_actors(movie1, movie2):
    """Напишите функцию common_actors(movie1, movie2), возвращающую множество 
    актеров, снимавшихся в обоих фильмах."""

    set1 = set(movie1.get("actors", []))
    set2 = set(movie2.get("actors", []))
    
    set3 = set(set2 & set1)
    
    return set3

def genres_only_in_one(movies_a, movies_b):
    """Напишите функцию genres_only_in_one(movies_a, movies_b), которая 
    возвращает жанры, встречающиеся в movies_a, но не встречающиеся 
    в movies_b."""

    """genres_a = set()
    genres_b = set()

     movie in movies_a:
        genres_a.update(movie.get("genres", []))

    for movie in movies_b:
        genres_b.update(movie.get("genres", []))"""
  
    # Разность множеств: жанры из A, которых нет в B
    return all_genres(movies_a) - all_genres(movies_b)

def iter_high_rated(movies, min_rating=8.0):
    """Напишите функцию-генератор iter_high_rated(movies, min_rating=8.0),
      которая через yield лениво отдает фильмы с 
      рейтингом не ниже min_rating."""

    for movie in movies:
        if movie.get("rating", 0) >= min_rating:
            yield movie

def build_report(movies):
    """Напишите функцию build_report(movies), которая объединяет результаты
    всех предыдущих этапов в единый консольный отчет: общую статистику, 
    топ-3 фильма, количество фильмов по каждому жанру и полный список
    уникальных жанров каталога.
    ОТЧеТ ПО КАТАЛОГУ
    Средний рейтинг: 7.2
    Средний возраст фильмов: 8 лет

    Топ-3 фильма:
    "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi
    "Midnight In Oslo" (2020) — 8.9/10, 2ч 4м, жанры: mystery, thriller
    "The Dune Chronicles" (2021) — 8.6/10, 2ч 35м, жанры: drama, sci-fi

    Фильмов по жанрам:
    drama — 5
    comedy — 3
    sci-fi — 3
    thriller — 3
    action — 2
    mystery — 1

    Все жанры каталога: action, comedy, drama, mystery, sci-fi, thriller 

    """
    # сортировка жанров
    all_genres_sorted = sorted(all_genres(movies))
    # Количество фильмов по жанрам, отсортировано по убыванию
    genre_counts = count_by_genre(movies)
    genre_lines = '\n'.join(
        f'  {genre} — {count}'
        for genre, count in sorted(genre_counts.items(), key=lambda x: -x[1])
    )
    #Топ-3 фильма:
    top3 = sorted(movies, key=lambda x: x['rating'], reverse=True)[:3]
    top3_lines = '\n'.join(f'  {format_report_line(m)}' for m in top3)
    return (f"ОТЧеТ ПО КАТАЛОГУ\nСредний рейтинг: {average_rating(movies)}\n"
        f"Средний возраст фильмов: "
        f"{catalog_age_stats(movies, current_year=2026)[-1]} лет \n \n"
        f"Топ-3 фильма: \n{top3_lines}\n"
        f"Фильмов по жанрам:\n{genre_lines}\n"
        f"Все жанры каталога: {', '.join(map(str,all_genres_sorted))}")





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
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    
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
#print(titles_sorted_by_rating(movies)) # stage 5
#print(top_n_by_rating(movies, 5)) # stage 5
#rint(count_by_genre(movies)) # stage 6
#rint(actor_filmography(movies)) # stage 6
#rint(high_rated_movies(movies)) # stage 6
#rint(average_rating(movies))# stage 6
#print(all_genres(movies))# stage 7
#print(common_actors(movies[0], movies[3])) # stage 7
#print(genres_only_in_one(movies[5:6], movies[:5])) # stage 7
"""Напишите функцию-генератор iter_high_rated(movies, min_rating=8.0),
 которая через yield лениво отдает фильмы с рейтингом не ниже min_rating.
Продемонстрируйте ее работу циклом for с вызовом format_report_line."""
"""for high_rated_movie in iter_high_rated(movies, min_rating=8.0):
    print(format_report_line(high_rated_movie)) # stage 8"""


"""Напишите генераторное выражение, которое считает суммарную 
длительность всех фильмов с рейтингом выше 7 в минутах, и 
передайте его в sum()."""
"""print(sum(movie["duration_min"] for movie 
          in movies if movie["rating"] > 7)) #stage 8"""


print (build_report(movies))