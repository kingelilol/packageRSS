from tinydb import TinyDB, Query
import time


def append(data):
    db = TinyDB('/packageRSS/db.json')
    query = Query()
    if not data.get('date') in [entry.get('date') for entry in db.search(query.link == data.get('link'))]:
        if len(db) == 0:
            db.insert({'modified': time.time()})
        else:
            db.update({'modified': time.time()}, query.modified != None)

        db.insert({
            'link': data.get('link'),
            'edd': data.get('edd'),
            'date': data.get('date'),
            'discr': data.get('text'),
            'epoch': time.time()
            })

def extend(data):
    if not data:
        return
    for entry in data:
        append(entry)

def all():
    db = TinyDB('/packageRSS/db.json')
    query = Query()
    return db.search(query.link != None)

