def tagged(base, tags):
    for tag in tags:
        if len(tag.strip()) > 0:
            base += "<" + tag.strip() + ">"
    return base

def cons_masc(lemma):
    forms = dict()
    forms[lemma] = [lemma, "n", "m", "sg", "dir"]
    forms[lemma + "i"] = [lemma, "n", "m", "sg", "obl"]
    forms[lemma + "i"] = [lemma, "n", "m", "pl", "dir"]
    forms[lemma + "an"] = [lemma, "n", "m", "pl", "obl"]
    forms[lemma + "o"] = [lemma, "n", "m", "sg", "ezd"]
    forms[lemma + "ê"] = [lemma, "n", "m", "sg", "ezg"]
    forms[lemma + "dê"] = [lemma, "n", "m", "sg", "ezs"]
    forms[lemma + "ê"] = [lemma, "n", "m", "pl", "ezd"]
    forms[lemma + "ê"] = [lemma, "n", "m", "pl", "ezg"]
    forms[lemma + "dê"] = [lemma, "n", "m", "pl", "ezs"]
    return forms


def cons_fem(lemma):
    forms = dict()
    forms[lemma] = [lemma, "n", "f", "sg", "dir"]
    forms[lemma + "ı"] = [lemma, "n", "f", "sg", "loc"]
    forms[lemma + "er"] = [lemma, "n", "f", "sg", "obl"]
    forms[lemma + "i"] = [lemma, "n", "f", "pl", "dir"]
    forms[lemma + "an"] = [lemma, "n", "f", "pl", "obl"]
    forms[lemma + "a"] = [lemma, "n", "f", "sg", "ezd"]
    forms[lemma + "a"] = [lemma, "n", "f", "sg", "ezg"]
    forms[lemma + "da"] = [lemma, "n", "f", "sg", "ezs"]
    forms[lemma + "ê"] = [lemma, "n", "f", "pl", "ezd"]
    forms[lemma + "ê"] = [lemma, "n", "f", "pl", "ezg"]
    forms[lemma + "dê"] = [lemma, "n", "f", "pl", "ezs"]
    return forms

def vow_masc(lemma):
    forms = dict()
    forms[lemma] = [lemma, "n", "m", "sg", "dir"]
    forms[lemma + "y"] = [lemma, "n", "m", "sg", "obl"]
    forms[lemma + "y"] = [lemma, "n", "m", "pl", "dir"]
    forms[lemma + "yan"] = [lemma, "n", "m", "pl", "obl"]
    forms[lemma + "yo"] = [lemma, "n", "m", "sg", "ezd"]
    forms[lemma + "y"] = [lemma, "n", "m", "sg", "ezg"]
    forms[lemma + "dê"] = [lemma, "n", "m", "sg", "ezs"]
    forms[lemma + "y"] = [lemma, "n", "m", "pl", "ezd"]
    forms[lemma + "y"] = [lemma, "n", "m", "pl", "ezg"]
    forms[lemma + "dê"] = [lemma, "n", "m", "pl", "ezs"]
    return forms

def vow_fem(lemma):
    forms = dict()
    forms[lemma] = [lemma, "n", "f", "sg", "dir"]
    forms[lemma + "yı"] = [lemma, "n", "f", "sg", "loc"]
    forms[lemma + "yer"] = [lemma, "n", "f", "sg", "obl"]
    forms[lemma + "y"] = [lemma, "n", "f", "pl", "dir"]
    forms[lemma + "yan"] = [lemma, "n", "f", "pl", "obl"]
    forms[lemma + "ya"] = [lemma, "n", "f", "sg", "ezd"]
    forms[lemma + "ya"] = [lemma, "n", "f", "sg", "ezg"]
    forms[lemma + "y"] = [lemma, "n", "f", "sg", "ezd"]
    forms[lemma + "y"] = [lemma, "n", "f", "sg", "ezg"]
    forms[lemma + "da"] = [lemma, "n", "f", "sg", "ezs"]
    forms[lemma + "y"] = [lemma, "n", "f", "pl", "ezd"]
    forms[lemma + "y"] = [lemma, "n", "f", "pl", "ezg"]
    forms[lemma + "dê"] = [lemma, "n", "f", "pl", "ezs"]
    return forms


def adj_masc(lemma):
    forms = dict()
    forms[lemma] = [lemma, "adj", "m", "sg"]
    if lemma[-1] in "aoeiıêuû":
        forms[lemma + "yi"  ] = [lemma, "adj", "m", "pl"]
    else:
        forms[lemma + "i"  ] = [lemma, "adj", "m", "pl"]
    return forms

def adj_fem(lemma):
    forms = dict()
    if lemma[-1] in "aoeiıêuû":
        forms[lemma + "yı"] = [lemma, "adj", "f", "sg"]
        forms[lemma + "yi"  ] = [lemma, "adj", "f", "pl"]
    else:
        forms[lemma + "ı"] = [lemma, "adj", "f", "sg"]
        forms[lemma + "i"  ] = [lemma, "adj", "f", "pl"]
    return forms


def verb_chin_tv(pres_stem, past_stem=None):
    forms = dict()
    forms[pres_stem + "enan"] = [pres_stem, "v", "tv", "pres", "p1", "sg"]
    forms[pres_stem + "enê"] = [pres_stem, "v", "tv", "pres", "p2", "sg", "m"]
    forms[pres_stem + "ena"] = [pres_stem, "v", "tv", "pres", "p2", "sg", "f"]
    forms[pres_stem + "eno"] = [pres_stem, "v", "tv", "pres", "p3", "sg", "m"]
    forms[pres_stem + "ena"] = [pres_stem, "v", "tv", "pres", "p3", "sg", "f"]
    forms[pres_stem + "enê"] = [pres_stem, "v", "tv", "pres", "pl"]
    return forms




if __name__ == "__main__":
    b = cons_masc("bergir")
    print(b)

