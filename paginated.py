
def handler_paginated(event, context):
    print("Calling paginated ...")
    return {'message': event['message']}
