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
  user(id:"VXNlclR5cGU6MQ=="){
  	name
    details
    contents {
        id,
        heading,
        createdAt
        contentData
      }
  }
}
```

2. For fetching Only specific content data using content id -

```

{
  content(id:"Q29udGVudFR5cGU6Mg=="){
    id: id
    contentData
    createdAt
    heading
	}
}
```

3. For fetching all users data using filters -

```

{
  allUsers(first:3){
  	edges{
      node{
        details
        id
      }
    }
  }
}

```

4. For fetching all user contents data using filters -

```
{
  userContents(offset:4,last:2){
    edges{
      node{
        contentData
        heading
        createdAt
        id
        user{
          id
          details
        }
    }
  }
}
}

```