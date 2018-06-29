import cx_Oracle as c
con = c.Connection('T795038/T795038@10.123.79.61:1521/georli06')
cur = c.Cursor(con)
try:
    cur.execute("drop table eliza")
except:
    print("Error")
finally:
    cur.close()
    con.close() 