from base_datos import db
class EstudianteModel(db.Model):
    __tablename__="t_estudiante"
    id = db.Column("est_id",db.Integer, primary_key=True)
    nombre = db.Column("est_nom", db.String(50))
    appat = db.Column("est_app", db.String(50))
    apmat = db.Column("est_apm", db.String(50))
    descripcion = db.Column("est_descrip", db.String(255))
    job = db.Column("est_job", db.String(50))
    address = db.Column("est_address", db.String(100))
    email = db.Column("est_email", db.String(100))


    #capacidad = db.Column("est_cap", db.Integer, nullable=False)
    #ubicacion = db.Column("est_ubic", db.String(50))
    #descripcion = db.Column("est_desc", db.String(45))
    #estado = db.Column(db.Boolean, default=True)
    # Voy a crear mi relacion inversa
    # sirve para hacer la relacion inversa (traer todos los libros que pertenecen a un estante) y nos ayuda demasiado para la logica
    #libros = db.relationship('LibroModel', backref='estante')

    def __init__(self, nombre, appat, apmat, descripcion, job, address, email):
        self.nombre = nombre
        self.appat = appat
        self.apmat = apmat
        self.descripcion = descripcion
        self.job = job
        self.address = address
        self.email = email

    
    def guardar_bd(self):
        db.session.add(self)
        db.session.commit()
    
    def mostrar_json(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'appat':self.appat,
            'apmat':self.apmat,
            'descripcion':self.descripcion,
            'job':self.job,
            'address':self.address,
            'email':self.email
            #'capacidad':self.capacidad,
            #'ubicacion':self.ubicacion,
            #'descripcion': self.descripcion,
            #'estado': self.estado
        }
    def __str__(self):
       # return '%s, %s, %s'%(self.id, self.capacidad, self.ubicacion)
       return '%s, %s, %s , %s, %s, %s , %s, %s' % (self.id, self.nombre, self.appat, self.apmat, self.descripcion,
                                                    self.job, self.address, self.email)
