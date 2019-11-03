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
/accounts/api/generate/password
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
/accounts/api/validate/password
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
accounts/api/list
```

Requerimientos:
```
{
	"key":"OQmYzmageRRcWosZ11TGPoXqZ4JhcNWpzh8NUCeMlug=",
	"user_id":"2"
}
```


### Mostrar contraseña [POST]

ruta : 
```
/accounts/api/show
```

Requerimientos:
```
{
	"key":"OQmYzmageRRcWosZ11TGPoXqZ4JhcNWpzh8NUCeMlug=",
	"account_id":"1",
	"user_id":"2"
}
```

### Añadir Cuenta  [POST]

ruta : 
```
/accounts/api/add
```

Requerimientos:
```
{
	"key":"OQmYzmageRRcWosZ11TGPoXqZ4JhcNWpzh8NUCeMlug=",
	"user_id":"2",
	"site":"www.youtu.com",
	"email":"stalinfernandocarrioncarchi@gmail.com",
	"password":"asdasddas123434"
	
}
```

o 
```
{
	"key":"OQmYzmageRRcWosZ11TGPoXqZ4JhcNWpzh8NUCeMlug=",
	"user_id":"2",
	"site":"www.youtu.com",
	"user_name":"stalinfernando",
	"password":"asdasddas123434"
	
}
```

## TODO

1. listar cuentas en la pagina de *accounts.html* llamndo al api (accounts/api/list)
2. crear formulario *add_accounts.html* para añadir una cuenta que me permita sugerir contraseñas y validar la contraseña, los datos deberan ser enviados al api (accounts/api/add)