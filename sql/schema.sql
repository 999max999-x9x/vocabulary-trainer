CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);


CREATE TABLE collections (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    user_id INTEGER REFERENCES users(id)
);


CREATE TABLE words (
    id SERIAL PRIMARY KEY,
    original_word VARCHAR(100) NOT NULL,
    translation VARCHAR(100) NOT NULL,
    example TEXT,

    collection_id INTEGER REFERENCES collections(id)
);


CREATE TABLE progress (
    id SERIAL PRIMARY KEY,

    word_id INTEGER REFERENCES words(id),

    knowledge_level INTEGER DEFAULT 0,

    repeat_date DATE
);