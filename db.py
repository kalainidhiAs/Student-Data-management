import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        sql="""
            create table if not exists students(
                id Integer primary key,
                name text not null,
                dob date not null,
                gender varchar(10),
                email text,
                phone text not null,
                address text not null,
                enrolment_no text,
                grade varchar(5)
            )        
            """
        self.cur.execute(sql)
        self.conn.commit()

    def insert(self,name,dob,gender,email,phone,address,enrolment_no,grade):
        self.cur.execute("INSERT INTO students values (null,?,?,?,?,?,?,?,?)", (name,dob,gender,email,phone,address,enrolment_no,grade))
        self.conn.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM students")
        rows = self.cur.fetchall()
        #print(rows)
        return rows
    
    def remove(self,id):
        self.cur.execute("delete from students where id=?",(id,))
        self.conn.commit()
    
    def update(self, id, name, dob, gender, email, phone, address, enrolment_no, grade):
        self.cur.execute("UPDATE students SET name=?, dob=?, gender=?, email=?, phone=?, address=?, enrolment_no=?, grade=? WHERE id=?", 
                         (name, dob, gender, email, phone, address, enrolment_no, grade, id))
        self.conn.commit()
    

    

    


