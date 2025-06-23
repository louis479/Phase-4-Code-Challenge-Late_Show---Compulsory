# Phase-4-Code-Challenge-Late_Show---Compulsory

## Late Show Flask API

### Overview

The **Late Show Flask API** is a RESTful API built using **Flask** and **Flask-SQLAlchemy** to manage TV show episodes, guests, and their appearances. It allows users to retrieve information about episodes, guests, and create relationships between guests and episodes with their respective appearance details.

---

### Features

- Retrieve a list of episodes
- Get details of a specific episode
- Retrieve a list of guests
- Create a new appearance of a guest on an episode

---

### Technologies Used

- **Python** (Flask, Flask-SQLAlchemy, Flask-Migrate)
- **SQLite** (for database management)
- **Postman or curl** (for API testing)

---

## Setup & Installation

### **1.Clone the Repository**

```sh
git clone Code-challenge
cd Phase-4-Code-Challenge-Late_Show---Compulsory
```

### **2. Create and Activate a Virtual Environment Using Pipenv**

```sh
pipenv install
pipenv shell
```

### **3. Install Dependencies**

```sh
pipenv install --dev
```

### **4. Set the Environment Variables**

Before running the application, set the following environment variables:

```sh
export FLASK_APP=app.py
export FLASK_RUN_PORT=5555
```

### **5. Set Up Database Migrations**

```sh
flask db init  
flask db migrate -m "Initial migration"
flask db upgrade
```

### **6. Run the Flask App**

```sh
flask run
By default, the app runs on http://127.0.0.1:5555/.
```

## API Endpoints

### **Base Endpoint**

```sh
GET / → Returns a welcome message
```

### **Episodes**

```sh
GET /episodes → Get a list of all episodes

GET /episodes/<id> → Get a specific episode by ID
```

### Guests

```sh
GET /guests → Get a list of all guests
```

## Appearances

```sh
POST /appearances → Create a new appearance of a guest on an episode (Requires guest_id, episode_id, and appearance_date)
```

Example Requests & Responses

### 1. Get All Episodes

Request:**

GET /episodes
Response:
json

```sh

[
  { "id": 1, "title": "Episode 1", "air_date": "2025-04-01" },
  { "id": 2, "title": "Episode 2", "air_date": "2025-04-02" }
]
```

## 2. Get an Episode by ID

Request:**

```sh

GET /episodes/1
Response:
{ "id": 1, "title": "Episode 1", "air_date": "2025-04-01" }
```

### 3. Create an Appearance

Request:

```sh
POST /appearances
Content-Type: application/json

{
  "guest_id": 1,
  "episode_id": 2,
  "appearance_date": "2025-04-06"
}

Response:

{
  "id": 1,
  "guest_id": 1,
  "episode_id": 2,
  "appearance_date": "2025-04-06"
}
```
