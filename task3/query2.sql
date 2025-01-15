-- Napište SQL query, který vrátí počet filmů v jednotlivých filmových kategoriích
SELECT
    category.name AS "Category",
    COUNT(film_category.film_id) AS "Number of films"
FROM film_category
    JOIN film ON film_category.film_id = film.film_id
    JOIN category ON film_category.category_id = category.category_id
GROUP BY category.name;