# 🚀 Task Manager API 

A flexible Django REST API for managing tasks with customizable fields. Perfect for building your next productivity app!  

![Django REST](https://img.shields.io/badge/Django-REST-44B78B?style=flat&logo=django)  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql)  
![JWT Auth](https://img.shields.io/badge/JWT-Auth-000000?style=flat&logo=jsonwebtokens)

## ✨ Features

- **JWT Authentication** 🔒  
  Secure user registration/login with refresh tokens
- **Flexible Tasks** 🎨  
  Core fields + unlimited custom JSON data
- **Soft Deletion** ♻️  
  `deleted_at` field for easy recovery
- **Ready for Docker** 🐳  
  Includes PostgreSQL and Redis configurations

## 🛠️ Setup (1-2-3!)

### Prerequisites
- Docker & Docker Compose
- Python 3.9+

### Installation
```bash
git clone https://github.com/your-repo/task-manager.git
cd task-manager
```

### Configure Environment
Rename `.env.example` to `.env` and update:
```ini
# PostgreSQL
POSTGRES_USER=django
POSTGRES_PASSWORD=secret

# Django
SECRET_KEY=your-random-key-here
DEBUG=True
```

### Start Services
```bash
docker compose up -d
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/auth/register/` | POST | Create new user |
| `/api/auth/login/` | POST | Get JWT tokens |
| `/api/tasks/` | GET | List your tasks |
| `/api/tasks/` | POST | Create new task |

**Example Request**:
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn Docker","custom_fields":{"priority":"high"}}'
```

## 🧑‍💻 Development Tips

### Access Admin Panel
1. Create superuser:
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```
2. Visit `http://localhost:8000/admin`

### Check Database
```bash
docker compose exec db psql -U django -c "SELECT * FROM app_task;"
```

### Run Tests
```bash
docker compose exec web python manage.py test
```

## 🌱 Customizing Tasks

Add fields to `app/models.py`:
```python
class Task(models.Model):
    # Core fields
    title = models.CharField(max_length=200)
    # Add your customizations here!
    due_date = models.DateField(null=True, blank=True)
```

Then regenerate migrations:
```bash
docker compose exec web python manage.py makemigrations
```

## 🤝 Contributing

Found a bug? Want a feature?  
1. Fork the repo  
2. Create a branch (`git checkout -b cool-feature`)  
3. Commit changes  
4. Push to branch  
5. Open a PR!

---

Made with ❤️ and Django  
✨ **Pro Tip**: Use `custom_fields` for rapid prototyping!