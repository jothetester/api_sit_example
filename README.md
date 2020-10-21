# api_sit_example
##Installing Requirements
- Assuming you have python 3.x and pip installed 
- Run the following command from the terminal to install requirements
- cd to the directory where requirements.txt is located. 
- Run :
  `pip install -r requirements.txt`
## Setting up the secrets
- Create a spotify developer account
- When you log on to www.spotify.com with your user credentials, view your user profile
- Identify the user id , copy and paste it in test_data/secrets.py
- For the code to run you need the bearer tokens which can be found if you click on one of the links here https://developer.spotify.com/console/
- These tokens are valid for an hour, so you might need to refresh it

## Running from command line 
- Use the command at the root directory `behave -Denv=dev`

## Debug on IDE
- I used pycharm and you need to set up the configuration and point to right interpreter and virtual env
- Add `-Denv=dev` as the parameter