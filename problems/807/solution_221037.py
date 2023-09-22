def conta_frases(string):
	l=string.split(". ")
    for x in l:
        x=x.split("!")
    for x in l:
        x=x.split("?")
    for x in l:
        x=x.split("...")
    return len(l)