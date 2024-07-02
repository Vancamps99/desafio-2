""" Instalar Postgres e django

pip list
pip install django  (ya lo tengo en este pc (de mi hermano) )

#iniciar un entorno virtual y dentro de este ejecutar los comandos 
#una vez dentro de desafio2-ev activar el entorno virtual  .\Scripts\activate
 tuve que ejecutar este PS C:\Python\Django\desafio2-ev> Set-ExecutionPolicy RemoteSigned -Scope Process
 (no podia acceder al entorno virtual) 
 instalar django y el psycopg2-binary
 EJECUTAR 
pip install django
pip install psycopg2-binary
django-admin startproject desafio2 
(una vez creado el proyecto entrar a el y crear una aplicacion)
django-admin startapp desafioadl e incluirla en settings.py
vincular la base de datos postgressql al proyectoigual en settings.py
                             List of roles
 Role name |                         Attributes
-----------+------------------------------------------------------------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS  #el admin es postgres

""ESTO ES POR DEFAULT DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'desafioadl',
        'USER': 'postgres',
        'PASSWORD': 'Admin1234',  
        'HOST': 'localhost',
        'PORT': '5432',  
    }
    !!PARA USAR POSTGRES!!
}
#13:36 dice algo relacionado con el set o sept
#opcional la sobrecarga y tambien
# agregar al admin los modelos y admin.site.register(nombre-clase)
#una vez creado los modelos hacer
python manage.py makemigrations y python manage.py migrate
crear un super usuario python manage.py createsuperuser 


#python manage.py shell
#from desafioadl import services
#elimina_tarea(7)

#retorno = services.crear_nueva_tarea('tarea 1')
print(retorno)
#retorno = services.crear_sub_tarea(1,'subtarea 2')
print(retorno)
#retorno = services.recupera_tareas_y_sub_tareas()
#retorno = services.elimina_tarea(1)
#retorno = services.elimina_sub_tarea(2)

# print(retorno)

COMANDOS SHELL
python manage.py shell
"""

