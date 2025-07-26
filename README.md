# ✅ TODO API – Proyecto Backend Educativo

Este es un proyecto backend educativo desarrollado con **FastAPI** y otras tecnologías modernas. Su propósito es gestionar tareas personales (**TODOs**) por usuario, integrando autenticación segura y un stack profesional. Ideal para aprender desarrollo backend de forma práctica.

---

## 🚀 Características Principales

- 🔐 **Autenticación flexible**:
  - Opción A: GitHub OAuth2
  - Opción B: Email/Contraseña con JWT
- 📝 CRUD completo de tareas TODO
- 📦 Arquitectura en capas: Controller → Service → Repository
- ⚡ Cache de TODOs con Redis
- 🗃️ Base de datos PostgreSQL con SQLAlchemy
- 🐳 Entorno Dockerizado con Docker Compose
- 🔍 Observabilidad con ELK Stack (Elasticsearch, Logstash, Kibana)
- 🧪 Soporte para pruebas y buenas prácticas DevOps

---

## 🧰 Tecnologías Usadas

| Tecnología | Función |
|------------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | Framework web asincrónico y moderno |
| [PostgreSQL](https://www.postgresql.org/) | Base de datos relacional |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM para manejo de modelos |
| [Redis](https://redis.io/) | Caché en memoria |
| [Docker](https://www.docker.com/) | Contenedores para entornos aislados |
| [Docker Compose](https://docs.docker.com/compose/) | Orquestación de servicios |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Manejo de variables de entorno |
| [ELK Stack](https://www.elastic.co/what-is/elk-stack) | Logs y monitoreo |

---

## 🏗️ Arquitectura General

```plaintext
[Frontend o Postman]
       ↓
    FastAPI (Controller)
       ↓
     Service (lógica de negocio)
       ↓
   Repository (ORM SQLAlchemy)
       ↓
 PostgreSQL y Redis
