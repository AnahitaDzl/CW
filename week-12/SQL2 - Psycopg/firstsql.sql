select film.title,film.release_year,film_category.category_id
from film inner join film_category
on film.film_id = film_category.film_id 