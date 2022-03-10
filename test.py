# Import module - !! = nécessite une installe via PIP
import sqlite3
import pyodbc   # !!

# Variable SQLite
#sqlite_path = "E:\http\lan\immosyn\edit-aech\application\database\mydb.db"


# Variable SQLServer
sqlsrv_server = "IMMO-SQLP1.esh.lan\MSSQL_COMMUN"
sqlsrv_db = "DWH"
sqlsrv_user = "appli_web"
sqlsrv_pass = "cinema"

# Fonction get_demandes : Récupérer les demandes à traiter dans la base sqlite
def test_sqlite():
    res = []
    try:
        sqlite_path = "C:\\outils-php\\serveur-web\\http\\edit-aech\\application\\database\\mydb.db"
        conn = sqlite3.connect(sqlite_path)
        cur = conn.cursor()
        sql = "select id, code_groupe_immo, types_doc, email, mois, annee from demandes where nom_fichier is null and actif = 0;"
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        conn.close()
    except sqlite3.Error as error:
        print("Erreur lors de la connexion à SQLite", error)
    print(res)

# Fonction get_comptes_affaire : Récupère les comptes affaire présent à une période donnée
def test_sqlsrv():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+sqlsrv_server+';DATABASE='+sqlsrv_db+';UID='+sqlsrv_user+';PWD='+ sqlsrv_pass)
    cursor = conn.cursor()
    requete = "SELECT * FROM DWH..GROUPE_IMMOBILIER where CODE_GROUPE_IMMO_COMP=?"
    cursor.execute(requete, ('V90 6896'))
    res = cursor.fetchall()

    print(res)

# Main
if __name__ == '__main__':  

    #test_sqlite()
    test_sqlsrv()