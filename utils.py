import random
import string

def build_tag():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
