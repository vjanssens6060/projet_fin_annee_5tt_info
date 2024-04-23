CREATE TABLE IF NOT EXISTS driver
(
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    numero_pilote VARCHAR
    voiture_utiliser VARCHAR
    position_classement_pilote INTEGER
    podium INTEGER
    fastest_lap DATETIME
    victoire INTEGER
    championnat_gagner INTEGER
    nationalite TEXT
    date_de_naissance VARCHAR,
);

CREATE TABLE IF NOT EXISTS team
(
    team_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    voiture VARCHAR
    directeur TEXT
    position_classement_constructeur INTEGER,
    FOREIGN KEY (team_id) REFERENCES driver(driver_id)
);

CREATE TABLE IF NOT EXISTS car
(
    car_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    FOREIGN KEY (team_id) REFERENCES team(team_id)
);

CREATE TABLE IF NOT EXISTS present
(
    present_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    FOREIGN KEY (present_id) REFERENCES driver(driver_id)
    FOREIGN KEY (present_id) REFERENCES race(race_id)
);

CREATE TABLE IF NOT EXISTS race
(
    race_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nombre_de_course VARCHAR
    date_des_courses VARCHAR
    classement_course VARCHAR
    meilleur_tour DATETIME
);