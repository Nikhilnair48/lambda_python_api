import json

def main_handler(event, context):
    response = {}

    if(event["queryStringParameters"]["username"] == "user" and event["queryStringParameters"]["password"] == "pass"):
        response = { "statusCode": 200, "body": json.dumps("Welcome!") }
    else:
        response = { "statusCode": 401, "body": json.dumps("Incorrect credentials. Please try again.") }
    
    return response