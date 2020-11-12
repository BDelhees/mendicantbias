# Data Science and Toolkits

### Milestone 3

#### 1.

We followed the given steps from the docker compose website. First, we had to install the Docker Engine and Docker compose. We did the following steps:

1. Setup
 - Create directory for the project
 - Create a file called app.py in the project directory:
 ```sh
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

```   
 - Create a file called requirements.txt:

```sh
flask
redis
``` 

2. Create Dockerfile
  - In the project directory, create a file named Dockerfile:
```sh  
FROM python: 3.7-alpine 

WORKDIR /code

ENV FLASK_APP= app.py

ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

Copy requirements.txt requirements.txt 

RUN pip install -r requirements.txt 

EXPOSE 5000

COPY . . 

CMD ["flask", "run"]
``` 
3. Define services in a Compose file
  - Create a file called docker-compose.yml in the project directory:
```sh
version: "3.8"
services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: "redis:alpine"
``` 

4. Build and run your app with compose
  - From your project directory, start up your application by running docker-compose up.
  - Enter http://localhost:5000/ in the browser to see if the application is up and running.


***Encountered Problems:***

We did not encounter any problems until the last step. When we ran docker-compose up, we got the following error message:

Version in the "./docker-compose.yml" is unsupported.

We looked for solutions on Github. We checked whether the problem was caused by the version of the package. This was not the case. We further tried changing the version of the Dockerfile and then run the .yml file, but to no avail. 

#### 2.

1. What is PostgreSQL?

PostgreSQL is an open source object-relational database management system (RDBMS) that uses and extends the SQL language combined with other features (store,scal). It runs on all major operating systems. It is also highly extensible. Different programming languages can be used, for example to build custom functions. It also tries to conform with the SQL standard, which gives it a wide basis for usage. The development community adheres closely to the SQL standard. However, there are a number of PostgreSQL specific functionalities.  These are pointed out in the documentation. PostgreSQL has an extensive range of third-party extensions (e.g. PostGIS, management of geodata). Basically, PostgreSQL is SQL with additional functionalities that SQL does not have.

2. Run a PostgreSQL server and find an appropriate Python package that allows communication with the database server

PostgreSQL is usually available for all Unbuntu versions by default. But we had to install it, because we needed a specific version (12.4). For that we followed the steps below:

  - Create the file repository configuration:
```sh
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```
  - Import the repository signing key:
```sh
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```
  - Update the package lists:
```sh
sudo apt-get update
```
  - Install PostgreSQL Version 12.4. If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
```sh
sudo apt -y install postgresql-12 postgresql-client-12 
```
  - Giving sudo-rights to the created user:
```sh
sudo su - postgres 
```
  - to start PostgreSQL prompt:
```sh
psql
```

This all worked well. We assume at this point that the installation worked well. Now we have to run a PostgreSQL using a docker image.

1. Download the Docker image from the official Docker hub website https://hub.docker.com/_/postgre :

```sh
docker pull postgres
```

2. Run the Docker image with the following command:

```sh
docker run –name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p postgres
```

3. To check, on what port the docker container runs (it was port 5432/tcp):

```sh
docker ps
```

4. Install package psycopg2:

```sh
sudo apt-get install python3-psycopg2
```

5. Connecting to PostgreSQL:

```sh
psycopg2.connect()
```

6. We need information about the Name of the database, User, Host, Password, Port, run the following code:

```sh
docker exec -tiu postgres some postgres psql
```

In the prompt we use the command \conninfo to get all the information (without the password). The Output was:

"You are connected to database “postgres” as user “postgres” via socket in “/var/run/postgresql” at port “5432”"

7. To access the "ms3_jokes" database via Python script called ***jokes_db.py***, we used the ***pyscopg2*** package we installed on step 4.

8. To connect the python file and the database, we need the information (Name of the database, User, Host, Password, Port) outlined in step 6 and its command.

9. To see the table, we ran:

```sh
\dt
```

10. Connecting to the PostgreSQL Database and see your table, as well as our database there, we ran:

```sh
docker pull dpage/pgadmin4
```

11. Since the pgadmin4 tool is up and running, we use our browser and go to http://127.0.0.1:5050

12. We can then add a new server via the dashboard. After that, we locate to "create - server" and in the "general" tab, we identify our pgAdmin server. In the connection tab, we use our information (User, Host, Password, Port) and click save. 

13. We can then check again if our jokes are still in the docker container and databse, we run:

```sh
docker run ...
docker exec ...
\dt
```




***Encountered Problems:***

When I tried to install the Docker engine on my Virtualbox.
When trying to install docker engine via https://docs.docker.com/engine/install/ubuntu/, while trying to remove old docker affiliated files, I got the following error message:

"Reading packages lists... Error! Write error- write (28: No space left on device)"

I then ran the following command to see if my space is full:

```sh
dh -h
```
And indeed, it turns out that the several filesystems (all /dev/loop and /cow) are at 100% capacity.



While trying to download the Docker image form the official Docker hub page, with:

```sh
sudo snap install docker
```
and,

```sh
docker pull postgres
```
I encountered the following message:

"error: cannot communicate with server: timeout exceeded while waiting for response"

After that, the virtualbox crashed.



Helpful websites for this task:

https://docs.cloudera.com/HDPDocuments/DAS/DAS-1.4.4/installation/content/das_configure_postgres_ubuntu.html

https://jfrog.com/knowledge-base/a-beginners-guide-to-understanding-and-building-docker-images/#:~:text=A%20Docker%20image%20is%20a,publicly%20with%20other%20Docker%20users

https://www.pgadmin.org/download/pgadmin-4-python/

#### 3.

To find what datatypes of each object in bitcoin.csv we run (pandas is required):

```sh
python3 df.dtypes
```

Output is as follows:

| Variable | Type in Python| Type in PostgresSQL (precision, scale)|
| --- | --- | --- |
| Timestamp |   int64  | NUMERIC(10)
| Open |  float64   | NUMERIC
| High |  float64   | NUMERIC
| Low |   float64  | NUMERIC
| Close |   float64  | NUMERIC
| Volume_(BTC)  |float64     | NUMERIC
| Volume_(Currency) |   float64  | NUMERIC
| Weighted_Price  |   float64  | NUMERIC
| date |  datetime64   | ISO 8601
| dtype |  object   |

PostgresSQL does not support any 64-byte integers or floats (int64, float64) according to https://www.postgresql.org/docs/12/datatype-numeric.html#DATATYPE-INT. This leaves us with the following option to structure our database. Change the float64 and int64 to NUMERIC. However, this will slow down calculations comapred to PostgresSQL int-types. Nevertheless, the calculations are more precise and recommended for monetary amounts. This trade-off between precision and time needs to be observed in real-time. The int64 could technically be converted to int8 in python (with the numpy package) but this cuts down the possible range of values from -128 to 127 (see https://numpy.org/doc/stable/user/basics.types.html). This would be possible for the "Volume_(BTC)" variable but not for the others. We therefore stick to NUMERIC for now. Also, we want to keep the option of a larger precision (total amount of numbers for a given observation) and scale (numbers after the decimal points). This is mostly for the float-variables which would give us closer predictions of our Rnn-Model. The timestamp variable is an int with a precision of 10, so int8 is not an option without major transformations. We refrain from using the direct money type since there could arise problems when classifying BTC as a currency. To change the datatype of the "Date" variable from object to datetime, we implemented the following line to "loading_and_preparing_data.py":

```sh
df['date'] = df['date'].astype('datetime64[ns]')
```

To find the largest and lowest numbers for each variable, we run:

```sh
python3 df.max()
python3 df.min()
```
This reveals:

| Variable | Max| Min|
| --- | --- | ---|
| Timestamp | 1421421480    | 1417411980
| Open |  398   | 109.87
| High |  398   | 109.94
| Low |   398  | 109.87
| Close |   398  | 109.94
| Volume_(BTC)  |5.2     | 0.01
| Volume_(Currency) |   1965.6  | 1.0994
| Weighted_Price  |   398  | 109.94
| date |  2015-01-16   | 2014-12-01
| dtype |  object   | object
