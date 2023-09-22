def conta_frases(string):
	final=string.count(". ")
    excl=string.count("! ")
    inter=string.count("? ")
    ret=string.count("...")
    return final+excl+inter+ret