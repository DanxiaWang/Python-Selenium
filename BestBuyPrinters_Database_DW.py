'''
Created on Dec 10, 2021

@author: Danxia Wang
'''
import sqlite3

conn = sqlite3.connect('BestBuyPrinters.db')
cursor = conn.cursor()
#Dropping ProductDetails table if already exists.
cursor.execute('''DROP TABLE IF EXISTS ProductDetails''')
cursor.execute('''CREATE TABLE ProductDetails (\
                SKU INT NOT NULL PRIMARY KEY,\
                MobilePrinting varchar (500),\
                Networking varchar (500),\
                PrinterType vaarchar(100));''')
#Dropping ProductInfo table if already exists.
cursor.execute('''DROP TABLE IF EXISTS ProductInfo''')
cursor.execute('''CREATE TABLE ProductInfo (\
                ProductID INTEGER PRIMARY KEY AUTOINCREMENT,\
                ProductName varchar (500) NOT NULL,\
                Brand varchar (50) NOT NULL,\
                Model varchar (100) NOT NULL,\
                SKU INT NOT NULL,\
                Price REAL NOT NULL,\
                Stars varchar (100) NOT NULL,\
                TotalReviews varchar(100) NOT NULL,\
                FOREIGN KEY (SKU) REFERENCES ProductDetails (SKU));''')
#Dropping CustomerReviews table if already exists.
cursor.execute('''DROP TABLE IF EXISTS CustomerReviews''')
cursor.execute('''CREATE TABLE CustomerReviews (\
                ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,\
                SKU INT NOT NULL,\
                CustomerName varchar (50),\
                Star varchar (100),\
                Keyword varchar(500),\
                Reviews varchar(10000) NOT NULL,\
                ReviewDate DATE,\
                FOREIGN KEY (SKU) REFERENCES ProductInfo (SKU));''')

conn.close()
