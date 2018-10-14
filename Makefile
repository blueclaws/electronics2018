#run the project.
run:
	sudo docker run --name db -e MYSQL_ROOT_PASSWORD=moot -v /home/claw/Docker/electronics-website/sql:/var/lib/mysql -d mariadb:10
	sudo docker run --name project_site --link db -it -p 8000:80 elec

#compile the project.
build:
	sudo docker build -t elec .

#run just the sql instance.
dsql:
	sudo docker run --name db -e MYSQL_ROOT_PASSWORD=moot -v /home/claw/Docker/electronics-website/sql:/var/lib/mysql -d mariadb:10	

#kill just the sql instance.
csql:
	sudo docker container stop db
	sudo docker container rm db

	
#kill the project.
clean:
	sudo docker container stop project_site
	sudo docker container rm project_site
	sudo docker container stop db
	sudo docker container rm db

