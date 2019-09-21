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


def pres_chin(pres_stem):
    forms = dict()
    if pres_stem[0] in "aoeiıêuû":
        neg_pref = "nêy"
        subj_pref = "bıy"
    else:
        neg_pref = "nê"
        subj_pref = "bı"
    if pres_stem[-1] in "aoeiıêuû":
        forms[pres_stem + "nan"] = [pres_stem, "v", "pres", "p1", "sg"]
        forms[pres_stem + "nê"] = [pres_stem, "v", "pres", "p2", "sg", "m"]
        forms[pres_stem + "na"] = [pres_stem, "v", "pres", "p2", "sg", "f"]
        forms[pres_stem + "no"] = [pres_stem, "v", "pres", "p3", "sg", "m"]
        forms[pres_stem + "na"] = [pres_stem, "v", "pres", "p3", "sg", "f"]
        forms[pres_stem + "nê"] = [pres_stem, "v", "pres", "pl"]
        forms[subj_pref + pres_stem + "yan"] = [pres_stem, "v", "subj", "p1", "sg"]
        forms[subj_pref + pres_stem + "yê"] = [pres_stem, "v", "subj", "p2", "sg"]
        forms[subj_pref + pres_stem + "yo"] = [pres_stem, "v", "subj", "p3", "sg"]
        forms[subj_pref + pres_stem + "yê"] = [pres_stem, "v", "subj", "pl"]
        forms[pres_stem + "yan"] = [pres_stem, "v", "subj", "p1", "sg"]
        forms[pres_stem + "yê"] = [pres_stem, "v", "subj", "p2", "sg"]
        forms[pres_stem + "yo"] = [pres_stem, "v", "subj", "p3", "sg"]
        forms[pres_stem + "yê"] = [pres_stem, "v", "subj", "pl"]
    else:
        forms[pres_stem + "enan"] = [pres_stem, "v", "pres", "p1", "sg"]
        forms[pres_stem + "enê"] = [pres_stem, "v", "pres", "p2", "sg", "m"]
        forms[pres_stem + "ena"] = [pres_stem, "v", "pres", "p2", "sg", "f"]
        forms[pres_stem + "eno"] = [pres_stem, "v", "pres", "p3", "sg", "m"]
        forms[pres_stem + "ena"] = [pres_stem, "v", "pres", "p3", "sg", "f"]
        forms[pres_stem + "enê"] = [pres_stem, "v", "pres", "pl"]
        forms[subj_pref + pres_stem + "an"] = [pres_stem, "v", "subj", "p1", "sg"]
        forms[subj_pref + pres_stem + "ê"] = [pres_stem, "v", "subj", "p2", "sg"]
        forms[subj_pref + pres_stem + "o"] = [pres_stem, "v", "subj", "p3", "sg"]
        forms[subj_pref + pres_stem + "ê"] = [pres_stem, "v", "subj", "pl"]
        forms[pres_stem + "an"] = [pres_stem, "v", "subj", "p1", "sg"]
        forms[pres_stem + "ê"] = [pres_stem, "v", "subj", "p2", "sg"]
        forms[pres_stem + "o"] = [pres_stem, "v", "subj", "p3", "sg"]
        forms[pres_stem + "ê"] = [pres_stem, "v", "subj", "pl"]
    surface_forms = list(forms.keys())
    for item in surface_forms:
        if "pres" not in forms[item]:
            continue
        negated = list(forms[item])
        negated.insert(negated.index("v") + 1, "neg")
        forms[neg_pref + item] = negated
    return forms


def past_ant(past_stem, stem):
    forms = dict()
    if past_stem[0] in "aoeiıêuû":
        neg_pref = "nêy"
    else:
        neg_pref = "nê"
    if past_stem[-1] in "aoeiıêuû":
        forms[past_stem + "yan"] = [stem, "v", "past", "p1", "sg"]
        forms[past_stem + "y"] = [stem, "v", "past", "p2", "sg", "m"]
        forms[past_stem + "ya"] = [stem, "v", "past", "p2", "sg", "f"]
        forms[past_stem] = [stem, "v", "past", "p3", "sg", "m"]
        forms[past_stem + "y"] = [stem, "v", "past", "p3", "sg", "f"]
        forms[past_stem + "y"] = [stem, "v", "past", "pl"]
    else:
        forms[past_stem + "an"] = [stem, "v", "past", "p1", "sg"]
        forms[past_stem + "ê"] = [stem, "v", "past", "p2", "sg", "m"]
        forms[past_stem + "a"] = [stem, "v", "past", "p2", "sg", "f"]
        forms[past_stem] = [stem, "v", "past", "p3", "sg", "m"]
        forms[past_stem + "i"] = [stem, "v", "past", "p3", "sg", "f"]
        forms[past_stem + "i"] = [stem, "v", "past", "pl"]
    surface_forms = list(forms.keys())
    for item in surface_forms:
        negated = list(forms[item])
        negated.insert(negated.index("v") + 1, "neg")
        forms[neg_pref + item] = negated
    return forms


if __name__ == "__main__":
    v = pres_chin("şı")
    print(v)

