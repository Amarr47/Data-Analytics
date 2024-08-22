import ibm_db
dhn = "0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
did = "qyg77666"
dpw = "xXYKbzRzTcgaoLrQ"
ddr = "{IBM DB2 ODBC DRIVER}"
dd = "BLUDB"
dpo = "31198"
dpt = "TCPIP"
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(ddr,dd,dhn,dpo,dpt,did,dpw)
conn = ibm_db.connect(dsn, "DATABASE", "UID")

print("Connected to database: ", dd, "as user: ", did, "on host: ", dhn)
server = ibm_db.server_info(conn)

print ("DBMS_NAME: ", server.DBMS_NAME)
print ("DBMS_VER:  ", server.DBMS_VER)
print ("DB_NAME:   ", server.DB_NAME)
client = ibm_db.client_info(conn)

print ("DRIVER_NAME:          ", client.DRIVER_NAME)
print ("DRIVER_VER:           ", client.DRIVER_VER)
print ("DATA_SOURCE_NAME:     ", client.DATA_SOURCE_NAME)
print ("DRIVER_ODBC_VER:      ", client.DRIVER_ODBC_VER)
print ("ODBC_VER:             ", client.ODBC_VER)
print ("ODBC_SQL_CONFORMANCE: ", client.ODBC_SQL_CONFORMANCE)
print ("APPL_CODEPAGE:        ", client.APPL_CODEPAGE)
print ("CONN_CODEPAGE:        ", client.CONN_CODEPAGE)
query ="CREATE TABLE songs(name varchar(255) NOT NULL,album varchar(255)  NOT NULL primary key,artist varchar(255) NOT NULL,year int NOT NULL)"
st = ibm_db.exec_immmediate(conn,query)
i1 = "INSERT INTO songs(name,album,artist,year) VALUES('One Last Time' , 'My Everything' , 'Ariana Grande' , 2014)"
ist1 = ibm_db.exec_immmediate(conn,i1)
i2 = "INSERT INTO songs(name,album,artist,year) VALUES('Dangerous Woman','Dangerous Woman','Ariana Grande',2016)"
ist2 = ibm_db.exec_immmediate(conn,i2)
i3 = "INSERT INTO songs(name,album,artist,year) VALUES('God Is A Woman','Sweetener','Ariana Grande',2018)"
ist3 = ibm_db.exec_immmediate(conn,i3)
i4 = "INSERT INTO songs(name,album,artist,year) VALUES('7 Rings','Thank U,Next','Ariana Grande',2019)"
ist4 = ibm_db.exec_immmediate(conn,i4)
i5 = "INSERT INTO songs(name,album,artist,year) VALUES('POV','Positions','Ariana Grande',2020)"
ist5 = ibm_db.exec_immmediate(conn,i5)
selectQuery = "select * from songs"
selectStmt = ibm_db.exec_immediate(conn, selectQuery)
while ibm_db.fetch_row(selectStmt) != False:
   print (" Song_Name:",  ibm_db.result(selectStmt, "name"), " Album_Name:",  ibm_db.result(selectStmt, "album"))