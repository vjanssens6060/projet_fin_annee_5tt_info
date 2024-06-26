import sqlite3
import os
import re

def fn_question_alpha(question, erreur):
    reponse = input(question)
    while not reponse.isalpha():
        print(erreur)
        reponse = input(question)
    return reponse

def fn_question_int(question, erreur):
    reponse = input(question)
    while not reponse.isnumeric():
        print(erreur)
        reponse = input(question)
    return reponse

def fn_read_db(db_name, table_name):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()  
                                  
            try:
                if table_name == 'team':        
                    cursor.execute(f"SELECT * FROM TEAM;")
                    data = cursor.fetchall()
                    print("SQLite script executed successfully")
                    print(f'\nExecution du SELECT :')
                    for line in data:
                        print(line)
                    return data
                elif table_name == 'car':
                    cursor.execute(f"SELECT * FROM CAR;")
                    data = cursor.fetchall()
                    print("SQLite script executed successfully")
                    print(f'\nExecution du SELECT :')
                    for line in data:
                        print(line)
                    return data
                elif table_name == 'driver':
                    cursor.execute(f"SELECT * FROM DRIVER;")
                    data = cursor.fetchall()
                    print("SQLite script executed successfully")
                    print(f'\nExecution du SELECT :')
                    for line in data:
                        print(line)
                    return data

            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def fn_check_foreign_key(list_foreign_key):
    # vérifier que la foreign key encodée par l'utilisateur est dans la liste crée
    reponse = int(input(question))
    while not reponse in list_foreign_key:
        print(erreur)
        reponse = int(input(question))
    return reponse

def fn_question_id_team(question, erreur):
    db_name = fn_get_db_name()
    data = fn_read_db(db_name, 'team')
    # requete SQL qui SELECT les valeurs de la colonne id_name dans table_name et les stocks dans une liste
    list_id_name = []
    for team in data: 
        print(team)
        print(team[0])
        list_id_name.append(team[0])
    # vérifier que la foreign key encodée par l'utilisateur est dans la liste crée ci-dessus
    # si oui, on return la reponse
    # si non, on repose la question et on effectue le processus à nouveau
    print(list_id_name)
    
    print(type(list_id_name[0]))
    fn_check_foreign_key(list_id_name)


     
    
    #while fn_check_foreign_key(list_id_name, reponse):
    #    print(erreur)
    #    reponse = input(question)
    #return reponse

def fn_question_train(question, erreur):
    reponse = input(question).upper()
    pattern = re.compile(r'^[A-Z]{2}\d{4}$')
    while not bool(pattern.match(reponse)):
        print(erreur)
        reponse = input(question).upper()
    return reponse

def fn_get_db_name():
    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)
    # print(f'Chemin du dossier script : {work_dir}')
    # print(f'Chemin de la db : {work_dir}/data.db')
    db_name = f'{work_dir}/data.db'
    return db_name

def fn_get_sql_script():
    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)
    sql_init_script = f'{work_dir}/sql_script/init_classement_F1.sql'
    return sql_init_script

def fn_init_db(db_name, sql_init_script):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                with open(sql_init_script, "r") as sqlite_file:
                    try:
                        sql_script = sqlite_file.read()
                    except Exception as error:
                        print(f"Error while reading the SQL script: {error}")
                        return
            except Exception as error:
                print(f"Error while opening the SQL file: {error}")
                return                
            try:
                cursor.executescript(sql_script)
                print("SQLite script executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def fn_input_team():
    q_team_nom = "Encoder le nom de la team : "
    e_team_nom = "Erreur le nom de la team n'est pas valide"
    team_nom = fn_question_alpha(q_team_nom, e_team_nom)
    q_directeur_nom = "Encoder le nom du directeur : "
    e_directeur_nom = "Erreur le nom du directeur n'est pas valide"
    directeur_nom = fn_question_alpha(q_directeur_nom, e_directeur_nom)
    q_position_classement_constructeur = "Entrer le position au classement constructeur de la team : "
    e_position_classement_constructeur = "Erreur la position au classement constructeur n'est pas valide"
    position_classement_constructeur = fn_question_int(q_position_classement_constructeur, e_position_classement_constructeur)
    team_list = [team_nom, directeur_nom, position_classement_constructeur]
    return team_list
    
def fn_set_team_data(db_name, team_data):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()                                
            try:
                print(f"Commande SQL exécutée : INSERT INTO TEAM (nom, directeur, position_classement_constructeur ) VALUES ('{team_data[0]}', '{team_data[1]}', '{team_data[2]}');")
                cursor.execute(f"INSERT INTO TEAM (nom, directeur, position_classement_constructeur ) VALUES ('{team_data[0]}', '{team_data[1]}', '{team_data[2]}');")
                print("SQLite command executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def fn_init_set_team_menu():
    q_choix_1 = "[1] Ajouter une team"
    q_choix_2 = "[2] Encoder une voiture"
    q_choix_3 = "[3] Encoder un pilote"
    q_choix_4 = "[4] Quitter"
    list_menu = [q_choix_1, q_choix_2,q_choix_3, q_choix_4]
    return list_menu


def fn_set_team_menu(list_menu):
    print(f'\n----Menu - Projet Classement F1----')
    for item in list_menu:
        print(f'{item}')
    q_status = "Entrer votre choix (1-4) : "
    e_status = "\nErreur : Caractères invalides\n"
    status = int(fn_question_int(q_status, e_status))
    match status:
        case 1:
            team_data = fn_input_team()
            db_name = fn_get_db_name()
            fn_set_team_data(db_name, team_data)
            return True
        case 2:
            car_data = fn_input_car()
            db_name = fn_get_db_name()
            fn_set_car_data(db_name, car_data)
        case 3 : 
            driver_data = fn_input_driver()
            db_name = fn_get_db_name()
            fn_set_driver_data(db_name, driver_data)
        case 4:
            print(f'Fermeture de l\'application')
            return False
        case _:
            print(f'\nErreur : Choix non-valide\n')
            return True

def fn_init_set_table_menu():
    q_choix_1 = "[1] Afficher une team"
    q_choix_2 = "[2] Afficher une voiture"
    q_choix_3 = "[3] Afficher un pilote"
    q_choix_4 = "[4] Quitter"
    list_menu = [q_choix_1, q_choix_2,q_choix_3, q_choix_4]
    return list_menu


def fn_set_table_menu(list_menu):
    print(f'\n----Menu - Afficher les Tables ----')
    for item in list_menu:
        print(f'{item}')
    q_status = "Entrer votre choix (1-4) : "
    e_status = "\nErreur : Caractères invalides\n"
    status = int(fn_question_int(q_status, e_status))
    match status:
        case 1:
            return 'team'
        case 2:
            return 'car'
        case 3 : 
            return 'driver'
        case 4:
            print(f'Fermeture de l\'application')
            return False
        case _:
            print(f'\nErreur : Choix non-valide\n')
            return True
    
def fn_create_db():
    try:
        list_menu = fn_init_set_team_menu()
        create_db_out = fn_set_team_menu(list_menu)            
    except Exception as error:
        print(f"{error}")
    finally:
        return create_db_out



def fn_question_id(question, erreur):
    train_id = input(question)
    while not train_id.isnumeric():
        print(erreur)
        train_id = input(question)
    return train_id

def fn_update_team(team_data, team_id, db_name):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                print(f"UPDATE TEAM SET nom='{team_data[0]}', directeur='{team_data[1]}', position_classement_constructeur='{team_data[2]}' WHERE team_id='{team_id}';")
                cursor.execute(f"UPDATE TEAM SET nom='{team_data[0]}', directeur='{team_data[1]}', position_classement_constructeur='{team_data[2]}' WHERE team_id='{team_id}';")
                print("SQLite command executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def fn_update_car(car_data, db_name):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                print(f"UPDATE CAR SET nom_voiture='{car_data[0]}', numero_voiture='{car_data[1]}' WHERE car_id='{car_id}';")
                cursor.execute(f"UPDATE CAR SET nom_voiture='{car_data[0]}', numero_voiture='{car_data[1]}' WHERE car_id='{car_id}';")
                print("SQLite command executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    
def fn_init_update_team_menu():
    q_choix_1 = "[1] Modifier une team"
    q_choix_2 = "[2] Modifier une voiture" 
    q_choix_3 = "[3] Quitter"
    list_menu = [q_choix_1, q_choix_2, q_choix_3]
    return list_menu

def fn_update_team_menu(list_menu):
    print(f'\n----Menu - Projet Classement F1----')
    for item in list_menu:
        print(f'{item}')
    q_status = "Entrer votre choix (1-3) : "
    e_status = "\nErreur : Caractères invalides\n"
    status = int(fn_question_int(q_status, e_status))
    match status:
        case 1:
            db_name = fn_get_db_name()
            fn_read_db(db_name, 'team')
            q_id_status = "Entrer votre choix : "
            e_id_status = "\nErreur : Caractères invalides\n"
            train_id = fn_question_id(q_id_status, e_id_status)
            train_code = fn_input_team()
            fn_update_team(train_code, train_id, db_name)
            return True
        case 2: 
            db_name = fn_get_db_name()
            fn_read_db(db_name, 'car')
            q_id_status = "Entrer votre choix : "
            e_id_status = "\nErreur : Caractères invalides\n"
            train_id = fn_question_id(q_id_status, e_id_status)
            train_code = fn_input_car()
            fn_update_car(train_code, train_id, db_name)
        case 3:
            print(f'Fermeture de l\'application')
            return False
        case _:
            print(f'\nErreur : Choix non-valide\n')
            return True
        
def fn_update_db():
    try:
        list_menu = fn_init_update_team_menu()
        update_db_out = fn_update_team_menu(list_menu)            
    except Exception as error:
        print(f"{error}")
    finally:
        return update_db_out

def fn_delete_team (db_name, table_name, id):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                if table_name == 'team':
                    print(f"DELETE FROM TEAM WHERE team_id = {id};")
                    cursor.execute(f"DELETE FROM TEAM WHERE team_id = {id};")
                    print("SQLite command executed successfully")
                elif table_name == 'car':
                    print(f"DELETE FROM CAR WHERE car_id = {id};")
                    cursor.execute(f"DELETE FROM CAR WHERE car_id = {id};")
                    print("SQLite command executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite command: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def fn_delete_car (db_name, car_id):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                print(f"DELETE FROM CAR WHERE car_id = {car_id};")
                cursor.execute(f"DELETE FROM CAR WHERE car_id = {car_id};")
                print("SQLite command executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite command: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def fn_init_delete_team_menu():
    q_choix_1 = "[1] Supprimer une team"
    q_choix_2 = "[2] Supprimer une voiture"
    q_choix_3 = "[3] Quitter"
    list_menu = [q_choix_1, q_choix_2, q_choix_3]
    return list_menu

def fn_delete_team_menu(list_menu):
    print(f'\n----Supprimer - Projet Classement F1----')
    for item in list_menu:
        print(f'{item}')
    q_status = "Entrer votre choix : "
    e_status = "\nErreur : Caractères invalides\n"
    status = int(fn_question_int(q_status, e_status))
    match status:
        case 1:
            table_name = 'team'
            db_name = fn_get_db_name()
            fn_read_db(db_name, table_name)
            q_id_status = "Entrer votre choix : "
            e_id_status = "\nErreur : Caractères invalides\n"
            team_id = fn_question_id(q_id_status, e_id_status)
            fn_delete_team(db_name, table_name, team_id)
            return True
        case 2: 
            table_name = 'car'
            db_name = fn_get_db_name()
            fn_read_db(db_name, table_name)
            q_id_status = "Entrer votre choix : "
            e_id_status = "\nErreur : Caractères invalides\n"
            car_id = fn_question_id(q_id_status, e_id_status)
            fn_delete_car(db_name,table_name, car_id)
            return True
        case 3:
            print(f'Fermeture de l\'application')
            return False
        case _:
            print(f'\nErreur : Choix non-valide\n')
            return True

def fn_delete_db():
    try:
        list_menu = fn_init_delete_team_menu()
        delete_db_out = fn_delete_team_menu(list_menu)            
    except Exception as error:
        print(f"{error}")
        delete_db_out = False
    finally:
        return delete_db_out

def fn_set_car_data(db_name, car_data):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()                                
            try:
                print(f"Commande SQL exécutée : INSERT INTO CAR (nom_voiture, numero_voiture) VALUES ('{car_data[0]}', '{car_data[1]}');")
                cursor.execute(f"INSERT INTO CAR (nom_voiture, numero_voiture, team_id) VALUES ('{car_data[0]}', '{car_data[1]}','{car_data[2]}');")
                print("SQLite command executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def fn_input_car():
    q_nom_voiture = "Encoder le nom de la voiture"
    nom_voiture = input(q_nom_voiture)
    q_numero_voiture = "Encoder le numéro de la voiture : "
    e_numero_voiture = "Erreur le numéro de la voiture n'est pas valide "
    numero_voiture = fn_question_alpha(q_numero_voiture, e_numero_voiture)
    q_id_voiture = "Encoder l'id de la team associée : "
    e_id_voiture = "Erreur l'id de la team associée n'est pas valide"
    id_voiture = fn_question_id_team(q_id_voiture, e_id_voiture)
    car_list = [numero_voiture, nom_voiture, id_voiture]
    return car_list

def fn_set_driver_data(db_name, driver_data):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()                                
            try:
                print(f"Commande SQL exécutée : INSERT INTO DRIVER (numero, position_classement_pilote, podium, fastest_lap, victoire, championnat_gagner, nationalite, date_de_naissance) VALUES ('{driver_data[0]}', '{driver_data[1]}', '{driver_data[2]}', '{driver_data[2]}', '{driver_data[3]}', '{driver_data[4]}', '{driver_data[5]}', '{driver_data[6]}', '{driver_data[7]}');")
                cursor.execute(f"INSERT INTO DRIVER (numero, position_classement_pilote, podium, fastest_lap, victoire, championnat_gagner, nationalite, date_de_naissance, team_id) VALUES ('{driver_data[0]}', '{driver_data[1]}', '{driver_data[2]}', '{driver_data[2]}', '{driver_data[3]}', '{driver_data[4]}', '{driver_data[5]}', '{driver_data[6]}', '{driver_data[7]}', '{driver_data[8]}');")
                print("SQLite command executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def fn_input_driver():
    q_numero = "Encoder numéro pilote : "
    e_numero = 'Erreur le numéro pilote est mauvais'
    numero = int(input(q_numero))
    q_position_classement_pilote = "Encoder la position au classement pilote : "
    e_position_classement_pilote = "Erreur la position est mauvaise"
    position_classement_pilote = int(intput(q_position_classement_pilote))
    q_podium = "Encoder le nombre de podium du pilote : "
    e_podium = "Erreur le nombre de podium est mauvais"
    podium = int(input(q_podium))
    q_fastest_lap = "Encoder le meilleur tour en course : "
    e_fastest_lap = "Erreur le temps n'est pas valide"
    fastest_lap = input(q_fastest_lap)
    q_victoire = "Encoder le nombre de victoire du pilote : "
    e_victoire = "Erreur le nombre de victoire n'est pas valide"
    victoire = int(input(q_victoire))
    q_championnat_gagner = "Encoder le nombre de championnat gagner du pilote : "
    e_championnat_gagner = "Erreur le nombre de championnat gagner n'est pas valide"
    championnat_gagner = int(intput(q_championnat_gagner))
    q_nationalite = "Entrer la nationalite du pilote : "
    e_nationalite = "Erreur dans la nationalité du pilote"
    nationalite = fn_question_alpha(q_nationalite, e_nationalite)
    q_date_de_naissance = "Entrer la date de naissance du pilote : "
    e_date_de_naissance = "Erreur la date de naissance du pilote n'est pas valide"
    date_de_naissance = intput(q_date_de_naissance)
    id_voiture = fn_question_id_team(q_id_voiture, e_id_voiture)
    car_list = [numero, position_classement_pilote, podium, fastest_lap, victoire, championnat_gagner, nationalite, date_de_naissance]
    return car_list


def fn_dict_team(db_name):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()                                
            try:
                cursor.execute(f"SELECT * FROM TEAM;")
                data = cursor.fetchall()
                print("SQLite script executed successfully")
                print(f'\nExecution du SELECT :')
                for line in data:
                    print(line)
                print()
                # Transformation des donnÃ©es d'une table SQL contenant (title, date, description_e) rÃ©cupÃ©rÃ©e Ã  l'aide de (SELECT * FROM TEAM;) en liste de dictionnaire
                # RÃ©cupÃ©rez les noms des colonnes
                column_names = [description[0] for description in cursor.description]
                # Transformez les donnÃ©es en une liste de dictionnaires
                team_list = []
                for line in data:
                    event = dict(zip(column_names, line))
                    team_list.append(event)
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            return team_list
        
def fn_dict_team_one_row(db_name, id):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()                                
            try:
                cursor.execute(f"SELECT * FROM team WHERE team_id={id};")
                data = cursor.fetchone()
                print("SQLite script executed successfully")
                print(f'\nExecution du SELECT :')
                column_names = [description[0] for description in cursor.description]
                # Transformez les donnÃ©es en une liste de dictionnaires
                dict_team = dict(zip(column_names, data))
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            return dict_team