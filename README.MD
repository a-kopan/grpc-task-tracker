# gRPC Task Tracker

**A minimalist Python task tracker demonstrating gRPC (Unary RPCs), Protocol Buffers, and local SQLite persistence with SQLAlchemy.**

**Topics/Tags:** `python`, `grpc`, `sqlalchemy`, `protobuf`, `microservice`, `sqlite`, `tutorial`


## Features

* **gRPC Server & Client:** Demonstrates strict API contracts using Protocol Buffers (`proto3`).
* **Unary RPCs:** Implements standard Create, Read, and List operations.
* **SQLAlchemy ORM:** Maps Protobuf messages directly to database rows using Python's leading ORM.
* **Local SQLite Persistence:** Zero-infrastructure database setup with proper session and transaction management.

## Project Structure

* `task.proto`: The Protocol Buffer contract defining the `TaskManager` service and request/response messages.
* `db.py`: The database layer handling the SQLite connection engine, SQLAlchemy models, and CRUD queries.
* `server.py`: The gRPC server that listens on port `50051`, receives client requests, interacts with the database, and returns Protobuf objects.
* `client.py`: The gRPC client that uses a local stub to send requests (Create, Get, List) to the server.

## Setup & Installation
1. Clone the repository
2. Compile the Protocol Buffers
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. task.proto
```

## Usage - run from project root folder
1. Start the server
```bash
python src/server.py
```
2. Run the Client
```bash
python src/client.py
```
