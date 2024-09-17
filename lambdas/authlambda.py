import json
import logging
from sys import stdout

format = logging.Formatter("%(asctime)s %(levelname)s %(funcName)s-%(lineno)s - %(message)s")
logger= logging.getLogger(__name__)
logger.setLevel('INFO')
consoleHandler = logging.StreamHandler(stdout) #set streamhandler to stdout
consoleHandler.setFormatter(format)
logger.addHandler(consoleHandler)

def lambda_handler(event, context):
    # TODO implement
    logger.info(f'lambda event: {event}')
    return login(event['queryStringParameters']['username'], event['queryStringParameters']['password'])

def login(username, password):
    #dummy DB operation.
    dbname="suresh"
    dbpassword="suresh123"
    logger.info(f'username: {username} and password: {password}')
    reponseobject = {
    "statusCode": httpStatusCode,
    "headers": { "Content-Type":"application/json"},
    "body": body
}
    if(username == dbname and password == dbpassword):
        httpStatusCode=200
        body = "user logged in"
    else:
        httpStatusCode=400
        body = "invalid user name or password"

    



