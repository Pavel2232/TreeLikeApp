# ✏️🗒🌳 приложение для управления древовидной структурой страниц на Python, используя Django и DRF | TreeLikeApp | Python, Django, PostgresSQL, DRF, Docker, Nginx


## Суть приложения

Требуется сделать древовидную структуру страниц неограниченного уровня вложенности, например:

````ecmascript 6
├── Главная страница (slug: "", url: "/")
├── О компании (slug: "about", url: "/about/")
│   ├── Реквизиты (slug: "req", url: "/about/req/")
│   └── Контакты (slug: "contacts", url: "/about/contacts/")
└── Каталог (slug: "catalog", url: "/catalog/")
    ├── Обувь (slug: "shoes", url: "/catalog/shoes/")
    │   ├── Тапки (slug: "slipper", url: "/catalog/shoes/slipper/")
    │   └── Сандали (slug: "sandals", url: "/catalog/shoes/sandals/")
    └── Одежда (slug: "clothes", url: "/catalog/clothes/")
        ├── Штаны (slug: "pants", url: "/catalog/clothes/pants/")
        └── Кофты (slug: "sweatshirts", url: "/catalog/clothes/sweatshirts/")
````


## Управление страницами

Управление страницами осуществляется в панели управления. Можно использовать стандартный интерфейс Django Admin.

### Возможности панели управления:

- Добавление страницы
- Редактирование страницы
- Удаление страницы

### Атрибуты страницы:

- **name**: Название страницы
- **slug**: Фрагмент URL-адреса
- **url**: Полный URL-адрес

> ⚠️ В панели управления для страницы указывается только фрагмент URL-адреса. Полный URL страницы вычисляется конкатенацией фрагментов URL всех родителей и самой страницы, используя слеш.

- **parent**: Родительская страница

Также требуется реализовать REST API (используя Django REST Framework) для получения страницы и её потомков (полное дерево) по полному URL.ё
Например 
```http request
GET /api/pages/?url=/catalog/
```
```json
{
    "name": "Каталог",
    "slug": "catalog",
    "url": "/catalog/",
    "children": [
        {
            "name": "Обувь",
            "slug": "shoes",
            "url": "/catalog/shoes/",
            "children": [
                {
                    "name": "Тапки",
                    "slug": "slipper",
                    "url": "/catalog/shoes/slipper/",
                    "children": []
                },
                {
                    "name": "Сандали",
                    "slug": "sandals",
                    "url": "/catalog/shoes/sandals/",
                    "children": []
                }
            ]
        },
        {
            "name": "Одежда",
            "slug": "clothes",
            "url": "/catalog/clothes/",
            "children": [
                {
                    "name": "Штаны",
                    "slug": "pants",
                    "url": "/catalog/clothes/pants/",
                    "children": []
                },
                {
                    "name": "Кофты",
                    "slug": "sweatshirts",
                    "url": "/catalog/clothes/sweatshirts/",
                    "children": []
                }
            ]
        }
    ]
}
```

## Как запустить
* склонируйте репозиторий ``` git clone https://github.com/Pavel2232/TreeLikeApp  ```
* создайте виртуальное окружение проекта ```poetry shell ```
* установите зависимости проекта ```poetry install ```
* заполните .env по аналогии с [.env.example](.env.example)
* выполните ```python manage.py makemigrations```
* выполните ```python manage.py migrate```
* по желанию можете загрузить тестовые данные ```python manage.py loaddata db.json```
* выполните ```python manage.py runserver```

## Как запустить через Docker
* склонируйте репозиторий ``` git clone https://github.com/Pavel2232/TreeLikeApp  ```
* заполните .env по аналогии с [.env.example](.env.example)
* выполните ```docker compose up -d ```
* сервер будет доступен по адресу ```http://localhost/```

