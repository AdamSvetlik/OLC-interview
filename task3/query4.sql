-- Napište SQL query pro manažera, které vrátí kolik zápůjček udělali jednotliví zaměstnanci
-- v každém roce. Rozděleno na jednotlivé prodejny. Vymyslete, jak by mohla fungovat
-- aktualizace dat.
SELECT
    concat(
        address.address, ' ',
        address.address2, ' ',
        address.district, ' ',
        city.city, ' ',
        address.postal_code, ' ',
        country.country
    ) AS "Full address",
    concat(staff.first_name, ' ', staff.last_name) AS "Full name",
    extract(YEAR FROM rental.rental_date) AS "Year",
    count(*) AS "Rentals made"
FROM staff
    JOIN rental ON staff.staff_id = rental.staff_id
    JOIN store ON staff.store_id = store.store_id
    JOIN address ON store.address_id = address.address_id
    JOIN city ON address.city_id = city.city_id
    JOIN country ON city.country_id = country.country_id
GROUP BY
    extract(YEAR FROM rental.rental_date),
    staff.first_name,
    staff.last_name,
    address.address,
    address.address2,
    address.district,
    city.city,
    address.postal_code,
    country.country
ORDER BY "Full address", "Full name", "Year";
