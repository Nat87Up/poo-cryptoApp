# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.3.0
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x05\x06\
C\
REATE TABLE Port\
ofolio (\x0a\x09idPort\
ofolio integer P\
RIMARY KEY,\x0a\x09nam\
e varchar(20) NO\
T NULL UNIQUE,\x0a\x09\
password varchar\
(255) NOT NULL\x0a)\
;\x0a\x0aCREATE TABLE \
Currency (\x0a\x09idCu\
rrency varchar(1\
0) PRIMARY KEY,\x0a\
\x09name varchar(10\
) NOT NULL,\x0a\x09tic\
ker varchar(3) N\
OT NULL,\x0a\x09price \
real,\x0a\x09circulati\
ngSupply integer\
,\x0a\x09rank integer,\
\x0a\x09last_update ti\
mestamp,\x0a\x09isCryp\
to boolean NOT N\
ULL CHECK (isCry\
pto IN (0, 1))\x0a)\
;\x0a\x0aCREATE TABLE \
PortofoliosCurre\
ncies (\x0a\x09portofo\
lio integer NOT \
NULL,\x0a\x09currency \
varchar(10) NOT \
NULL,\x0a\x09amount re\
al DEFAULT 0,\x0a\x09P\
RIMARY KEY(porto\
folio, currency)\
,\x0a\x09FOREIGN KEY (\
portofolio) REFE\
RENCES Portofoli\
o(idPortofolio),\
\x0a\x09FOREIGN KEY (c\
urrency) REFEREN\
CES Currency(idC\
urrency)\x0a);\x0a\x0aCRE\
ATE TABLE Crypto\
Transaction (\x0a\x09i\
dTransaction int\
eger PRIMARY KEY\
,\x0a\x09date timestam\
p,\x0a\x09amountSend r\
eal,\x0a\x09amountRece\
ived real,\x0a\x09curr\
encySend varchar\
(10) NOT NULL,\x0a\x09\
currencyReceived\
 varchar(10) NOT\
 NULL,\x0a\x09portofol\
io integer NOT N\
ULL,\x0a\x09FOREIGN KE\
Y (currencySend)\
 REFERENCES Curr\
ency(idCurrency)\
,\x0a\x09FOREIGN KEY (\
currencyReceived\
) REFERENCES Cur\
rency(idCurrency\
),\x0a\x09FOREIGN KEY \
(portofolio) REF\
ERENCES Portofol\
io(idPortofolio)\
\x0a);\x0a\x0a\x0aINSERT INT\
O Currency (idCu\
rrency, name, ti\
cker, isCrypto)\x0a\
VALUES ('dollar'\
, 'Dollar', 'usd\
', 0);\x0a\x0aINSERT I\
NTO Currency (id\
Currency, name, \
ticker, isCrypto\
)\x0aVALUES ('euro'\
, 'Euro', 'eur',\
 0);\x0a\
\x00\x00\x01\x0e\
\x00\
\x00\x03\xcfx\x9c\x8d\x93\xc1n\xc3 \x0c@\xef\xf9\x0a\
\x7f@\xd4?\xe8)J\xa5N[\x22%\xdd\xb9B`\
m\xa8)A\x04VU\xd3\xfe}3\x1d+Y\x08\xdb\
\x09\x1b?\x03y\x90\xbe~\xac\xab\x03Hq0LM\
\x8c[9\xaa\x12\x04\xb3X\x02;\x8fN\xd9\x1e\x95\x08\
q\x87\x1c\xe5\x1b\x8a\xb2\xa8\x9c1\xa8\xf8\x95\xaa\x1b)\
B\x0al\x82{\xe6[\xe7\xa8bg$\x88\xc6D\xd9\
J~BC\xc0-J \xdaH\xee\x97\xf0A\x02\xe0\
\xd2p70+\xd5K\xef\xb4\x1e\xfc\xa1\x16\x93\x89\xc6\
\x81M\xf6\xe84}<\xb5P\xfa\xec\xb3\x04\xfbe\xeb\
D\x10\x8d\x89\xb2\x9c*s\xd5v\xf4>\xbe\xe39\x16\
T\xae\xca[\xba\xfei\x89%f\xb0\xdf23\xe8\x5c\
j\x06\xfc\x9f\xdc\xcc\x02\xab\x923=\xb1\xec;\xc6\x17\
&\x13\xd2C\xb1\xd8u\xed\x13\xdc\xe6\xa2\xa7^\xec\x9b\
\xa6\xee\xe0\xa1\xdd7\x10_C|\x99\xd06\xcb\xc6\x0d\
\x8f\x88\xed\xca\xdf\xf0\xd7\xea\xe1p\xf9\x1d\x02\xb5\xcd<\
\x9d\xe2\xfd\xf2\x8a\x06?>\x01(6k\xa7\
"

qt_resource_name = b"\
\x00\x03\
\x00\x00z|\
\x00s\
\x00q\x00l\
\x00\x07\
\x00P\xa5B\
\x00i\
\x00n\x00i\x00t\x00_\x00d\x00b\
\x00\x1a\
\x08P\xf0\x13\
\x00s\
\x00c\x00r\x00i\x00p\x00t\x00_\x00s\x00e\x00l\x00e\x00c\x00t\x00_\x00t\x00r\x00a\
\x00n\x00s\x00a\x00c\x00t\x00i\x00o\x00n\x00s\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x810\x9c\x9b\x9e\
\x00\x00\x00 \x00\x01\x00\x00\x00\x01\x00\x00\x05\x0a\
\x00\x00\x01\x81@\x02yr\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()