-- Napište SQL query, které vrátí informace o všech, co si pučili film v posledním roce. Zajímá nás
-- jeho jméno a kompletní adresa.
SELECT DISTINCT
    concat(customer.first_name, ' ', customer.last_name) AS "Full name",
    concat(
            address.address, ' ',
            address.address2, ' ',
            address.district, ' ',
            city.city, ' ',
            address.postal_code, ' ',
            country.country
    ) AS "Full address",
    customer.first_name AS "First name",
    customer.last_name AS "Last name",
    address.address AS "Address",
    address.address2 AS "Address 2",
    address.district AS "District",
    city.city AS "City",
    country.country AS "Country",
    address.postal_code AS "Postal code"
FROM rental
    JOIN customer ON rental.customer_id = customer.customer_id
    JOIN address ON customer.address_id = address.address_id
    JOIN city ON address.city_id = city.city_id
    JOIN country ON city.country_id = country.country_id
WHERE '2006-01-01' - rental_date <= INTERVAL '1 year';
-- year 2006 is used due to old data, now() would be used on recent data