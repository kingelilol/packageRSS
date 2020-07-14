from extractor import update
from feedgen.feed import FeedGenerator
import database
import datetime
import time

URL = 'https://realURL'

def generateFeed():
    fg = FeedGenerator()
    fg.id(URL)
    fg.title('Package Tracking')
    fg.link(href=URL)
    fg.description('Delivers Package Tracking Updates')

    for entry in database.all():
        fe = fg.add_entry()
        fe.link(href=entry.get('link'))
        fe.id(URL + '/' + str(entry.doc_id))
        fe.title(entry.get('edd'))
        fe.description(entry.get('discr'))
        fe.updated(datetime.datetime.fromtimestamp(entry.get('epoch'),datetime.timezone.utc))
    atomfeed = fg.atom_str(pretty=True) # Get the ATOM feed as string
    fg.atom_file('/srv/atom.xml') # Write the ATOM feed to a file


if __name__ == "__main__":
    for line in open('/packageRSS/list.txt','r').readlines():
        database.extend(update.fetchData(line))
    generateFeed()
    
