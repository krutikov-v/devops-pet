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
```

2. Запустите контейнеры:
```bash
docker compose up --build
```
4. Откройте в браузере:

Frontend: http://localhost:8080

Backend API: http://localhost:5000

Структура проекта
```bash
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
```

5. 🔄 Автоматизация с GitHub Actions
Проект использует CI/CD пайплайн (.github/workflows/deploy.yml), который:

Устанавливает Python 3.11

Устанавливает зависимости из requirements.txt

Запускает Flask-приложение и проверяет доступность API (/api/health)

При успешном прохождении теста автоматически деплоит проект на AWS EC2 через SSH

CI/CD запускается автоматически при пуше в ветку main.

Что реализовано сейчас
📦 Backend и frontend в Docker-контейнерах

📡 Мониторинг backend через Prometheus

📊 Grafana, подключённая к Prometheus

☁️ Автодеплой на AWS EC2 через GitHub Actions

Что планируется дальше
🔍 Расширить метрики backend (кастомные метрики NASA API)

🖥️ Мониторинг сервера через Node Exporter

📈 Создание дашбордов в Grafana

⚙️ Автоматизация инфраструктуры через Terraform или Ansible
