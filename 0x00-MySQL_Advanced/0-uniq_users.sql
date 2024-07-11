-- creates table users with:
-- id, email and name

CREATE TABLE IF NOT EXIST users(
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY (id)
	);
