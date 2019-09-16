# Chirpper
RESTFUL APIs that retrieves tweets from twitter using Twitter API.

## How to run the project
### Setting up and installing requirements
1. Clone the repository `https://github.com/patrickian/Chirper.git`<br/>
2. Install python. this project requires `python 3.7.0`<br/>
3. Create a virtualenv. I recommend using `pyenv and pyenv-virtualenv` for controlling both your python version and your virtualenv.<br/>
4. Install `requirements.txt` by running `pip install -r requirements.txt` in the project directory.<br/>
### Creating your configs
5. Signin your account in <a href="https://www.twitter.com">twitter</a>.If you dont have an account, you can signup <a href="https://twitter.com/i/flow/signup">here</a>.<br/>
6. Apply for a twitter developer account. you can apply <a href="https://developer.twitter.com/en/application/use-case">here</a>.<br/>
7. Once your application has been verified by twitter, you can now use the Twitter API!! Hoorayy :) please follow the instructions <a href="https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html">HERE</a> on how to generate tokens to access Twitter API.<br/>
8. Change directory inside the `Chirper` folder and create your own `secrets.json` by copying the content of the `secrets.json.template`. Please put your Twitter API keys here.<br/>
### Finishing up!
9. run the migration. `python manage.py migrate`<br/>
10. run the server. `python manage.py runserver`<br/>

## How to use
*NOTE:* You can use `limit` parameter to control the number of tweets to retrieve.<br/>
### Retrieving tweets based on User
You can retrieve tweets by user using the following endpoint.<br/>
```
/user/<your_user_here>/
```
#### Example
```
curl -H "Accept: application/json" -X GET http://localhost:xxxx/users/jdoe/?limit=20

Example response:

[
    "favorites": 68,
    "account": {
        "fullname": "John Doe",
        "url": "https://ti.co/onlysample",
        "id": 123123123
    },
    "date": "Mon Sep 14 08:09:03 +0000 2019",
    "text": "Sample tweet.SWEEEEEEET!!!!!",
    "hashtags": [
        "OneZeroOne"
    ],
    "retweets": 40
   ...
] 
```

### Retrieving tweets based on Hashtag
You can retrieve tweets by hashtag by using the following endpoint.<br/>
```
/hashtags/<your_hashtag_here>/
```
#### Example
```
curl -H "Accept: application/json" -X GET http://localhost:xxxx/hashtags/python/?limit=20

Example response:

[
    "favorites": 96,
    "account": {
        "fullname": "Mary Jane",
        "url": "https://ti.co/onlysample101",
        "id": 687675547
    },
    "date": "Mon Sep 12 08:09:03 +0000 2019",
    "text": "Python can kill you!!Programmatically and literally. oops :)",
    "hashtags": [
        "python"
    ],
    "retweets": 19
   ...
] 
```