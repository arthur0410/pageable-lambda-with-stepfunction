def handler_initialize(event, context):
    print("Initializing context ...")
    return {
        'start_date': "2021-01-01", 
        'end_date': "2021-01-02",
        'page': 0, 
        'is_completed': False
    }
