import mysql.connector      # import module

class Database:             # create class for db operations 
    def __init__(self, db):
        try:
             # create connection
            self.con = mysql.connector.connect(   
                host="localhost",
                user="root", 
                password="root",
                database=db)
            self.cur = self.con.cursor()                    # create cursor obj
            # create table , name -> student
            sql = """
            CREATE TABLE IF NOT EXISTS student(
                rollno int Primary Key,
                name varchar(30),
                DOB varchar(30),
                gender varchar(30),
                mark_10th varchar(30),
                join_date varchar(30),
                dept varchar(30),
                contact varchar(10),
                address varchar(30)
            )
            """
            self.cur.execute(sql)  #execute in db
            self.con.commit()       #save the changes

            if self.con.is_connected(): #check connected or not
                print("Successfully connected...")
        except Exception as e:
            print("Connection error:", e)

    def insert(self, rollno, name, DOB, gender, mark_10th, join_date, dept, contact, address):   #insert data into table 
        try:
            sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"   # insert 9 value
            values = (rollno, name, DOB, gender, mark_10th, join_date, dept, contact, address)   #store all values in tuple
            self.cur.execute(sql, values)  # why use self --> which obj(database-->mpc) execute this command
            self.con.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print("Insert error:", e)

    def fetch(self):    #display all records
        self.cur.execute("SELECT * from student")
        rows = self.cur.fetchall()   #why dont use for loop ?
        return rows

    def remove(self, rollno):   # delete value using rollno
        try:
            sql = "DELETE FROM student WHERE rollno = %s"
            self.cur.execute(sql, (rollno,))  # why use tuple --> its only accept tuple , without comma its not consider as a tuple
            self.con.commit()
            print("Record with rollno =", rollno, "removed successfully.")
        except Exception as e:
            print("Remove error:", e)

    def update(self, rollno, name, DOB, gender, mark_10th, join_date, dept, contact, address):  #update database
        try:
            sql = "UPDATE student SET name=%s, DOB=%s, gender=%s, mark_10th=%s, join_date=%s, dept=%s, contact=%s, address=%s WHERE rollno=%s"
            values = (name, DOB, gender, mark_10th, join_date, dept, contact, address, rollno)  # why give last in rollno
            self.cur.execute(sql, values)
            self.con.commit()
            print("Record with rollno =", rollno, "updated successfully.")
        except Exception as e:
            print("Update error:", e)



# test
'''
obj = Database("g_example")
obj.insert(1, "a", "2005-06-01", "male", "100", "2005-06-01", "ct", "1234567890", "tnhb")
print(obj.fetch())
obj.remove(1)
print(obj.fetch())
obj.update(2, "ganeshan", "2005-06-01", "male", "100", "2005-06-01", "ct", "1234567890", "tnhb")
print(obj.fetch())
'''
