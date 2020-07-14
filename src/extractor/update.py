import re
from extractor import dhl, hermes

def fetchData(link):
    if re.search("www\.myhermes\..+",link):
        return hermes.update(link)
    elif re.search("www\.dhl\..+",link):
        return dhl.update(link)
    else:
        return None


