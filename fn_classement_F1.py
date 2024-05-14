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

def fn_question_train_code(question, erreur):
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

def fn_input_team_code():
    q_team_nom = "Encoder le nom de la team"
    e_team_nom = "Erreur le nom de la team n'est pas valide"
    team_nom = fn_question_alpha(q_team_nom, e_team_nom)
    q_directeur_nom = "Encoder le nom du directeur"
    e_directeur_nom = "Erreur le nom du directeur n'est pas valide"
    directeur_nom = fn_question_alpha(q_directeur_nom, e_directeur_nom)
    q_position_classement_constructeur = "Entrer le position au classement constructeur de la team"
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
                print(f"Commande SQL exécutée : INSERT INTO TEAM (nom) VALUES ('{team_data[0]}');")
                cursor.execute(f"INSERT INTO TEAM (nom) VALUES ('{team_data[0]}');")
                print(f"Commande SQL exécutée : INSERT INTO TEAM (directeur) VALUES ('{team_data[0]}');")
                cursor.execute(f"INSERT INTO TEAM (directeur) VALUES ('{team_data[0]}');")
                print(f"Commande SQL exécutée : INSERT INTO TEAM (position_classement_constructeur) VALUES ('{team_data[0]}');")
                cursor.execute(f"INSERT INTO TEAM (position_classement_constructeur) VALUES ('{team_data[0]}');")
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

def fn_init_set_team_code_menu():
    q_choix_1 = "[1] Ajouter une team"
    q_choix_2 = "[2] Quitter"
    list_menu = [q_choix_1, q_choix_2]
    return list_menu


def fn_set_team_code_menu(list_menu):
    print(f'\n----Menu - Projet Classement F1----')
    for item in list_menu:
        print(f'{item}')
    q_status = "Entrer votre choix (1-2) : "
    e_status = "\nErreur : Caractères invalides\n"
    status = int(fn_question_int(q_status, e_status))
    match status:
        case 1:
            team_data = fn_input_team_code()
            db_name = fn_get_db_name()
            fn_set_train_code(db_name, team_data)
            return True
        case 2:
            print(f'Fermeture de l\'application')
            return False
        case _:
            print(f'\nErreur : Choix non-valide\n')
            return True
    
def fn_create_db():
    try:
        list_menu = fn_init_set_team_code_menu()
        create_db_out = fn_set_team_code_menu(list_menu)            
    except Exception as error:
        print(f"{error}")
    finally:
        return create_db_out

def fn_read_db(db_name):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()                                
            try:
                cursor.execute(f"SELECT * FROM TRAIN;")
                data = cursor.fetchall()
                print("SQLite script executed successfully")
                print(f'\nExecution du SELECT :')
                for line in data:
                    print(line)
                print()
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

def fn_question_id(question, erreur):
    train_id = input(question)
    while not train_id.isnumeric():
        print(erreur)
        train_id = input(question)
    return train_id

def fn_update_train_code(train_code, train_id, db_name):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                print(f"UPDATE TRAIN SET Code='{train_code}' WHERE train_id='{train_id}';")
                cursor.execute(f"UPDATE TRAIN SET Code='{train_code}' WHERE train_id='{train_id}';")
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
    
def fn_init_update_train_code_menu():
    q_choix_1 = "[1] Modifier un train"
    q_choix_2 = "[2] Quitter"
    list_menu = [q_choix_1, q_choix_2]
    return list_menu

def fn_update_train_code_menu(list_menu):
    print(f'\n----Menu - Projet Classement F1----')
    for item in list_menu:
        print(f'{item}')
    q_status = "Entrer votre choix (1-2) : "
    e_status = "\nErreur : Caractères invalides\n"
    status = int(fn_question_int(q_status, e_status))
    match status:
        case 1:
            db_name = fn_get_db_name()
            fn_read_db(db_name)
            q_id_status = "Entrer votre choix : "
            e_id_status = "\nErreur : Caractères invalides\n"
            train_id = fn_question_id(q_id_status, e_id_status)
            train_code = fn_input_team_code()
            fn_update_train_code(train_code, train_id, db_name)
            return True
        case 2:
            print(f'Fermeture de l\'application')
            return False
        case _:
            print(f'\nErreur : Choix non-valide\n')
            return True
        
def fn_update_db():
    try:
        list_menu = fn_init_update_train_code_menu()
        update_db_out = fn_update_train_code_menu(list_menu)            
    except Exception as error:
        print(f"{error}")
    finally:
        return update_db_out

def fn_delete_train_code (db_name, train_id):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                print(f"DELETE FROM TRAIN WHERE train_id = {train_id};")
                cursor.execute(f"DELETE FROM TRAIN WHERE train_id = {train_id};")
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

def fn_init_delete_train_code_menu():
    q_choix_1 = "[1] Supprimer un train"
    q_choix_2 = "[2] Quitter"
    list_menu = [q_choix_1, q_choix_2]
    return list_menu

def fn_delete_train_code_menu(list_menu):
    print(f'\n----Supprimer - Projet Classement F1----')
    for item in list_menu:
        print(f'{item}')
    q_status = "Entrer votre choix : "
    e_status = "\nErreur : Caractères invalides\n"
    status = int(fn_question_int(q_status, e_status))
    match status:
        case 1:
            db_name = fn_get_db_name()
            fn_read_db(db_name)
            q_id_status = "Entrer votre choix : "
            e_id_status = "\nErreur : Caractères invalides\n"
            train_id = fn_question_id(q_id_status, e_id_status)
            fn_delete_train_code(db_name, train_id)
            return True
        case 2:
            print(f'Fermeture de l\'application')
            return False
        case _:
            print(f'\nErreur : Choix non-valide\n')
            return True

def fn_delete_db():
    try:
        list_menu = fn_init_delete_train_code_menu()
        delete_db_out = fn_delete_train_code_menu(list_menu)            
    except Exception as error:
        print(f"{error}")
    finally:
        return delete_db_out