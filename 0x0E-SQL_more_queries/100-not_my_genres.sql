-- List all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
    SELECT DISTINCT tv_shows_genres.genre_id
    FROM tv_shows_genres
    JOIN tv_shows ON tv_shows.id = tv_shows_genres.show_id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
