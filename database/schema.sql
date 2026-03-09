CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    height INTEGER,
    mass NUMERIC,
    birth_year TEXT,
    gender TEXT,
    url TEXT UNIQUE,
    films_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE starships (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    model TEXT,
    max_atmosphering_speed NUMERIC,
    hyperdrive_rating NUMERIC,
    url TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE planets (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    climate TEXT,
    terrain TEXT,
    surface_water NUMERIC,
    population BIGINT,
    url TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    episode_id INTEGER,
    release_date DATE,
    url TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);