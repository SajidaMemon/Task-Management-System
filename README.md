# Task Management System
# Project Setup and run locally

- `Step-1:` Create Virtual Environment. `python3 -m venv env` and Active environment `source env/bin/activate`

- `Step-2:` Install necessary packages from requirements.txt. `pip install -r requirements.txt`

- `Step-3:` Run the server locally. `python manage.py runserver`



admin login: http://127.0.0.1:8000/admin
# Admin Credentials:
`User-1:`

`username:` admin

`password:` admin

`User-2:`

`username:` saji

`password:` saji


# How I created this project (Step by Step)

- `Step1:` Create a folder and open in editor like vscode

- `Step2:` create virtual environment ----- > `python3 -m venv env`

- `Step3:` activate Virtual enviroment --> `source env/bin/activate`

- `Step 4:` install django --> `pip install django`

- `Step5:` create django project --> `django-admin startproject projectfile . `

- `Step6:` run the server ---> `python3 manage.py runserver`

- `Step7:` Create app named 'task' : `python3 manage.py startapp tasks`

- `Step 8:` Installed new app named `tasks` in `settings.py` on `INSTALLED_APP`

- `Step 9:` Create new urls.py file in tasks app

- `Step 10:` Make pipeline between `projectfile.urls` and `tasks.urls` using `include` library `path('', include('tasks.urls')),`

- `Step 11:` Define the main url on index function. `path('', views.index, name="name")`

- `Step 12:` Create index function in views.py.

- `Step 13:` Make templates folder in tasks app and create `index.html` file in that folder. render this index.html file on index function.

- `Step 14:` Do makemigrations and migrate, then createsuperuser to login to admin penal:

  `python3 manage.py makemigrations`

`python3 manage.py migrate`

`python3 manage.py createsuperuser`

`username: admin`

`password: admin`

- `Step 15:` create a model named `Label` and then makemigrations and migrate. after that register this class on admin.py. owner is OnetoOneField so that there will be no duplicate record.

- `Step 16:` create model named `task` and add many to many fields and then makemigrations and migrate.

# Label APi Creation:

- `Step 1:` installed djangorestframework
- `Step 2:` add rest_framework in settings installed apps
- `Step 3:` in urls.py import DefaultRouter and registered path with classes. and include the router on api path. `router.register(r'labels', views.LabelView)`
- `Step 4:` created the class LabelView. add queryset the label table
- `Step 5:` created serializers class for Label named labelserializers and mensioned as serializers_class in labelview.

# Task Api Creation

- `Step 1:` add task path in urls and allocate the a class named `TaskView` `router.register(r'tasks' , views.TaskView)`
- `Step 2:` create class TaskView ,add queryset the task table.
- `Step 3:` creted serlializers class for task table named TaskSerializer mension as serializers_class in TaskView.
