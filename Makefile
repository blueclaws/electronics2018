run:
	sudo docker run --name db -e MYSQL_ROOT_PASSWORD=moot --mount type=volume,source=sqlshit,dst=/var/lib/mysql -d mariadb:10
	sudo docker run --name project_site --link db -it -p 8000:80 elec

build:
	sudo docker build -t elec .

sql:
	sudo docker run --name db -e MYSQL_ROOT_PASSWORD=moot --mount type=volume,source=sqlshit,dst=/var/lib/mysql -d mariadb:10	

clean:
	sudo docker container stop project_site
	sudo docker container rm project_site
	sudo docker container stop db
	sudo docker container rm db

csql:
	sudo docker container stop db
	sudo docker container rm db
	
