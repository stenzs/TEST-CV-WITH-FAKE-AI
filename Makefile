docker-up:
	docker-compose -f docker-compose.yml up cv_test ;


docker-down:
	docker-compose -f docker-compose.yml down --volumes --rmi all ;
