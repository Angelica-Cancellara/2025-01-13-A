from database.DB_connect import DBConnect
from model.classification import Classification
from model.gene import Gene
from model.interaction import Interaction


class DAO():

    @staticmethod
    def get_all_genes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                        FROM genes"""
            cursor.execute(query)

            for row in cursor:
                result.append(Gene(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_interactions():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                           FROM interactions"""
            cursor.execute(query)

            for row in cursor:
                result.append(Interaction(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_classifications():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                        FROM classification"""
            cursor.execute(query)

            for row in cursor:
                result.append(Classification(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getLocalizzazione():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select Localization 
                from classification c
                group by Localization 
                order by Localization desc """
        cursor.execute(query)
        for row in cursor:
            result.append(row["Localization"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(localization):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select c.*
                from classification c 
                where Localization = %s"""
        cursor.execute(query, (localization,))
        for row in cursor:
            result.append(Classification(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(localization, idMap):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select c1.GeneID as c1, c2.GeneID as c2, sum(distinct g.Chromosome) as peso
                from classification c1, classification c2, interactions i, genes g
                where i.GeneID1 = c1.GeneID 
                and i.GeneID2 = c2.GeneID 
                and c1.GeneID != c2.GeneID 
                and c1.Localization = %s
                and c2.Localization = %s
                and (g.GeneID = c1.GeneID or g.GeneID = c2.GeneID)
                group by c1.GeneID, c2.GeneID"""
        cursor.execute(query, (localization, localization))
        for row in cursor:
            result.append((idMap[row["c1"]], idMap[row["c2"]], row["peso"]))
        cursor.close()
        conn.close()
        return result