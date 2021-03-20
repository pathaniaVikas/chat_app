import threading

Lock = threading.Lock()


def printl(*data):
    with Lock:
        final_string = ''
        for d in data:
            final_string = final_string + str(d)
        print(final_string)