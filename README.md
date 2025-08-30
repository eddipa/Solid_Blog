# Solid_Blog

A simple Django blog with posts, accounts, static assets, and media uploads.

> Built with Django. Repo includes `accounts/`, `posts/`, `static/`, and `media/`. There’s also a `bloggg/` app that you can keep or rename to `blog` for clarity.

---

## Quickstart

### 1) Clone & set up environment
```bash
git clone https://github.com/eddipa/Solid_Blog.git
cd Solid_Blog
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install django django-environ whitenoise pillow
```

### 2) Settings split
Create `config/` with `base.py`, `dev.py`, `prod.py` as in this README.  
Set the default:
```bash
export DJANGO_SETTINGS_MODULE=config.dev
```
(Windows PowerShell: `setx DJANGO_SETTINGS_MODULE "config.dev"` then reopen the shell)

### 3) Environment variables
Create a `.env` file at project root:
```bash
SECRET_KEY=replace-this
DEBUG=True
ALLOWED_HOSTS=["localhost","127.0.0.1"]
TIME_ZONE=Europe/Berlin
# DATABASE_URL=postgresql://user:pass@host:5432/dbname
```

### 4) Migrate & run
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput  # safe to run; dev ignores STATIC_ROOT
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## Project structure (suggested)
```
Solid_Blog/
  accounts/
  posts/
  bloggg/            # consider renaming to 'blog'
  static/            # your CSS/JS/images (not collected)
  media/             # user uploads (keep out of git)
  config/
    __init__.py
    base.py
    dev.py
    prod.py
  templates/         # create and add base.html, etc.
  manage.py
```

---

## Development notes

- **Static & media**  
  - `STATIC_URL=/static/`, `STATICFILES_DIRS=["static"]`  
  - `MEDIA_URL=/media/`, `MEDIA_ROOT=media/`  
  - In production, `collectstatic` gathers to `staticfiles/` and WhiteNoise serves them.

- **Apps**  
  - `posts`: your blog posts (add `slug`, `status`, `published_at`, `featured_image`)  
  - `accounts`: auth/profile bits  
  - `bloggg`: legacy or second blog app; you can merge into `posts` or rename to `blog`.

- **Admin**  
  - Prepopulate slugs: `prepopulated_fields={"slug": ("title",)}`  
  - Add list filters for status/date; search by title/body.

---

## Testing & linting (optional but recommended)
```bash
pip install pytest pytest-django ruff black isort
pytest
ruff check .
black --check .
isort --check-only .
```

Add a `.gitignore` if missing:
```gitignore
__pycache__/
*.py[cod]
db.sqlite3
.env
/media/
staticfiles/
.DS_Store
.idea/
.vscode/
```

---

## Deployment (quick sketch)

- **Environment**: `DJANGO_SETTINGS_MODULE=config.prod`, `SECRET_KEY`, `ALLOWED_HOSTS`, `DATABASE_URL` (Postgres recommended).
- **Static**: run `collectstatic` during build.
- **WSGI**: `gunicorn config.wsgi:application`.
- **Reverse proxy**: ensure `X-Forwarded-Proto` so `SECURE_SSL_REDIRECT` behaves.

---

## Roadmap

- Rename `bloggg` → `blog` and standardize URLs to `/blog/<yyyy>/<mm>/<slug>/`.
- Add RSS/Atom feed (`django.contrib.syndication`), sitemap, and meta tags.
- Simple search + pagination with class-based views.
- Optional: `django-taggit` for tags, `Pillow` for images, and an admin thumbnail.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
