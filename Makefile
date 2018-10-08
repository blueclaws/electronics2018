build:
	docker run --name db -e MYSQL_ROOT_PASSWORD=moot -d mariadb:10
	sudo docker run --name project_site --link db -it -p 8000:80 elec

clean:
	sudo docker container stop project_site
	sudo docker container rm project_site
	sudo docker container stop db
	sudo docker container rm db
