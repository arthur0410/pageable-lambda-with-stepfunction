

def handler_initialize(event, context):
    print("Initializing context ...")
    return {'message': "retorno" + event['message']}


if __name__ == "__main__":
    event = {'message': 'message test'}
    context = []
    print(handler_initialize(event, context)['message'])
