# Hotel Booking
## Intro
This is an application where you can display, add, update, and delete bookings/clients using **Django** and **Bootstrap**.
## What you need beforehand:
- Install [Python](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwiryNTbmMnnAhWB3eAKHRwoCtEQFjAAegQICBAC&url=https%3A%2F%2Fwww.python.org%2Fdownloads%2F&usg=AOvVaw3VuYRIaaa-SL5nRa6pfny0).
- It is better to create a [virtual](https://docs.python.org/3/library/venv.html) environment.
- Then install [Django](https://www.djangoproject.com/download/).
## How to run the project
- In you code editor's terminal run the following:
1. Navigate into the project's directory `cd hotel_project`.
2. Migrate the database `python manage.py migrate` and `python manage.py makemigrations hotel_app`.
3. Create a  super user to access the Django admin interface
 `python manage.py createsuperuser`.
4.  Run the project 
`python manage.py runserver`.
5. Type [http://localhost:8000](http://localhost:8000) into your browser's address bar and hit enter.
