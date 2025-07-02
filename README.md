# SOFTDSNL - Activity 1: Python API Basics and Sci-kit Learn

## 🚀 Goals

- Understand how to set up a basic API using **Django Rest Framework**.
- Learn how to use **Scikit-Learn** to create a simple machine learning model.
- Deploy a basic API endpoint that accepts input and returns predictions.

---

## 🧠 What You'll Build

A simple API that predicts whether a flower is **Setosa**, **Versicolor**, or **Virginica** using the famous **Iris dataset**.

---

## 🔧 Requirements

- Python 3.10 or higher
- Basic understanding of Python
- Basic terminal/command line skills

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/godwyn20/softdsnl-act1.git
cd softdsnl-act1
```

### 2. Create and activate a Virtual Environment (Skip this step if using HAU Lab PC. PC restrictions prevent creating VENV)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django djangorestframework scikit-learn
```

---

## Project Structure

```
ml_api_project/
├── ml_api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py          
│   └── urls.py         
├── ml_api_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py 
│   └── wsgi.py
├── manage.py
```

---


### 4. Run the Server

```bash
python manage.py runserver
```

The API will be accessible at:

```
http://127.0.0.1:8000/api/predict/
```

---

## 🔥 How to Test the API

You can use tools like **Postman**, **Insomnia**, or simply `curl`.

### Example Request

**POST** to:

```
http://127.0.0.1:8000/api/predict/
```

**Request Body (JSON):**

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Example Response

```json
{
  "prediction": "setosa"
}
```

---

## 🎯 Your Task

- Follow the steps to create the API.
- Test it with 10 different flower measurements.
- For each measurement, screenshot and provide the following:
  - The API URL
  - The request body
  - The response
- Organize the results in your report and pass it via Canvas. 

---

## 📚 Useful Resources

- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)
- [Iris Dataset Info](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)




