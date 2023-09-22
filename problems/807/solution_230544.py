def frases(diga):
    """ separa words e  conta elas string -> int """
    oi = str.rstrip(diga)
    oi = str.split(diga," ")
    print(len(oi))
    print(oi)