# User-Contents

User Contents

### Tools and Package Required

1. Python3
2. Django
3. pip3
4. graphene-django

### Setup Instructions -

1. Clone repository: git clone https://github.com/Shubham1007/User-Contents.git
2. Activate virtual environment: source env/bin/activate
3. Install library in python:  pip install -r requirements.txt
3. For database models make migrations and migrate: python manage.py makemigrations and python manage.py migrate
4. Load UserContents sample data: python manage.py loaddata contents
5. Run server: python manage.py runserver

### Query Requests-

Goto graphql url: http://127.0.0.1:8000/graphql/
and make requests:-

Examples: GET Query in graphql for fetching data.

1. For fetching user contents data using id enter below graphql query -

```
{
  user(id:"2"){
  	contents
    {
      id:id
     	createdAt
      contentData
    }
  }
}
```

2. For fetching Only specific content data using content id -

```

{
  content(id:"1"){
    createdAt,
    contentData,
    user{
      id,
      details
    }
  }
}
```