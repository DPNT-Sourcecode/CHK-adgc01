

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if(not isinstance(friend_name, str)) : friend_name = str(friend_name)

    return f"Hello {friend_name}!"


