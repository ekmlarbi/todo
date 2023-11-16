itest:
	py.test todo/tests

cov:
	py.test --cov-report term-missing --cov todo

lnt:
	flake8 . --exclude __init__.py

tests: lnt itest cov

trun: tests
	gunicorn -b 0.0.0.0:8080 --access-logfile - --reload "todo.app:create_app()"

run:
	gunicorn -b 0.0.0.0:8080 --access-logfile - "todo.app:create_app()"

buildrun:
	docker compose up --build

dcup:
	docker compose up

dcdown:
	docker compose down

dccleanup: dcdown
	docker compose down -v --remove-orphans
	docker compose rm -f
	docker rmi -f $$(docker images -qf dangling=true)

dctest:
	# RUN: docker compose exec website py.test snakeeyes/tests
	#docker-compose exec website snakeeyes
	#docker-compose exec website py.test snakeeyes/tests
	#docker compose exec saas saas test
	docker compose exec todo py.test todo/tests

dccov:
	# RUN: docker compose exec website py.test --cov-report term-missing --cov snakeeyes
	#docker-compose exec website py.test --cov-report term-missing --cov snakeeyes
	#term-missing will provide number for missing coverage lines
	docker compose exec todo snakeeyes cov

dcfl8:
	# RUN: docker compose exec website flake8 .
	#docker-compose exec website flake8 .
	#docker-compose exec website snakeeyes flake8 --help
	#docker-compose exec website snakeeyes flake8 --no-skip-init
	docker compose exec todo flake8 . --exclude __init__.py

db:
	# docker-compose exec website snakeeyes db
	docker compose exec todo db reset --with-testdb

psql:
	docker exec -it todo psql -U todo