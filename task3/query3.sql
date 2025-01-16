-- Napište SQL query pro výpočet pokuty. Pokuta se počítá za každý den po termínu vrácení a to
-- částkou 1 % z ceny. Počítejme, že filmy se půjčují na 14 dní
SELECT
    concat(c.first_name, ' ', c.last_name) AS "Full name",
    c.email AS "E-mail",
    extract(DAY FROM (coalesce(r.return_date, now()) - r.rental_date)) - f.rental_duration AS "Days overdue",
    (extract(DAY FROM (coalesce(r.return_date, now()) - r.rental_date)) - f.rental_duration) * f.rental_rate * 0.01 AS "Fine"
FROM rental r
    LEFT JOIN inventory i ON r.inventory_id = i.inventory_id
    LEFT JOIN film f ON i.film_id = f.film_id
    LEFT JOIN customer c ON r.customer_id = c.customer_id
WHERE extract(DAY FROM (coalesce(r.return_date, now()) - r.rental_date)) - f.rental_duration > 0;
-- found that there are fields in film table with rental duration and rental rate, so I decided to use them instead


-- could be done with a subquery instead of redundant calculations
SELECT
    concat(c.first_name, ' ', c.last_name) AS "Full name",
    c.email AS "E-mail",
    overdue_info.days_overdue AS "Days overdue",
    overdue_info.days_overdue * f.rental_rate * 0.01 AS "Fine"
FROM rental r
    LEFT JOIN inventory i ON r.inventory_id = i.inventory_id
    LEFT JOIN film f ON i.film_id = f.film_id
    LEFT JOIN customer c ON r.customer_id = c.customer_id
    JOIN (
        SELECT
            r.rental_id,
            extract(DAY FROM (coalesce(r.return_date, now()) - r.rental_date)) - f.rental_duration AS days_overdue
        FROM rental r
        LEFT JOIN inventory i ON r.inventory_id = i.inventory_id
        LEFT JOIN film f ON i.film_id = f.film_id
    ) overdue_info ON r.rental_id = overdue_info.rental_id
WHERE overdue_info.days_overdue > 0;
