# Fenarc

If you want run this local please install the pipenv package and configure

```
$ pipenv install 
$ pipenv shell
```

Configure your database on postgresql

```
createdb database -O youruser
```

Migrate your database with flask migrate, this command will help you migrate your tables on your database

```
flask db upgrade
```

if you want charge data so copy the utils/db/ini.sql to your database

for example:

```
psql -U username -d database -f /tmp/init.sql
```

# With docker 

Now if you want use docker so:

```
docker compose build --no-cache #for build
docker compose up #for up
```

for charge data:

```
docker exec -ti local_postgres /bin/bash
```

so you can execute the following:

```
PGPASSWORD=yourpassword psql -U youruser -d apps -f utils/db/init.sql -h database -p 5432
```


If you want see the documentation use: 

```
localhost:5000/apidocs/
```

The next route for executing:

1. [GET] /process/status/{status} -> /process/status/60/
2. [POST] /process/add/ -> body {"idBulk":1, "retries":2, "status":60, "name":eliezer}
