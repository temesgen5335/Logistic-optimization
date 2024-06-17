import mysql.connector as mysql
import pandas as pd
from pathlib import Path
import os, logging

def DBConnect(dbName=None):
    """connect to SQL database"""
    conn = mysql.connect(host='localhost', user='root', password='password', database=dbName, buffered=True)
    cur = conn.cursor()
    return conn, cur

def createDB(dbName: str) -> None:
    """
    create database
    Parameter: database name : string
    """
    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()

def createTable(dbName, sqlFilePath) -> None:
    """
    create table
    Parameters: database name : string
                schema file path : string
    """
    conn, cur = DBConnect(dbName)
    sqlFile = sqlFilePath
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            cur.execute(command)
        except Exception as ex:
            logging.error("Command skipped: ", command)
            logging.error(ex)
    conn.commit()
    cur.close()
    return
