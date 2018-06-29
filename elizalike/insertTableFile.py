import cx_Oracle as c
con = c.Connection('T795038/T795038@10.123.79.61:1521/georli06')
cur = c.Cursor(con)
try:
    cur.execute("insert into eliza (key,value) values('how?','good')")
    con.commit()
except:
    print("Error")
finally:
    print("done")
    cur.close()
    con.close()         
