CREATE TABLE IF NOT EXISTS driver
(
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    numero_pilote VARCHAR,
    voiture_utiliser VARCHAR,
    position_classement_pilote INTEGER,
    podium INTEGER,
    fastest_lap DATETIME,
    victoire INTEGER,
    championnat_gagner INTEGER,
    nationalite VARCHAR,
    date_de_naissance VARCHAR,
    team_id INT,
    FOREIGN KEY (team_id) REFERENCES team(id)
);

CREATE TABLE IF NOT EXISTS team
(
    team_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nom VARCHAR,
    directeur VARCHAR,
    position_classement_constructeur INTEGER
);

CREATE TABLE IF NOT EXISTS car
(
    car_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    team_id INT,
    FOREIGN KEY (team_id) REFERENCES team(id)
);

CREATE TABLE IF NOT EXISTS present
(
    present_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    driver_id INT,
    race_id INT, 
    FOREIGN KEY (driver_id) REFERENCES driver(id),
    FOREIGN KEY (race_id) REFERENCES race(id)
);

CREATE TABLE IF NOT EXISTS race
(
    race_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nombre_de_course VARCHAR,
    date_des_courses VARCHAR,
    classement_course VARCHAR,
    meilleur_tour DATETIME
);