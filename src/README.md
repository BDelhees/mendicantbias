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

7. To access the "ms3_jokes" database via Python script called ***jokes.py***, we used the ***pyscopg2*** package we installed on step 4.

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

We were not able to create the table since for some reason we were not able to reconnect to docker and we tried several approaches, as well as re-running the above code. The error messages varied and tried to find solutions online, but this led us down one rabbit-hole after another with no avail.



***Encountered Problems:***

When I tried to install the Docker engine on my Virtualbox.
When trying to install docker engine via https://docs.docker.com/engine/install/ubuntu/, while trying to remove old docker affiliated files, I got the following error message:

"Reading packages lists... Error! Write error- write (28: No space left on device)"

I then ran the following command to see if my space is full:

```sh
df -h
```
And indeed, it turns out that the several filesystems (all /dev/loop and /cow) are at 100% capacity.



While trying to download the Docker image from the official Docker hub page, with:

```sh
sudo snap install docker
```
and,

```sh
docker pull postgres
```
I encountered the following message:

"error: cannot communicate with server: timeout exceeded while waiting for response"

After that, the virtualbox crashed. I have not found a solution to this without setting up the Virtualbox from scratch. Even when setting up the Virtualbox from scratch and follwing the aboce commands, I get to the same point and disk space is still full, keeping me from further implementing the above steps.


When we first tried to run docker, our access was usually denied. We tried to use the following four commands:

```sh
sudo groupadd docker
```

```sh
sudo usermod -aG docker ${USER}
```

```sh
su -s ${USER}
```

```sh
docker run hello-world
```


***Helpful websites for this task:***

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


To create a database with our ***bitcoin.csv*** file, we would follow the same steps as in Task 2. Since we do not have images as our data (see data structure abvoe), minimal changes would have to be made to save them PostgreSQL compliant in a databse. However, we got stuck on the same issue as mentioned at the end of Task 2 and could not proceed due to these reasons.

We envision the following database structure (when we have sorted out the issues above and get this far):




#### 4.

The goal is to create a Multi-Docker Application. Essentially, we need to have a database running and thus tables based on the ***bitcoin.csv*** file and the predicitons from our Rnn-Model, which has been partitioned/modularized into several ***.py*** files. This means we have to dockerize our code as well as our data input.

Create a docker-compose.yml file which:

1. Starts a PostgreSQL Server Docker container (version 12.4). It should use a Docker volume to persist your data, even after your Docker container was stopped and deleted.

We created a docker compose file, called ***docker-compose.yml***, which keeps the data even after the docker container is deleted or stopped. To do this, we copied and modified a code as such:

```sh
version: "3.8"

services:

  postgres_service:
   container_name: postgresql_container
   restart: always
   image: postgres:12.4
   volumes:
     - postgres-data:/var/lib/postgresql/data
     - ./postgresql/init:/docker-entrypoint-initdb.d
   ports:
     - "5432:5432"
   environment:
     - POSTGRES_USER=admin
     - POSTGRES_PASSWORD=password
volumes:
  postgres-data:
    driver: local
```

We are unsure if that is the correct approach or if we are miles off.


2. Executes a Python Script in another (!) Docker container, which connects to the your database (you'll have to write a Dockerfile for this). This script should do the following taks:

2.1. Initialize database from previous task and add two tables "input_data" and "predictions":

We failed to start the container due to the same raesons outlined in the end of Task 2&3. Further, we were not able to properly debug our Rnn-model code. The code does not execute or deliver any proper predictions. We have spent a considerable amount of time troubleshooting (also in spyder) this but we were not able to solve it. We will try again in the coming weeks, since without predictions, our future app is useless.

2.2 Load your trained Neural Network (.h5) file:

We were not able to create a ***.h5*** file for milestone2. Sadly, we were not able to produce one for this milestone either.

2.3 Load a sample from the data set:

See answer for 2.1&2

2.4 Save this single sample to the database:

See answer for 2.1&2

2.5 Load the sample again from the database

See answer for 2.1&2

2.6 Call your predict function:

See answer for 2.1&2

2.7 Save the prediction result to the database

See answer for 2.1&2



3. Explain to us how you chose to structure your database and what tables do you have, what attributes do they have?

Since we are working with PostgreSQL, we would adpot a SQL compliant relational database. This works well with our structured Bitcoin pricing data. However, since our dataset only consists of one table with roughly 10k rows and 7 variables, it would not make sense to partition this any further. We would link the datetime (created out of timestamp) variable as the id, any other variables would not make much sense. With the date as id, we could select specific days and split the data into training and test set accordingly. The database would not have any connections to other tables since we do not have any further data. The only possible case would be prediction data which coul potentially be saved in another table. In this case a seperate table would be created and linked to the existing datatable with the id which would lead to problems (we would have to choose how many datapoints/dates the Rnn-model would use to make price movement predictions, but then we could not just append it with a new id since they would be the same as in the training set which would convolute and interefere with the bitcoin/training set, therefore a seperate table would not make much sense unless for comparison purposes of training/test sets). The database would look as follows:

| Database |  |
| --- | --- |
| id | Int(8) |
| date | ISO 8601
| Timestamp | NUMERIC(10)
| Open | NUMERIC
| High |  NUMERIC
| Low | NUMERIC
| Close |  NUMERIC
| Volume_(BTC)  | NUMERIC
| Volume_(Currency) | NUMERIC
| Weighted_Price  |  NUMERIC




***Encountered Problems:***

Same problem as Task 2 and Task 3, unable to connect to Docker. Overall, we were not able to do a lot in this task since we failed on some major points in the previous tasks.



***Helpful Websites for this task:***

https://docs.docker.com/compose/compose-file/

https://linuxhint.com/run_postgresql_docker_compose/

https://reasonabledeviations.com/2018/02/01/stock-price-database/#database-schema

We chose to keep our structure with the folders intact for this milestone since it is too risky to restructure our whole github on the eve of the delivery deadline of milestone3. For the next milestone, we will restrucutre our repository to the structure outlined by Arthur on the 12.11.2020. 
