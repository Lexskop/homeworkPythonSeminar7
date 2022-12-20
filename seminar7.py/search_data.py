import import_export
import function

def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                yield item
    else:
        return None