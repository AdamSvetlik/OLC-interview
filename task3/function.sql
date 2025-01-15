-- Napište jednoduchou funkci/proceduru pro přidání nového filmu našeho zápůjčkového
-- systému.
CREATE OR REPLACE FUNCTION add_film(
    p_title CHARACTER VARYING(255),
    p_description TEXT,
    p_release_year YEAR,
    p_language_id INTEGER,
    p_original_language_id INTEGER,
    p_rental_duration SMALLINT,
    p_rental_rate NUMERIC(4,2),
    p_length SMALLINT,
    p_replacement_cost NUMERIC(5,2),
    p_rating MPAA_RATING,
    p_special_features TEXT[],
    p_fulltext TSVECTOR
) RETURNS VOID AS $$
BEGIN
    INSERT INTO film (film_id, title, description, release_year, language_id, original_language_id, rental_duration,
                      rental_rate, length, replacement_cost, rating, last_update, special_features, fulltext)
    VALUES (
        DEFAULT,
        p_title,
        p_description,
        p_release_year,
        p_language_id,
        p_original_language_id,
        p_rental_duration,
        p_rental_rate,
        p_length,
        p_replacement_cost,
        p_rating,
        DEFAULT, -- default value is now()
        p_special_features,
        p_fulltext
    );
END;
$$ LANGUAGE plpgsql;

SELECT add_film(
    'Inception'::CHARACTER VARYING,
    'A mind-bending thriller'::TEXT,
    2010::year,
    1::INTEGER,
    NULL::INTEGER,
    7::SMALLINT,
    2.99::NUMERIC(4,2),
    148::SMALLINT,
    19.99::NUMERIC(5,2),
    'PG-13'::mpaa_rating,
    ARRAY['Behind the Scenes', 'Deleted Scenes']::TEXT[],
    to_tsvector('testtest')
);
-- needed to specify the types of the parameters, otherwise it would not work
-- data types in the ERD differ from the ones in the scheme of film table

SELECT * FROM film ORDER BY film.film_id DESC

-- if there wasn't a default value for film_id, I would declare a variable and select into it the highest film_id + 1
