# FastAPI with SQLAlchemy Tutorial

Code for my video tutorial [FastAPI with SQLAlchemy Tutorial](https://youtu.be/8GSYx-KDEas)

## What is FastAPI?

FastAPI is a high-performant REST API framework for Python. It's built on top of 
[Starlette](https://www.starlette.io/) and it uses [Pydantic](https://pydantic-docs.helpmanual.io/) 
for data validation. It can generate OpenAPI documentation from your code and also produces 
a Swagger UI that you can use to test your application.

Check out FastAPI's GitHub [repository](https://github.com/tiangolo/fastapi) and give it a 
star! Also make sure to check out its excellent [documentation](https://fastapi.tiangolo.com/) online.

## What are SQLAlchemy and Alembic?

* *SQLAlchemy* is Python's most popular Object Relational Mapper (ORM). ORMs are frameworks that offer an 
object-oriented interface to your database tables. ORMs give you a layer of abstraction on top of SQL, so 
you don't have to write SQL queries by hand - instead, you just write code. ORMs also abstract away the 
differences between SQL engines, such as PostgreSQL and MySQL, so you can switch between one and the other 
without having to change your code. You can learn more about SQLAlchemy with its official documentation: 
https://www.sqlalchemy.org/.

* *Alembic* is a database migrations management framework. Alembic ensures that your database schemas 
accurately reflect the data models that you define with SQLAlchemy. You can learn more about Alembic with 
its official documentation: https://alembic.sqlalchemy.org/en/latest/


