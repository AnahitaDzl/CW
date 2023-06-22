SELECT category.name, COUNT(film.film_id) AS "Total Films"
FROM film JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
GROUP BY category.name