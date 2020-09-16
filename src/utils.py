
def list_to_str(list, separator=" "):
    return separator.join(map(lambda x: x.__str__(), list))


def to_str(x):
    return x.__str__()
