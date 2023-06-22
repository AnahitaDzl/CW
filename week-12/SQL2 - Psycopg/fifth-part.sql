SELECT film.title, category.name, language.name as language_of_film
FROM film JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
join language
on language.language_id = film.language_id