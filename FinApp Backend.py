def dbcreate():
    mycon=mysql.connect(host="localhost", user="root", passwd = "root")
    mycur=mycon.cursor()
    mycur.execute("show databases")
    v=mycur.fetchall()
    f=0
    for i in v:
        if i[0]=="wallet":
            f=1
         
    if f==0:
        mycon=mysql.connect(host="localhost",user="root",passwd="root")
        mycur=mycon.cursor()
        mycur.execute("create database Wallet")
        mycon.commit()

        mycon=mysql.connect(host="localhost",user="root",passwd="root", database="Wallet")
        mycur=mycon.cursor()
        mycur.execute("create table Accounts(FullName char(20), EmailID char(20), UserName char(20), Passwd char(20))")
        mycon.commit()

        mycon=mysql.connect(host="localhost",user="root",passwd="root", database="Wallet")
        mycur=mycon.cursor()
        mycur.execute("create table Trans(TransName char(20), Amount float(13,2), Date date, TransType char(20), InOut char)")
        mycon.commit()

        mycon=mysql.connect(host="localhost",user="root",passwd="root", database="Wallet")
        mycur=mycon.cursor()
        mycur.execute("create table Bills(BillName char(20), BillMonth char(20), Amount float(13,2), DueDate date)")
        mycon.commit()

def cursorWallet():
    global mycur, mycon
    mycon=mysql.connect(host="localhost",user="root",passwd="root", database="Wallet")
    mycur=mycon.cursor()

def signup(a, b, c, d, e):
    cursorWallet()
    mycur.execute("insert into Accounts values(%s, %s, %s, %s, %s)",(a,b,c,d,e,))
    mycon.commit()

def login (a,b):
    cursorWallet()
    mycur.execute("select Passwd from Accounts where UserName = %s", (a,))
    if b ==mycur.fetchall()[0][0]:
        return True

def transEntry(a, b, c, d, e):
    cursorWallet()
    mycur.execute("insert into Trans values(%s, %s, %s, %s, %s)",(a,b,c,d,e,))
    mycon.commit()

def billEntry(a, b, c, d, e):
    cursorWallet()
    mycur.execute("insert into Bills values(%s, %s, %s, %s)",(a,b,c,d,))
    mycon.commit()
  
