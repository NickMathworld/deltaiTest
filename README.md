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
