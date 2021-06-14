def handler_paginated(event, context):
    print("start_date: " + event["start_date"])
    print("end_date: " + event["end_date"])
    print("page" + event["page"])
    print("is_completed" + event["is_completed"])

    event["page"] += 1
    if (event["page"] >= 3):
        event["isc_completed"] = True

    return event
