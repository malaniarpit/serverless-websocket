import json

def connectionManager(event, context):
  print(str(event))
  return { "statusCode": 200, "body": json.dumps({"message": "Hello World!"})}

def defaultMessage(event, context):
  print(str(event))
  return { "statusCode": 200, "body": json.dumps({"message": "Hello World!"})}

def sendMessage(event, context):
  print(str(event))
  return { "statusCode": 200, "body": json.dumps({"message": "Hello World!"})}
