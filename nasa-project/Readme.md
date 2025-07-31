# 🚀 NASA Project

Простой pet-проект, который показывает данные с NASA API через веб-интерфейс.  
Состоит из двух сервисов:

- **Backend** — Python-приложение на Flask (`backend/app.py`)
- **Frontend** — простой HTML-интерфейс (`frontend/index.html`)

Оба сервиса работают в отдельных контейнерах и запускаются с помощью Docker Compose.

---

## 📦 Используемые технологии

- Python 3 + Flask
- HTML/CSS
- Docker
- Docker Compose

---

## 🚀 Как запустить

1. Клонируйте репозиторий:
```bash
git clone https://github.com/krutikov-v/devops-pet.git
cd devops-pet

2. Запустите контейнеры:
docker compose up --build

3. Откройте в браузере:

Frontend: http://localhost:8080

Backend API: http://localhost:5000

Структура проекта

nasa-project/
├── backend/
│   ├── app.py               # Основной код API
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── index.html           # Интерфейс
│   └── Dockerfile
├── docker-compose.yml       # Сборка и запуск двух сервисов
└── README.md
Что планируется дальше
✅ Автоматизация через GitHub Actions (CI/CD)

🔜 Мониторинг через Prometheus + Grafana

🔜 Деплой на VPS через Terraform или Ansible
