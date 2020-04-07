# API News 
API Para obtener noticias de ciertas keywords
## Deploy en server Heroku
### 1. Requerimientos para levantar la API en Heroku
- Heroku
- Git
### 2. Creamos una carpeta para clonar el proyecto de github
```
mkdir micarpeta
cd micarpeta
```
Y procedemos a clonar el proyecto
```
git clone https://github.com/NickMathworld/deltaiTest
cd deltaiTest
```
### 3. Creamos la app en Heroku
```
heroku login
heroku create name
```
Verificamos que se haya creado el remote de git
```
git remote -v
heroku  https://git.heroku.com/deltaitest.git (fetch)
heroku  https://git.heroku.com/deltaitest.git (push)
origin  https://github.com/NickMathworld/deltaiTest (fetch)
origin  https://github.com/NickMathworld/deltaiTest (push)
```
### 4. Hacemos push al git de Heroku
```
git push heroku master
```
Una vez que finalice, nos dará la dirección del server donde fue deployado
```
remote: Verifying deploy... done.
To https://git.heroku.com/young-wave-03473.git
 * [new branch]      master -> master
```
Podemos hacer un open para verificar que se está ejecutando de manera correcta
```
heroku open
```
Se nos abrirá una ventana en nuestro navegador y se mostrará un mensaje de hola mundo
## Uso de la API
Una vez deployada la API, podemos hacer uso postman,curl o cualquier herramienta para mandar peticiones http
### Formato del request 
El schema que se pretende recibir es el siguiente
```
news = {
    'type': 'object',
    'properties': {
        'keywords': {'type': 'array','items':{'type':'string'} },
        'language': {'type': 'string'},
    },
    'required': ['keywords']
}
```
