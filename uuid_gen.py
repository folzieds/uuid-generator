import uuid
import datetime

def generate_random_uuid():
    date = str(datetime.datetime.now())
    return str(uuid.uuid4())

