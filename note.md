## 快速开始

    pipenv install
    pipenv shell

    # 设置环境变量
    $env:DJANGO_SETTINGS_MODULE="projectsettings.settings.development_sqlite_settings"

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
