import cx_Oracle as c
con = c.Connection('T795038/T795038@10.123.79.61:1521/georli06')
cur = c.Cursor(con)
user_input=input()
try:
    #print(user_input)
    cur.execute("SELECT value from eliza where key like '%"+user_input.strip()+"%'")
    
    print(cur.rowcount)
    for i in cur:
        print(i)
except:
    print("Error")
finally:
    cur.close()
    con.close()          
