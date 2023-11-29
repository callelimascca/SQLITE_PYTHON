import orm
from Tablas.Autores import Autores
from Tablas.Libros import Libros
from Tablas.Usuarios import Usuarios

db= orm.SQLiteORM("db_biblioteca") #especificar el nombre de base de datos en <("tiendas")>
#la primera letra de los nombres de las tablas siempre seran mayuscula.
db.crear_tabla(Autores)
db.crear_tabla(Libros)
db.crear_tabla(Usuarios)

# autorUno={"dni":76545445,"nombre":"quevedo","apellidos":"escoja de los rios"} #crear la variable para almacenar los datos y pasar por parametro 
# db.insertarUno("Autores",autorUno)

usuario_varios= [
    {   
        "dni":74656453,
        "nombre":"nadine",
        "apellidos":"atoccsa",
        "f_nacimiento":"12/11/1999",
        "estado":"activo"
    },
    {   
        "dni":76442556,
        "nombre":"feliciana",
        "apellidos":"ccachahua",
        "f_nacimiento":"07/11/2010",
        "estado":"activo"
    },
    {   
        "dni":7999123,
        "nombre":"orlando",
        "apellidos":"lopez",
        "f_nacimiento":"12/02/2002",
        "estado":"desactivo"
    },
    {   
        "dni":79957643,
        "nombre":"yadira",
        "apellidos":"medina",
        "f_nacimiento":"12/02/2004",
        "estado":"momia"
    },
    {   
        "dni":78113432,
        "nombre":"chamitos",
        "apellidos":"de la calle",
        "f_nacimiento":"08/02/1999",
        "estado":"desactivo"
    }
]
db.insertarVarios("Usuarios",usuario_varios)

# print(db.mostrar("Usuarios")) # muestra una lista de tuplas
# print(db.mostrar("Usuarios",type="objeto")) #muestra un objeto con sus campos y sus valores
# print(db.mostrar("Usuarios",where="estado= 'momia'",type="objeto"))# tambien se puede filtrar la informacion de la tabla
# print(db.mostrar("Usuarios",where="nombre LIKE 'or%'",type="objeto"))
# print(db.mostrar("Usuarios",where="dni=76442556",type="objeto"))
# db.actualizar("Usuarios",{"f_nacimiento":"11/08/2005"},where="dni=79957643")

# # dato_actualizar={"nombre":"chamos","apellidos":"ya es salida"}
# # db.actualizar("Usuarios",dato_actualizar,where="dni=78113432")
# db.eliminar("Usuarios",where="nombre='orlando'")
# db.eliminar("Usuarios",where="dni=78113432")
# print(db.mostrar("Usuarios",type="objeto"))