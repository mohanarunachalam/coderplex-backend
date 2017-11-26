**JWT Token**
----
  Fetch JWT Token using user credentials

* **URL**

  **`/api-token-auth`**

* **Method:**
  
  **`POST`**

* **Data Params**
  
  **Required:**
 
   `username=[string]`
   
   `password=[string]`
    

* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:** `
                {
                    "token": "eyJ0eXAiOiJKV1QiLCJhbGciO"
                }`
        
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{
                    "non_field_errors": [
                        "Unable to log in with provided credentials."
                    ]
                  }`

  OR

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{
                   "password": [
                        "This field may not be blank."
                    ]
                  }`
  
  OR

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{                    
                    "password": [
                        "This field is required."
                    ]
                  }`
                  

* **Sample Call:**

  ```
    curl -X POST \
      http://localhost:8000/api-token-auth \      
      -H 'content-type: application/json' \
      -d '{
        "username": "admin",
        "password" : "admin_password"
    }'
  ``` 

* **Notes:**

  - None
  
**GITHUB LOGIN**
----
  Login to the application using **GITHUB**

* **URL**

  **`/v1/auth/github`**

* **Method:**
  
  **`POST`**

* **Data Params**
  
  **Required:**
    
   `code=[string]`
   
* **Headers**
  
  **Required:**
    
   `content-type: application/json`   

* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:** 
    ```json
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGc",
            "user": {                
                "username": "user123",
                "first_name": "P",
                "last_name": "User Name",
                "avatar": "http://www.sample.com/image.jpg",
                "email" : "email@example.com"
            }
        }
     ```
        
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{"non_field_errors": ["Incorrect input. access_token or code is required."]}` <br />
    **Problem:** `code is blank or code is not passed as data`
                  

* **Sample Call:**

  ```
    curl -X POST \
      http://localhost:8000/v1/auth/github \
      -H 'content-type: application/json' \      
      -d '{
        "code" : "e47deee658cb2c59a6"
    }'
  ``` 

* **Notes:**

  - You may get **500 INTERNAL SERVER ERROR** sometimes, in that case check the error content to find out the problem.  
  
**LINKEDIN LOGIN**
----
  Login to the application using **LINKEDIN**

* **URL**

  **`/v1/auth/linkedin`**

* **Method:**
  
  **`POST`**

* **Data Params**
  
  **Required:**
    
   `code=[string]`
   
* **Headers**
  
  **Required:**
    
   `content-type: application/json`

* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:** 
    ```json
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGc",
            "user": {                
                "username": "user123",
                "first_name": "P",
                "last_name": "User Name",
                "avatar": "http://www.sample.com/image.jpg",
                "email" : "email@example.com"
            }
        }
     ```
        
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{"non_field_errors": ["Incorrect input. access_token or code is required."]}` <br />
    **Problem:** `code is blank or code is not passed in data`
                  

* **Sample Call:**

  ```
    curl -X POST \
      http://localhost:8000/v1/auth/linkedin \    
      -H 'content-type: application/json' \      
      -d '{
        "code" : "e47deee658cb2c59a6"
    }'
  ``` 

* **Notes:**

  - You may get **500 INTERNAL SERVER ERROR** sometimes, in that case check the error content to find out the problem.
  

**GITHUB CODE**
----
  Fetch code from **GITHUB** api for oauth authorization

* **URL**

  **`https://github.com/login/oauth/authorize`**

* **Method:**
  
  **`GET`**

* **URL Params**
  
  **Required:**
    
   `client_id=[string]`
   
  **Optional:**
  
    `scope=[string]`
    
    `redirect_uri=[string]`
    
    `state=[string]`
    
    `allow_signup=[string]`  

* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:** `code` will be appended as param to your `callback_url` or `redirect_uri`                          

* **Sample Call:**

  ```
    curl -X GET \
    'https://github.com/login/oauth/authorize?scope=user:email&client_id=97d600c693730ed0'    
  ``` 

* **Notes:**

  - Check [this](https://developer.github.com/apps/building-integrations/setting-up-and-registering-oauth-apps/about-authorization-options-for-oauth-apps/) for further info
  
**LINKEDIN CODE**
----
  Fetch code from **LINKEDIN** api for oauth authorization

* **URL**

  **`https://www.linkedin.com/oauth/v2/authorization`**

* **Method:**
  
  **`GET`**

* **URL Params**
  
  **Required:**
    
   `response_type=[string]`
   
   `client_id=[string]`
   
   `redirect_uri=[string]`
   
   `state=[string]`
   
  **Optional:**
  
   `scope=[string]`         

* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:** `code` will be appended as param to your `callback_url` or `redirect_uri`                          

* **Sample Call:**

  ```
    curl -X GET \
    'https://github.com/login/oauth/authorize?scope=user:email&client_id=97d600c693730ed0'    
  ``` 

* **Notes:**
  - The value of the `response_type` field should always be:  `code`
  - Check [this](https://developer.linkedin.com/docs/oauth2) for further info
  
  
**USER View**
----
  Fetch the details of logged_in user

* **URL**

  **`/user`**

* **Method:**
  
  **`GET`**

* **Headers**
  
  **Required:**   
   
   `authorization: JWT <token>`

* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:** 
    ```json
        {            
            "username": "user123",
            "first_name": "First",
            "last_name": "Last",
            "email": "email@example.com"                        
        }
    ```
                               

* **Sample Call:**

  ```
    curl -X GET \
      http://localhost:8000/user \
      -H 'authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6Ik' \          
  ``` 

* **Notes:**
  - None
  
**USER Update**
----
  Update the details of logged_in user

* **URL**

  **`/user`**

* **Method:**
  
  **`POST`**

* **URL Params**  
   
  **Optional:**
  
   `username=[string]`
   
   `email=[email]`
   
   `first_name=[string]`
   
   `last_name=[string]`
   

* **Headers**
  
  **Required:**   
   
   `authorization: JWT <token>`

* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:** 
    ```json
        {                  
          "username": "user123",
          "first_name": "P",
          "last_name": "User Name",         
          "email" : "email@example.com"
        }
    ```
                               

* **Sample Call:**

  ```
    curl -X POST \
      http://localhost:8000/user \
      -H 'authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTE0ODMzOTQsImVtYWlsIjoiIiwidXNlcm5hbWUiOiJiaGFudV90ZWphIiwidXNlcl9pZCI6NzR9.Hc1H8Tt9d2FSJkTEHKjx-fB8cblrg1yKDVK9lzuZ914' \      
      -H 'content-type: application/json' \      
      -d '{
        "username" : "user123",
        "first_name" : "First",
        "last_name" : "last",
        "email" : "email@example.com"
    }'          
  ``` 

* **Notes:**
  - None
  
**USER Profile View**
----
  Fetch the profile of logged_in user
  
* **URL**

  **`/user/profile`**

* **Method:**
  
  **`GET`**

* **Headers**
  
  **Required:**   
   
   `authorization: JWT <token>`

* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:** 
    ```json
        {
            "user": {
                "username": "user123",
                "first_name": "First",
                "last_name": "Last",
                "email": "email@example.com"
            },
            "avatar": "https://avatars3.githubusercontent.com/u/17903466?v=4",
            "mobile_number": null,
            "short_bio": "This is my short bio",
            "job_status": true,
            "company_name": "company112",
            "looking_for_job": false,
            "github_profile": "https://github.com/user123",
            "facebook_profile": null,
            "twitter_profile": null,
            "linkedin_profile": null,
            "codepen_profile": null,
            "discord_profile": null,
            "familiar_technologies": null,
            "interested_technologies": null
        }
    ```
                               

* **Sample Call:**

  ```
    curl -X GET \
      http://localhost:8000/user \
      -H 'authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6Ik' \          
  ``` 

* **Notes:**
  - None
  
**USER Profile Update**
----
  Update the profile of logged_in user

* **URL**

  **`/user/profile`**

* **Method:**
  
  **`POST`**

* **URL Params**  
   
  **Optional:**
  
    `avatar=[url]`
    
    `mobile_number=[string]`
    
    `short_bio=[string]`
    
    `job_status=[boolean]`
    
    `company_name=[string]`
    
    `looking_for_job=[boolean]`
    
    `github_profile=[url]`
    
    `facebook_profile=[url]`
    
    `twitter_profile=[url]`
    
    `linkedin_profile=[url]`
    
    `codepen_profile=[url]`
    
    `discord_profile=[url]`
    
    `familiar_technologies=[string]`
    
    `interested_technologies=[string]`
    

* **Headers**
  
  **Required:**   
   
   `authorization: JWT <token>`

* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:** 
    ```json
        {
            "user": {
                "username": "user123",
                "first_name": "First",
                "last_name": "Last",
                "email": "email@example.com"
            },
            "avatar": "https://avatars3.githubusercontent.com/u/17903466?v=4",
            "mobile_number": null,
            "short_bio": "This is my short bio",
            "job_status": true,
            "company_name": "company112",
            "looking_for_job": false,
            "github_profile": "https://github.com/user123",
            "facebook_profile": null,
            "twitter_profile": null,
            "linkedin_profile": null,
            "codepen_profile": null,
            "discord_profile": null,
            "familiar_technologies": null,
            "interested_technologies": null
        }
    ```
                               

* **Sample Call:**

  ```
    curl -X POST \
      http://localhost:8000/user \
      -H 'authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTE0ODMzOTQsImVtYWlsIjoiIiwidXNlcm5hbWUiOiJiaGFudV90ZWphIiwidXNlcl9pZCI6NzR9.Hc1H8Tt9d2FSJkTEHKjx-fB8cblrg1yKDVK9lzuZ914' \      
      -H 'content-type: application/json' \      
      -d '{
            "avatar": "https://avatars3.githubusercontent.com/u/17903466?v=4",
            "mobile_number": "9854785985",
            "short_bio": "This is my short bio",
            "job_status": true,
            "company_name": "company112",
            "looking_for_job": false,
            "github_profile": "https://github.com/user123",
            "facebook_profile": "https://facebook.com/user123",
            "twitter_profile": "https://twitter.com/user123",
            "linkedin_profile": "https://linkedin.com/user123",
            "codepen_profile": "https://codepen.com/user123",
            "discord_profile": "https://discord.com/user123",
            "familiar_technologies": "c",
            "interested_technologies": "c"
      }'          
  ``` 

* **Notes:**
  - None