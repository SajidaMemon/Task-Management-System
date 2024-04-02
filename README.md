# Task Management System

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


