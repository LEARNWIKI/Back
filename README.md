# Deployment
Без nginx
```bash
# Склонируйте репозиторий
git clone https://github.com/LEARNWIKI/learnwiki_backend
cd learnwiki_backend

# Установите зависимости
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install

# Мигрируйте и протестируйте
cd learnwiki
python manage.py makemigrations
python manage.py migrate
python manage.py test

# Запустите
python3 manage.py runserver localhost:9999
```

# Зависимости
``` python
python = "^3.8"
Django = "^3.2.6"
loguru = "^0.5.3"
```

# TODO
- [ ] починить cors
- [ ] добавить X и Y
- [ ] добавить авторизацию
- [ ] добавить аутентификацию
- [X] нормальный url давать в графе url
- [ ] выдавать айдишники