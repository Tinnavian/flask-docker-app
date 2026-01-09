# Flask Docker App

![CI/CD Status](https://github.com/Tinnavian/flask-docker-app/workflows/Docker%20Build%20and%20Test/badge.svg)

Простое Flask-приложение с Docker и CI/CD pipeline.

## Возможности

- ✅ Контейнеризация с Docker
- ✅ Автоматическая сборка и тестирование
- ✅ Health check endpoint
- ✅ CI/CD с GitHub Actions

## Быстрый старт

### Запуск локально с Docker

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
