## SetUp
- clone or download this project
- pipenv shell
- pipenv install --dev
- manage.py runserver

## Bug 1 fix
- running pipenv install --dev gives an error :(
- you need to read and understand the error as much as possible
- then you need to track and fix this bug

## Bug 2 fix
- When you run `manage.py runserver`
- There are lots of unapplied migrations in red
- we need to fix this by running a migration

## Bug 3 fix

- After the bug 1 and 2 are fixed
- visiting http://127.0.0.1:8000/admin/
- gives a page not found (404)
- please fix it so we can see the admin login page