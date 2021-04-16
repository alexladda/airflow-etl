# installation notes airflow

## set up nginx

`/etc/nginx/sites-available/airflow`

`server {
       listen 80;

       location /airflow/ {
              proxy_pass http://localhost:8080;
              proxy_set_header Host $host;
              proxy_redirect off;
              proxy_http_version 1.1;
              proxy_set_header Upgrade $http_upgrade;
              proxy_set_header Connection "upgrade";
       }
}`

## OS dependencies

`sudo apt-get install -y --no-install-recommends \
        freetds-bin \
        krb5-user \
        ldap-utils \
        libsasl2-2 \
        libsasl2-modules \
        libssl1.1 \
        locales  \
        lsb-release \
        sasl2-bin \
        sqlite3 \
        unixodbc`


## Install script with constraints

(in venv)

AIRFLOW_VERSION=2.0.1
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

## Initialise airflow

`$ airflow` -> creates files

`$ airflow db init` -> initialises database

`$ airflow users create --username alex --firstname Alex --lastname Ladda --role Admin --email alex.ladda@gmail.com --password <password> `
