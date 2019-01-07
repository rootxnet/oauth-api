## OAuth2 API with Django

### Endpoints:

- **Register a new user**  
  POST  /register/  
  *params*: username, password
- **Generate token**  
  POST /o/token/  
  *params*: grant_type=password, username, password   
  *authentication*: client_id, client_secret  
  *response*: access_token
- **Revoke token**  
  POST /o/revoke_token/  
  *params*: access_token  
  *authentication*: client_id, client_secret  
  *response*: message
- **List all comments**  
   GET /comments/  
   *headers*: "Authorization Bearer <access_token>"  
   *response*: list comment objects  
- **Add a comment**
   POST /comments/  
   *headers*: "Authorization Bearer <access_token>"  
   *params*: title, description
   *response*: comment object or error

### How to run application:
1. Clone this repository
2. Create and activate virtual env with Python 3.6
3. Install all dependencies by pip
    > pip install -r requirements.txt
4. Prepare database
    > ./manage.py migrate
5. Create superuser
    > ./manage.py createsuperuser
6. Run API
    >./manage.py runserver
7. Go to admin page and set OAuth application with:  
  - Client type: Confidential  
  - Authorisation grant type: Resource owner password-based
