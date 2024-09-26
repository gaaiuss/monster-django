# Monster Hunter Django Project

Just a django project for study goal

## Done

- created the virtual environment (python -m venv env_name)
- activate the venv (activate.ps1 for VS code)
- install Django from requirements.txt
- started a django project (django-admin startproject project_name .)
- chaged basic settings
- standard database sqlite setup (python manage.py migrate)
- started web server (manage.py runserver) hosted on http://127.0.0.1:8000/
- created a separated application for blog (startapp blog)
- added blog to the settings (installed apps)
- created the Post class in blog models
- added blog model to the database (python manage.py makemigrations blog) and applied the migration (python manage.py migrate blog)
- registered post in admin.py
- created superuser to login django admin
- tested the post funcionality
- deployed on pythonanywhere.com
- created API token
- opened the bash console and installed pythonanywhere (pip3.10 install --user pythonanywhere)
- cloned the git repo (pa_autoconfigure_django.py --python=3.10 "git clone url")
- created superuser
- site live! (https://gaiusc.pythonanywhere.com/)
- added blog.urls to the site urls.py path
- created blog.urls.py
- got an error (AttributeError: module 'blog.views' has no attribute 'post_list') because view its not configured