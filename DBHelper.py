# persons - stores persons with bought items 
# add items to bill using serial number
import psycopg2
import os.path

# DATABASE_URL = os.environ['DATABASE_URL']

class DBHelper:
    def __init__(self):
        # self.dbname = dbname
        # self.conn = sqlite3.connect(dbname,check_same_thread=False)
        # self.conn = psycopg2.connect(DATABASE_URL,sslmode='require')
        self.conn = psycopg2.connect(dbname="bill_split",user="nikhilanu")

    
    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS people (id integer, bought integer[], paid float, owner integer)"
        print("Creating items table")
        cur = self.conn.cursor()
        cur.execute(stmt)
        self.conn.commit()

        stmt = "CREATE TABLE IF NOT EXISTS bill (id integer, serial_number integer, bill_items text, cost float)"
        print("Creating bill table")
        cur = self.conn.cursor()
        cur.execute(stmt)
        self.conn.commit()

        stmt = "CREATE TABLE IF NOT EXISTS number_of_people (id integer, total integer)"
        print("creating number_of_people table")
        cur = self.conn.cursor()
        cur.execute(stmt)
        self.conn.commit()

    def add_number_of_people(self, id1, total):
        stmt = "INSERT INTO number_of_people (id,total) values (%s,%s)"
        args = (id1,total)
        cur = self.conn.cursor()
        cur.execute(stmt,args)
        self.conn.commit()

    def get_number_of_people(self, id1):
        stmt = "SELECT total FROM number_of_people WHERE id = (%s)"
        args = (id1, )
        cur = self.conn.cursor()
        cur.execute(stmt,args)
        population = []
        for row in cur:
            population.append(row[0])
        return population

    def add_items_to_bill(self, id1, serial_number, bill_items, cost):
        stmt = "INSERT INTO bill (id, serial_number, bill_items, cost) values (%s,%s,%s,%s)"
        args = (id1, serial_number, bill_items, cost)
        cur = self.conn.cursor()
        cur.execute(stmt,args)
        self.conn.commit()

    def add_items_bought(self, id1, items, paid, owner):
        stmt = "INSERT INTO people (id, bought, paid, owner) VALUES (%s,%s,%s,%s)"
        args = (id1, items, paid, owner)
        cur = self.conn.cursor()
        cur.execute(stmt,args)
        self.conn.commit()

    def number_of_bill_items(self, id1):
        stmt = "SELECT count(id) FROM bill WHERE id=(%s)"
        args = (id1, )
        cur = self.conn.cursor()
        cur.execute(stmt,args)
        return cur[0][0]

    def items_with_price(self, id1):
        stmt = "SELECT bill_items,cost FROM bill WHERE id = (%s)"
        args = (id1, )
        cur = self.conn.cursor()
        cur.execute(stmt,args)
        items = []
        for row in cur:
            items.append([row[0],row[1]])
        return items

    def get_items_with_price(self, id1):
        stmt = "SELECT owner,bought,paid from people where id=(%s)"
        args = (id1, )
        cur = self.conn.cursor()
        cur.execute(stmt, args)
        items_with_price = []
        for row in cur:
            items_with_price.append([row[0], row[1], row[2]])
        print(items_with_price)
        return items_with_price
    

    # def delete_items(self,item_text,owner):
    #     stmt = "DELETE from items WHERE subject = %s AND owner = %s"
    #     args = (item_text,owner)
    #     cur = self.conn.cursor()
    #     cur.execute(stmt,args)
    #     self.conn.commit()

    # def get_items(self,owner):
    #     stmt = "SELECT subject from items WHERE owner = %s"
    #     args = (owner,)
    #     cur = self.conn.cursor()
    #     cur.execute(stmt,args)
    #     subjects = []
    #     for row in cur:
    #         subjects.append(row[0])
    #     return subjects

    # def increment_attendance(self,text,isPresent,owner):
    #     if isPresent == 1:
    #         stmt = "UPDATE items set present=present+1, total = total + 1 where subject = %s and owner = %s"
    #     else:
    #         stmt = "UPDATE items set total = total + 1 where subject = %s and owner = %s"
    #     args = (text,owner)
    #     cur = self.conn.cursor()
    #     cur.execute(stmt,args)
    #     self.conn.commit()

    # def delete_entire_table(self,owner):
    #     stmt = "delete from items where owner = %"
    #     args = (owner,)
    #     cur = self.conn.cursor()
    #     cur.execute(stmt,args)

    # def display_details(self,owner):
    #     stmt = "SELECT * from items where owner = %s"
    #     args = (owner, )
    #     cur = self.conn.cursor()
    #     temp = []
    #     cur.execute(stmt,args)
    #     for row in cur:
    #         temp.append([row[0],row[1],row[2]])

    #     return temp 
    #     # return [[x[0],x[1],x[2]] for x in cur.execute(stmt,args)]
    
    # def drop(self,owner):
    #     stmt = "DROP table items"
    #     cur = self.conn.cursor()
    #     cur.execute(stmt)
    #     self.conn.commit()
    
    def get_ids(self):
        stmt = "SELECT id FROM bill"
        cur = self.conn.cursor()
        cur.execute(stmt)
        temp = []
        for row in cur:
            temp.append(row[0])
        
        return temp