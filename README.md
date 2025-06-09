# radis-server 🔴

A simple Python server using Redis for caching and pub/sub messaging.

## Project Structure

radis-server/
├── app/
│   ├── __init__.py
│   ├── server.py
│   └── routes.py
├── tests/
│   ├── test_server.py
│   └── test_routes.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md


## Features

- Caches key/value pairs in Redis
- Publishes/subscribes to channels for real-time updates
- Dockerized for easy deployment
- Unit-tested

## Tech Stack & Tools

- Python 3.10+
- `redis-py` client library
- Flask (or FastAPI for async) for REST API layer
- Docker & Docker Compose
- pytest for testing

## Installation & Setup

1. Clone repo:
   ```bash
   git clone https://github.com/nambili-samuel/radis-server.git
   cd radis-server
   ```
2. Copy environment variables:
   ```bash
   cp .env.example .env
   ```
3. Build & run with Docker:
   ```bash
   docker-compose up --build
   ```
4. Server runs on `http://localhost:5000`; Redis at default `6379`.

## Usage

### REST Endpoints

| Endpoint                      | Method | Description                          |
|------------------------------|--------|--------------------------------------|
| `/cache/<key>`               | GET    | Retrieve cached value                |
| `/cache/<key>`               | POST   | Set value in cache (`{"value":...}`)|
| `/publish/<channel>`         | POST   | Publish to Redis pub/sub channel     |

### Example

```bash
curl -X POST localhost:5000/cache/foo -d '{"value":"bar"}'
curl localhost:5000/cache/foo
```

## Testing

Run unit tests in `tests/`:

```bash
pytest
```

## requirements.txt

```
Flask==2.2.3
redis==4.6.0
pytest==7.3.1
```

---

*All systems go. *
