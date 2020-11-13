from flask import Flask, render_template
# pip install flask-restful
from flask_restful import Api
# pip install flask-sqlalchemy
from base_datos import db
from models.estudiante import EstudianteModel
from controllers.estudiante import EstudiantesController, EstudianteController
#from models.autor import AutorModel
# from models.libro import LibroModel
#from controllers.libro import LibrosController, LibroController, EncontrarLibroController
#from models.autorlibro import AutorLibroModel

app = Flask(__name__)
# dialect+driver://username:password@host:port/database
# es compatible con MySQL, Oracle, PostgreSQL, SQLite
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/portafolio'
api = Api(app=app)
@app.before_first_request
def iniciador():
    # Aca se conecta al servidor
    db.init_app(app)
    # Eliminacion de los modelos, x defecto elimina todos
    # db.drop_all(app=app)
    # Creacion de los Modelos
    db.create_all(app=app)

@app.route("/")
def inicio():
    
    #return render_template('index.html')
    return 'El servidor funciona correctamente'

@app.route("/estudiante")
def index():
    #resultado = [
     #   {
     #       "curso":"html5",
      #      "descripcion":"no se",
       # },
        #{
         #    "curso":"html5",
          #  "descripcion":"no se",
       # },
   # ]
#estudiantes = EstudianteModel.query.all()
    #resultados = []
    #temporal = estudiantes.__str__()
    #resultados = estudiantes.__str__()
    #print(temporal)
    #resultados.append(temporal)
    #print(resultados)

 #   resultados = []
  #  resultados = estudiantes.__str__()
    
    return ('template principal')
    #return render_template('index.html')#resultados=resultados#)

@app.route("/estudiante/<int:est_id>")
def est_inicio(est_id=None):
    estudiante = EstudianteModel.query.filter_by(id=est_id).first()
    contents=[]
    contents = estudiante.mostrar_json()
    print(contents)
    #print(est_id)
    return render_template('index.html',contents=contents, est_id=est_id)


   #return render_template('index.html') 

# DEFINIR MIS RUTAS
api.add_resource(EstudiantesController,'/estudiante')
api.add_resource(EstudianteController, '/estudiante/<int:est_id>')
#api.add_resource(LibrosController, '/libro')
#api.add_resource(LibroController, '/libro/<int:lib_id>')
#api.add_resource(EncontrarLibroController,'/libro/<string:palabra>')

if __name__ == '__main__':
    app.run(debug=True)