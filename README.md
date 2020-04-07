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
En cualquier caso que no se mande la información como se debe, un response con status 400 "BAD REQUEST"
#### Parametros
- Keywords: Una lista de palabras en las que se basará la búsqueda
- Language: Puesto que se usa la API de Google, language servirá para definir una prioridad de que lenguaje queremos traer las noticias, no obstante, la misma API detecta el idioma de las palabras así que si se busca, digamos hola,mundo en inglés, la misma API nos regresará noticias en español y no en inglés.

### Ejemplo
#### Request
POST
https://deltaitest.herokuapp.com/api/news
```
{
	"keywords": ["hola","mundo"],
	"language": "es"
}
```
#### Response
```
{
    "news": [
        {
            "content": "La pandemia provocada por el coronavirus ha paralizado países y tiene confinados a millones de personas en todo el mundo. El COVID-19 no se detiene ante nada y ante nadie y está siendo especialmente cruento en las zonas del mundo que están afectadas por guerras, como en Siria. El secretario general de la ONU, Antonio Guterres,",
            "reference": "https://www.hola.com/realeza/20200406165027/princesa-haya-declaraciones-tras-sentencia-emir-dubai/",
            "score": 0.6
        },
        {
            "content": "\"Único. Gracias a todos. Vera, Dusan, Petra, Rade, Ivana, Marko y Ana. Sin palabras\". Ana Antic se despedía de su padre, Radomir Antic, con estas palabras y dos bonitas fotografías del que fuera entrenador del Atlético de Madrid .  Y es que Ana, figura influyente del mundo de la moda , personal shopper",
            "reference": "https://www.hola.com/actualidad/20200406165066/mundo-futbol-despide-radomir-antic/",
            "score": 0.4
        },
        {
            "content": "martes, 7 de abril de 2020 Bloomberg Viajes por podcast, visitas a museos, conciertos en streaming, entre otros, son algunos de los planes que se pueden hacer Margarita Coneo Rincón - mconeo@larepublica.com.co Si bien la Semana Santa es una época religiosa es también una oportunidad que muchos aprovechan para relajarse, pasear y disfrutar de las fiestas tradicionales con su familia, sin embargo, en medio de la cuarentena nacional, en la que nadie puede salir o viajar, muchos de estos planes se hacen imposibles.",
            "reference": "https://www.larepublica.co/ocio/planes-para-hacer-en-esta-semana-santa-desde-casa-en-medio-de-la-cuarentena-2988916",
            "score": 0.2
        }
    ]
}
```
## Más ejemplos en mi colección de [POSTMAN](https://www.getpostman.com/collections/546d699a039293c49228).
## Base de Datos 
### Mongo DB
La base de datos usada para éste proyecto fue MongoDB Atlas, es decir, la base de datos no vive en el servidor de Heroku, sino que fue deployada con la herramienta de Mongo y vive en un servidor de aws.
Pero la información guardada se puede consultar usando MongoDB Compass con el siguiente string de conección
```
mongodb+srv://<username>:<password>@deltaicluster-072dm.mongodb.net/test
```
