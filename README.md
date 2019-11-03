# PassWord Manager APP


## Instalar python

Instalar la version de Python 3.7+

## Requerimientos
Instalar todos los requerimientos encontrados en el archivo requirements.txt

```
pip install requirements.txt
```


## Resolver errores con las librerias de criptografia
Copiar el archivo *fixes/fields.py* a *venv/site-packages/cryptographic_fields/fields.py*


Copiar el archivo *fixes/generate_encryption_key.py* a *venv/Lib/site-packages/cryptographic_fields/management/commands/fields.py*


## Cargar datos

Realizar la carga de datos inicial

```
python manage.py loaddata fixtures/initial.json
```

## Configurar el email

En el archivo .env configurar las variables


*EMAIL_HOST_USER =  'test@example'*


*EMAIL_HOST_PASSWORD = 'password'*

## Endpoints

### Generar password  [GET]

ruta : 
```
/api/generate/password
```

Requerimientos:
```
{
	"key":"OQmYzmageRRcWosZ11TGPoXqZ4JhcNWpzh8NUCeMlug="
}
```

### Validar contraseña [POST]

ruta : 
```
/api/validate/password
```

Requerimientos:
```
{
	"key":"OQmYzmageRRcWosZ11TGPoXqZ4JhcNWpzh8NUCeMlug=",
	"password":"J6C$F^QsmlkM"
}
```

### Listar cuentas [GET]

ruta : 
```
/api/accounts/list
```

Requerimientos:
```
{
	"key":"OQmYzmageRRcWosZ11TGPoXqZ4JhcNWpzh8NUCeMlug="
}
```


### Mostrar contraseña [POST]

ruta : 
```
http://127.0.0.1:8000/api/accounts/show
```

Requerimientos:
```
{
	"key":"OQmYzmageRRcWosZ11TGPoXqZ4JhcNWpzh8NUCeMlug=",
	"id":"1"
}
```

