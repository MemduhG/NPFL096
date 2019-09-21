import re
from difflib import get_close_matches
from time import clock


def parse_dict(file="data/zaza.html"):
    entries = []
    entry = re.compile("<tr.*><td.*>(.*)</td><td.*>(.*)</td><td.*>(.*)</td><td.*>(.*)</td></tr>")
    with open(file) as infile:
        for line in infile:
            m = re.match(entry, line)
            if m is not None:
                entries.append(m.groups())
    return entries



if __name__ == "__main__":
    entries = parse_dict()
    zaza_words = [x[0] for x in entries]
    c = clock()
    for i in range(100):
        v = get_close_matches("verg", zaza_words)
    print(clock() - c )
    print(v)
