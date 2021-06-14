def handler_paginated(event, context):
    print("start_date: " + str(event["start_date"]))
    print("end_date: " + str(event["end_date"]))
    print("page" + str(event["page"]))
    print("is_completed" + str(event["is_completed"]))

    event["page"] += 1
    if (event["page"] >= 3):
        event["is_completed"] = True

    return event
