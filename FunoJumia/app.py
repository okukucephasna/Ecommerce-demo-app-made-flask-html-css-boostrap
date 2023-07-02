from flask import*
import pymysql

app = Flask(__name__)

app.secret_key = "AW_r%@jN*HU4AW_r%@jN*HU4AW_r%@jN*HU4"
print(__name__)


@app.route('/')
def home():
    

    # TODO SQL 2  - Smartphones**
    
    # Return smartphones to **home.html**
    return render_template('index.html')

# Get Single Item, Note this route has an product_id, It displays a product based on product_id

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    # Check if form was posted by user
    if request.method == 'POST':
            # Receive what was posted by user including username, password1,password2 email, phone
            username = request.form['username']
            email = request.form['email']
            phone = request.form['phone']
            password1 = request.form['password1']
            password2 = request.form['password2']
	    
            # check if any of the password is less than eight x-ters and notify the user to put a password more that 8 -xters  
            if len(password1) < 8:
                return render_template('signup.html', error='Password must more than 8 xters')
		
            # Check if the 2 passwords are matching, if not notify the user to match them up.		
            elif password1 != password2:
                return render_template('signup.html', error='Password Do Not Match')
            else:
	        # Now we can save username, password, email, phone into our users table
		# Make a connection to database
                connection = pymysql.connect(host='localhost', user='root', password='',
                                             database='FUNO')
		# Create an Insert SQL, Note the SQL has 4 placeholders, Real values to be provided later			     
                sql = ''' 
                     INSERT INTO users(username, password, phone, email) 
                     values(%s, %s, %s, %s)
                 '''
		# Create a cursor to be used in Executing our SQL 
                cursor = connection.cursor()
		# Execute SQL, providing the real values to replace our placeholders 
                cursor.execute(sql, (username, password1, phone, email))
		# Commit to Save to database
                connection.commit()
		# Return a message to user to confirm successful registration.
                return render_template('signup.html', success='Registered Successfully')

    else:
        # Form not posted, display the form to allow user Post something
        return render_template('signup.html')

# Get Single Item, Note this route has an product_id, It displays a product based on product_id

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = pymysql.connect(host='localhost', user='root', password='',
                                     database='FUNO')

        sql = '''
           select * from users where username = %s and password = %s
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (username, password))

        if cursor.rowcount == 0:
            return render_template('signin.html', error='Invalid Credentials')  
        else:
            session['key']= username  
            return redirect('/')  # redirect to Home Default route, After success Login
    else:
        return render_template('signin.html')
    


    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/signin')

@app.route('/', methods=['POST', 'GET'])
def sellerhome():
    # Check if form was posted by user
    if request.method == 'POST':
            # Receive what was posted by user including username, password1,password2 email, phone
            id = request.form['id']
            name = request.form['name']
            description = request.form['description']
            cost = request.form['cost']
            category = request.form['category']
        
	        # Now we can save username, password, email, phone into our users table
		# Make a connection to database
            connection = pymysql.connect(host='localhost', user='root', password='',
                                             database='FUNO')
		# Create an Insert SQL, Note the SQL has 4 placeholders, Real values to be provided later			     
            sql = ''' 
                     INSERT INTO goods(id, name, description, cost,category) 
                     values(%s, %s, %s, %s, %s)
                 '''
		# Create a cursor to be used in Executing our SQL 
            cursor = connection.cursor()
		# Execute SQL, providing the real values to replace our placeholders 
            cursor.execute(sql, (id, name, description, cost,category))
		# Commit to Save to database
            connection.commit()
		# Return a message to user to confirm successful registration.
            return render_template('signup.html', success='Registered Successfully')

    else:
        # Form not posted, display the form to allow user Post something
        return render_template('signup.html')
    
@app.route("/get",methods=['POST','GET'])
def get():
     connection = pymysql.connect(host='localhost', user='root', password='',
                                             database='FUNO')
     sql='select * from property'
     cursor=connection.cursor()
     cursor.execute(sql)
     if cursor.rowcount==0:
          return render_template("get.html",message="No records to display")
     else: 
        property=cursor.fetchall()
        return render_template("get.html",data=property)
     

       
if __name__ == '__main__':
    app.run(debug=True)