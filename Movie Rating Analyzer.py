from functools import reduce

ratings = [4.5, 3.2, 4.8, 2.9, 4.1]

top_movies = list(filter(lambda x: x >= 4, ratings))

percentage = list(map(lambda x: x * 20, top_movies))

total = reduce(lambda x, y: x + y, percentage)

print("Top Movies:", top_movies)
print("Rating Percentage:", percentage)
print("Total Score:", total)
