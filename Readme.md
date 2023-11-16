# Package By Layer Vs Package By Feature Reference
[Reference](https://medium.com/sahibinden-technology/package-by-layer-vs-package-by-feature-7e89cde2ae3a)


# Setup Before Run
>flask shell

> from app import db

> db.create_all()

> exit()


# Run
> flask run

# Issue with Running With Sqlite
https://github.com/mrkipling/maraschino/blob/master/lib/flaskext/sqlalchemy.py
"info.database = os.path.join(app.root_path, info.database)"