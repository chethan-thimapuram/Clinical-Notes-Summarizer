import json

def lambda_handler(event, context):
    # Simple demo lambda handler returning echo of input text
    body = event.get('body')
    if body is None:
        return { 'statusCode':400, 'body': json.dumps({'error':'No body provided'}) }
    return { 'statusCode':200, 'body': json.dumps({'received': body}) }

if __name__ == '__main__':
    print(lambda_handler({'body':'hello from local test'}, None))
