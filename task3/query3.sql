-- Napište SQL query pro výpočet pokuty. Pokuta se počítá za každý den po termínu vrácení a to
-- částkou 1 % z ceny. Počítejme, že filmy se půjčují na 14 dní
SELECT
    concat(c.first_name, ' ', c.last_name) AS "Full name",
    c.email AS "E-mail",
    (extract(DAY FROM (coalesce(r.return_date, now()) - r.rental_date)) - f.rental_duration) * f.rental_rate AS "Fine"
FROM rental r
    LEFT JOIN inventory i ON r.inventory_id = i.inventory_id
    LEFT JOIN film f ON i.film_id = f.film_id
    LEFT JOIN customer c ON r.customer_id = c.customer_id
WHERE extract(DAY FROM (coalesce(r.return_date, now()) - r.rental_date)) - f.rental_duration > 0;
-- found that there are fields in film table with rental duration and rental rate, so I decided to use them instead