
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT
);

CREATE TABLE usersinfo (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users,
  users_name TEXT NOT NULL,
  gender TEXT NOT NULL,
  faculty TEXT NOT NULL,
  student_number TEXT NOT NULL,
  address_user TEXT NOT NULL
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);