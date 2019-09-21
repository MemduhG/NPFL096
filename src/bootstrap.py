import requests
from html import unescape
from parse import parse_dict
import re
from collections import Counter

def get_dictionary(url="http://baseportal.de/cgi-bin/baseportal.pl?htx=/zonema/qesebend&range=0,14000"):
    r = requests.get(url)
    r.encoding = "iso8859_9"
    text = unescape(r.text)
    with open("data/zaza.html", "w") as outfile:
        outfile.write(text)


def get_initial_distributions(lexicon, analysis_file):
    with open(analysis_file) as infile:
        analyzed = infile.read()
    item_exp = re.compile("\^[^\$]*\$")
    items = re.findall(item_exp, analyzed)
    turkish_dictionary, distributions = dict(), dict()
    for item in items:
        broken = item.lstrip("^").rstrip("$").split("/")
        possibilities = [re.search("<[^>]*>", x).group(0) for x in broken[1:] if re.search("<[^>]*>", x)]
        summed, counts = len(possibilities), Counter(possibilities)
        turkish_dictionary[broken[0]] = {x: counts[x]/summed for x in counts}
    for item in lexicon:
        zaza_word = item[0].partition("[")[0].partition("(")[0].strip()
        definitions = item[1].split(",")
        def_distribution = Counter()
        for defn in definitions:
            if " " in defn:
                current_def = defn.split(" ")[-1]
            else:
                current_def = defn
            try:
                def_distribution += turkish_dictionary[current_def]
            except KeyError:
                continue
        prob_sum = sum(def_distribution.values())
        if len(def_distribution) > 0:
            distributions[zaza_word] = {x: def_distribution[x]/prob_sum for x in def_distribution}
    return distributions


if __name__ == "__main__":
    try:
        lexicon = parse_dict("data/zaza.html")
    except FileNotFoundError:
        get_dictionary()
        lexicon = parse_dict("data/zaza.html")
    distributions = get_initial_distributions(lexicon, "data/turkish_analyzed.txt")
    print("zobina:", distributions["zobina"])

