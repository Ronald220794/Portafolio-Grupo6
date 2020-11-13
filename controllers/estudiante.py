from flask_restful import Resource, reqparse
from models.estudiante import EstudianteModel
# @app.route("/estante",methods=["get","post"])


class EstudiantesController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "nombre",
        type=str,
        required=True,
        help="Falta el nombre del estudiante"
    )
    parser.add_argument(
        "appat",
        type=str,
        required=True,
        help="Falta el apellido paterno del estudiante"
    )
    parser.add_argument(
        "apmat",
        type=str,
        required=True,
        help="Falta el apellido materno del estudiante"
    )
    parser.add_argument(
        "descripcion",
        type=str,
        required=True,
        help="Falta la descripcion del estudiante"
    )
    parser.add_argument(
        "job",
        type=str,
        required=True,
        help="Falta el trabajo del estudiante"
    )
    parser.add_argument(
        "address",
        type=str,
        required=True,
        help="Falta la direccion del estudiante"
    )
    parser.add_argument(
        "email",
        type=str,
        required=True,
        help="Falta el email del estudiante"
    )

    def get(self):
        estudiantes = EstudianteModel.query.all()
        # print(estantes)
        resultado = []
        for estudiante in estudiantes:
        #    print(estudiante.libros)
        #    libros=[]
        #    for libro in estante.libros:
        #        print(libro.mostrar_json())
        #     libros.append(libro.mostrar_json())
            temporal = estudiante.mostrar_json()
           # temporal['libros'] = libros
            resultado.append(temporal)
        return {
            'ok': True,
            'content': resultado,
            'message': None
        }

    def post(self):
        data = self.parser.parse_args()
        estudiante = EstudianteModel(data['nombre'], data['appat'], data['apmat'], data['descripcion'],
                    data['job'], data['address'], data['email'])
        try:
            estudiante.guardar_bd()
            print(estudiante)
            return {
                'ok': True,
                'message': 'Se guardo exitosamente los datos del estudiante',
                'content': estudiante.mostrar_json()
            }
        except:
            return {
                'ok': False,
                'message': 'No se pudo guardar los datos del estudiante en la bd'
            }, 500


class EstudianteController(Resource):
    def get(self, est_id):
        estudiante = EstudianteModel.query.filter_by(id=est_id).first()
        #print(estudiante.libros)
        if estudiante:
            return {
                'ok': True,
                'content': estudiante.mostrar_json(),
                'message': None
            }
        else:
            return {
                'ok': False,
                'content': None,
                'message': 'No existe el estudiante con id: '+str(est_id)
            }, 404

    def put(self, est_id):
        estudiante = EstudianteModel.query.filter_by(id=est_id).first()
        if estudiante:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "nombre",
                type=str,
                required=True,
                help="Falta el nombre del estudiante"
            )
            parser.add_argument(
                "appat",
                type=str,
                required=True,
                help="Falta el apellido paterno del estudiante"
            )
            parser.add_argument(
                "apmat",
                type=str,
                required=True,
                help="Falta el apellido materno del estudiante"
            )
            parser.add_argument(
                "descripcion",
                type=str,
                required=True,
                help="Falta la descripcion del estudiante"
            )
            parser.add_argument(
                "job",
                type=str,
                required=True,
                help="Falta el trabajo del estudiante"
            )
            parser.add_argument(
                "address",
                type=str,
                required=True,
                help="Falta la direccion del estudiante"
            )
            parser.add_argument(
                "email",
                type=str,
                required=True,
                help="Falta el email del estudiante"
            )

            data = parser.parse_args()
            estudiante.nombre = data['nombre']
            estudiante.appat = data['appat']
            estudiante.apmat = data['apmat']
            estudiante.descripcion = data['descripcion']
            estudiante.job = data['job']
            estudiante.address = data['address']
            estudiante.email = data['email']
            estudiante.guardar_bd()

            return {
                'ok': True,
                'content': estudiante.mostrar_json(),
                'message': None
            }
        else:
            return {
                'ok': False,
                'content': None,
                'message': 'No existe el estudiante con id: '+str(est_id)
            }, 404
    
    # def delete(self, est_id):
        # desahiblitar ese estante segun su ID
     #   estudiante = EstanteModel.query.filter_by(id=est_id).first()
      #  if estante:
       #     if estante.estado == True:
        #        estante.estado = False
         #       estante.guardar_bd()
          #      return {
           #         'ok': True,
            #        'content': None,
             #       'message': 'Se inhabilito exitosamente el estante'
             #   }
           # else:
                # si el estante ya esta deshabilitado que indique que ya lo esta
            #    return {
            #        'ok': False,
            #        'content': None,
            #        'message': 'El estante ya se encuentra deshabilitado'
            #    }, 400
      #  else:
      #      return {
      #          'ok': False,
      #          'content':None,
      #          'message': 'No existe el estante'
      #      }, 400
