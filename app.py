from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__) #instanciamos flask

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema'
mysql.init_app(app)


@app.route('/') #rootear para decirle que cuando alguien entre a esta direccion (o sea mi servidor), redireccionar
def index():
    sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'laura', 'obamacapo@ciudad.com.ar', 'fotodelauraobama.jpg');" 
    conn=mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return render_template('empleados/index.html')

if __name__=='__main__':
    app.run(debug=True)

