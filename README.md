# Random UUID generator

### About the project
> On page reload, a random UUID is added to the JSON list of generated UUID with the timestamp of when they were generated as the key 

### How to Run the Program

1. Download and Install [Python 3](https://www.python.org/)
2. Install requirements
```
pip install django
pip install django-restframework
```
3. Run the server
```
python manage.py runserver
```
4. Finally, Visit this page on your browser to see all the generated UUID
```
http://localhost:8000/api/
```

### Structure of JSON output 
```
{
  "2021-05-24 17:13:39.153571": "1efa1dd5-7d79-41aa-840d-3ff586e7d000",
  "2021-05-24 14:13:32.498564": "951fc27a-3d3d-4a6e-9412-3b8750693a9a",
  "2021-05-24 14:12:25.987911": "8610541f-13d2-41d4-b519-df14e8a802fc"
}
```

