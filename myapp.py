from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskzaq'

# Create a MySQL connection
mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

@app.route('/')
def index():
    cur = mysql.cursor()
    cur.execute('SELECT * FROM your_table_name')
    data = cur.fetchall()
    return render_template('index.html', data=data)

# Route to add data
# Route to add data
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        details = request.form
        alamat = details.get('alamat')  # Assuming 'alamat' is the name of the field in your form
        fakultas = details.get('fakultas')  # Assuming 'fakultas' is the name of the field in your form
        nomer_hp = details.get('nomer_hp')  # Assuming 'nomer_hp' is the name of the field in your form

        # Add data to MySQL
        cur = mysql.cursor()
        cur.execute("INSERT INTO your_table_name(alamat, fakultas, nomer_hp) VALUES (%s, %s, %s)", (alamat, fakultas, nomer_hp))
        mysql.commit()
        cur.close()
        return redirect(url_for('index'))


# Route to edit data
@app.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM your_table_name WHERE id = %s", (id,))
    data = cur.fetchall()
    cur.close()
    return render_template('edit.html', data=data[0])

# Route to save data changes
@app.route('/update/<id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        details = request.form
        alamat = details['alamat']
        fakultas = details['fakultas']
        nomer_hp = details['nomer_hp']
        # Update data in MySQL
        cur = mysql.cursor()
        cur.execute("UPDATE your_table_name SET alamat = %s, fakultas = %s, nomer_hp = %s WHERE id = %s", (alamat, fakultas, nomer_hp, id))
        mysql.commit()
        cur.close()
        return redirect(url_for('index'))

# Route to delete data
@app.route('/delete/<id>', methods=['GET'])
def delete(id):
    # Delete data from MySQL
    cur = mysql.cursor()
    cur.execute("DELETE FROM your_table_name WHERE id = %s", (id))
    mysql.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
