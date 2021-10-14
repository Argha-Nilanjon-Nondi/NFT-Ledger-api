from datetime import datetime

def listToDict(list,key):
    """

    :param list:[["argha","12"]]
    :param key:["name", "key"]
    :return: [{'name': 'argha', 'key': '12'}]
    """

    for index in range(len(list)):
        list[index] = dict(zip(key, list[index]))

    return list

def currentTime():
	now = datetime.now()
	date_time = now.strftime("%Y-%m-%d %H:%M:%S")
	return date_time