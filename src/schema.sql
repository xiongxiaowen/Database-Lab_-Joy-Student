CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT
);

CREATE TABLE usersinfo (
  id SERIAL PRIMARY KEY,
  user_id INTEGER UNIQUE REFERENCES users(id),
  users_name TEXT NOT NULL,
  degree_program TEXT,
  faculty TEXT,
  address TEXT
);

CREATE TABLE friends (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES usersinfo(user_id),
    friend_id INTEGER REFERENCES usersinfo(user_id)
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users(id),
    sent_at TIMESTAMP
);

CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    post_id INTEGER REFERENCES messages(id)
);
