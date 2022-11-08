

# Use Framework
**Fastapi**


# Getting start
## Setting some files
### Pip library install
 - instaall pip library with pipenv
 ```
 $ pipenv --python 3.10
 $ pipenv install --three fastapi fastapi-sqlalchemy sqlalchemy_utils mysqlclient pytest inject pydantic alembic uvicorn sqlalchemy
 ```

### Create docker/api/requirements.txt
`$ pipenv requirements > docker/api/requirements.txt`

### Alembic init
 `$ cd db`
 `$ alembic init migrations`
  -> create maigration directory
 - Please edit file of "alembic.ini"
   "Comment out below code"
   `sqlalchemy.url = driver://user:pass@localhost/dbname`

### Edit almebic/env.py
Edit "migrations/env.py" 
quote -> "db/samples/env.py"
Please edit env.py while referring to sample/env.py
  and edit parts are belows.
 ` -- added code here -- `
 ` -- changed code here -- `

### Preparing seed file
 ` cp samples/seed.py ./seed.py`


## Build & Start Docker container

### Create docker network
 `$ docker network create fastapi_network`

### Rebuild & run api & db container
 ```
 $ docker compose build
 $ docker compose up
 
 ```
 - try connect
   http://localhost:8888/docs

## DB Migration
```
# enter api container
 $ docker compose run api bash
  or
 $ docker ps
 $ docker exec -it XXX bash
   (*)xxx: container id
 
 $ cd /usr/src/app/db

# create maigration file
 $ alembic revision --autogenerate -m "create users, tasks"
  -> db/migrations/versions/~~~_comment
# maigrate
 $ alembic upgrade head
```
### Insert DB using by seed file.
!!! run on docker in api container
```
# enter api container
 $ cd /usr/src/app/db
 $ python seed.py
``` 

## Access to fast-api.
 - try connect
   http://localhost:8888/docs


# Chips
### how to login mysql 
  ```
  $ docker-compose run api bash
  $ cd /usr/src/app/db  
  > mysql -h"$MYSQL_HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD"
  > use test_db
  ```
### stop container running using docker-compose
 - stop and rm container
  `$ docker ccompose down`
- only stop container
  `$ docker ccompose stop`

### how to use case migration methods
  - the first migrate  
     `$ alembic upgrade head`
  - step by step upgrade  
     `$ alembic upgrade +1`
  - downgrade  
     `$ alembic downgrade -1`  
     if you remake migration file, delete migration file
  - all reset  
     `$ alembic downgrade base`


# Reference Documents
 - Fast API Router <Original Documents>
   - https://fastapi.tiangolo.com/tutorial/bigger-applications/
 - FastAPI 入門
   - https://zenn.dev/sh0nk/books/537bb028709ab9/viewer/86648d
   - https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5
 - fast-api TODO ソース
  https://yusekita.com/detail/ed5ce795-0ac7-48da-881d-eb8d78d34e40/#cruds
   
