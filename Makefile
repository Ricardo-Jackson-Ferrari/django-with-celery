## @ system
.PHONY: run
run: ## run the system
	@poetry run docker-compose up --build -V -d
stop: ## stop the system
	@poetry run docker-compose down

## @ build
superuser: ## create superuser for django admin access
	@poetry run docker-compose exec app python manage.py createsuperuser