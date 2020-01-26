from flask import *
app = Flask(__name__)
import psycopg2
import os.path
from DBHelper import DBHelper
# from DBHelper import DBHelper
# @app.route('/')
# def home():
#     return render_template('home4.html')

# @app.route('/welcome')
# def welcome():
#     return render_template('welcome.html')


# @app.route('/hello')
# def hello():
#     return render_template('hello.html')

db = DBHelper()
conn = psycopg2.connect(dbname="bill_split",user="nikhilanu")


# self.conn = psycopg2.connect(DATABASE_URL,sslmode='require')
# global b
# db = DBHelper()
# conn = psycopg2.connect(dbname="bill_split",user="nikhilanu")
app.config['DEBUG'] = True







def calculate(id1,i):
     # format: /calculate id
    # id1 = update.message.text.split(" ")[1]
    # number_of_bill_items = db.get_number_of_people(id1)[0]
    # print(number_of_bill_items)

    bill_items = db.items_with_price(id1)
    # print(bill_items)
    # population = db.get_number_of_people(id1)[0]
    population = i
    item_per_person = []
    for i in range(0, len(bill_items)):
        item_per_person.append([])
        print(item_per_person)
    # print(item_per_person)
    price_pairs = []
    for i in range(0, population):
        price_pairs.append([])

    items_with_price = db.get_items_with_price(id1)

    owners_list = []
    initial_amount_paid = []
    i = -1
    for person in items_with_price:
        i += 1
        owner = person[0]
        bought_items = person[1]
        paid = person[2]

        owners_list.append(owner)
        initial_amount_paid.append(paid)
        price_pairs[i].append(owner)
        price_pairs[i].append(0-paid)
        for j in bought_items:
            # print(j)
            index = int(j) - 1
            # print(item_per_person[0])
            item_per_person[index].append(owner)
    
    index = 0
    for i in item_per_person:
        share_number = len(i)
        if share_number>0:
            share_cost = bill_items[index][1] / share_number
            for j in i:
                for pair in price_pairs:
                    if pair[0] == j:
                        pair[1] += share_cost
        index+=1
    
    price_pairs.sort(key=lambda x: x[1])
    print(price_pairs)
        
    i = 0
    j = len(price_pairs)-1
    while(i!=j):
        if price_pairs[i][1]+price_pairs[j][1]<=0:
            temp=price_pairs[j][1]
            price_pairs[i][1]+=price_pairs[j][1]
            price_pairs[j][1]=0
            print(price_pairs[i][0],price_pairs[j][0], abs(temp))
            return "user"+str(price_pairs[i][0])+" <--  user"+str(price_pairs[j][0])+"\n"+"Rs."+ str(abs(temp))
            j-=1
            
        elif price_pairs[i][1]+price_pairs[j][1]>0:
            temp=price_pairs[i][1]
            price_pairs[j][1]+=price_pairs[i][1]
            price_pairs[i][1]=0
            print(price_pairs[i][0],price_pairs[j][0], abs(temp))
            return "user"+str(price_pairs[i][0])+" <--  user"+str(price_pairs[j][0])+"\n"+"Rs."+ str(abs(temp))
            i+=1













@app.route('/log',methods=['GET', 'POST'])
def log():
    error = None
    if request.method =='POST':
        # if request.form['item'] == 'admin' or request.form['price'] =='admin':
        #     error = 'Invalid Credentials. Please try again'
        # else:
            # return redirect(url_for('hello'))
        # result=request.form
        # i = request.form.get('total')
        # paid = request.form.getlist('initial_paid')
        
        n=[]
        p=[]
        i = request.form.get('getNumberOfUsers')
        i = int(i)
        print(i)
        
        session['my_var'] = i
        return redirect(url_for('next'))
    return render_template('home5.html', error=error) 



@app.route('/next',methods=['GET', 'POST'])
def next():
    i = session.get('my_var', None)
    i = int(i)

    n=[]
    p=[]

    if request.method =='POST':
        result=request.form
        paid = request.form.getlist('initial_paid')
        for k in range(0,i):
            # name = request.form.getlist('item-name'+str(k))
            # price = request.form.getlist('item-price'+str(k))
            name = request.form.getlist('item'+str(k))
            price = request.form.getlist('price'+str(k))
            n+=[name]
            p+=[price]

        print(n)
        print(p)


        id1 = 1569

        # db.add_items_to_bill(id, 6, n[0][0], p[0][0])

        stmt = "SELECT max(serial_number) FROM bill WHERE id = (%s)"
        args = (id1, )
        cur = conn.cursor()
        cur.execute(stmt,args)

        for row in cur:
            print(row[0])

            if row[0] == None:
                it=0
            else:
                it=int(row[0])+1
                    

        
        for l in range(0,len(n)):
            # items = []
            for m in range(0,len(n[l])):
                stmt = "SELECT * FROM bill WHERE bill_items = (%s) and id = (%s)"
                args = (n[l][m], id1)
                cur = conn.cursor()
                cur.execute(stmt,args)

                #Flag is set to check if the element already exists in the DB
                flag=0

                for row in cur:
                    if row[0]==id1:
                        flag=1
                        # break
                
                if flag==0:
                        db.add_items_to_bill(id1,it,n[l][m], p[l][m])
                        it += 1
                # items.append(it)
                # print(items)
                
            #checking if person is already there in people db
                

                
        for l in range(0,len(n)):
            items = []
            for m in range(0,len(n[l])):

                stmt = "SELECT serial_number FROM bill WHERE bill_items = (%s)"
                args = (n[l][m], )
                cur = conn.cursor()
                cur.execute(stmt,args)

                for row in cur:
                    items.append(row[0])


                stmt = "SELECT * FROM people WHERE owner = (%s) and id = (%s)"
                args = (l, id1)
                cur = conn.cursor()
                cur.execute(stmt,args)
                # print(cur)
                flag2 = 0
                b = []
                for row in cur:
                    if row[0]==id1:
                        flag2 = 1
                        break
                
                if flag2 == 1:
                    for row in cur:
                        print(row)
                        print(items)
                        b = row[1]
                        for z in items:
                            if z not in b:
                                b.append(z)
                    
                    print(items)

                    stmt = "select * from people;"
                    # args = (items, l, id1)
                    cur = conn.cursor()
                    cur.execute(stmt, )
                    for row in cur:
                        print(row)

                    stmt = "UPDATE people SET bought = bought || (%s) WHERE owner = (%s) and id = (%s) and (%s) not in (select bought from people)"
                        # stmt = "UPDATE people set bought =  (%s) WHERE owner = (%s) and id = (%s)"
                    args = (items, l, id1, items)
                    cur = conn.cursor()
                    cur.execute(stmt,args)
                    conn.commit()
            # Entering items into the people table;

                    stmt = "select * from people;"
                    # args = (items, l, id1)
                    cur = conn.cursor()
                    cur.execute(stmt, )
                    for row in cur:
                        print(row)
            
                else:
                    db.add_items_bought(id1,items,paid[l],l)

        session['fin_val'] = calculate(id1,i)
        return redirect(url_for('final'))


    return render_template('testing.html',i=i)


@app.route('/final')
def final():
    q = session.get('fin_val', None)
    return render_template('hello.html',q=q)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()

