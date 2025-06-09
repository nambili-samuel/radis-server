# radis-server 🔴

[![radis-server thumbnail](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3KvfmIBu8C7D5gkX65h4r4GWMpBPKBKtxSdG7iPgnShEty1d6imRk5mgEF4Z8c3Nydt4GeW_wKd5xN5RZDeh8Kg0qzkO4ei1676Hvk6aFdLtw8pWc-df3l1919VrfOI0CwoGK7IInSvNJ7wiFs1UWpJBgfRFdq1O9KGsIhPE_kKBZGlUgLvTL5NeOEGKf/s16000/radis.JPG)](https://github.com/nambili-samuel/radis-server/commit/ecc8f5746e0200a267e3fad8e52f41c93d36dbfd)


If you're developing data-driven applications that demand speed, real-time responsiveness, and scalability, [Redis](https://redis.io/) is an essential tool to have in your stack. Redis is an open-source, in-memory data structure store known for its blazing-fast performance and rich set of features. Whether you're a developer building APIs or a data scientist working on streaming analytics, Redis provides the backbone for modern, low-latency systems.

In the [radis-server](https://github.com/nambili-samuel/radis-server) project, we’ve combined the power of Python with Redis to create a minimal, production-ready server that handles both caching and [pub/sub messaging](https://redis.io/docs/manual/pubsub/). This design is ideal for scenarios where you need to store intermediate computation results, push updates in real-time to subscribers, or manage temporary session data with maximum efficiency.

Redis is not just a cache—it’s also a highly capable [data structure server](https://redis.io/docs/data-types/) that supports strings, hashes, sets, sorted sets, streams, and geospatial indexes. This makes it far more versatile than traditional key-value stores. And with recent additions like [RedisJSON](https://redis.io/docs/interact/json/) and [RediSearch](https://redis.io/docs/interact/search/), Redis has evolved into a fully-featured document and vector query engine—unlocking use cases from chat apps to recommendation engines and even machine learning inference pipelines.

The `radis-server` project uses Python’s Flask framework to expose RESTful endpoints for storing, retrieving, and publishing data via Redis. When running the server, it connects to Redis either locally or via Docker, depending on the setup. Once deployed, you can set key-value pairs, retrieve them instantly, or publish messages to channels for real-time distribution. This simplicity masks the power behind it—Redis handles all the heavy lifting, ensuring data is always available with sub-millisecond latency.

For developers, the ability to interact with Redis through familiar Python constructs and REST endpoints makes integration painless. For data scientists, Redis can serve as a high-speed intermediary for data processing, caching ML model predictions, or maintaining feature stores for inference.

Redis continues to evolve into a real-time, multi-model database with support for [vector similarity search](https://redis.io/docs/interact/search/vector-similarity/)—an increasingly important feature in applications powered by large language models and recommendation systems. Combined with Redis’s ability to persist data to disk and replicate across clusters, it’s clear why Redis remains the go-to choice for high-performance, real-time systems.

If you're interested in exploring this integration further, you can [check out the radis-server codebase](https://github.com/nambili-samuel/radis-server), run it locally with Docker, and experiment with using Redis in your own projects. It’s a clean, modern foundation for building the kind of responsive, intelligent systems that users now expect.

**Redis isn’t just fast—it’s essential.**


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
