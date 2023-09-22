def conta_frases(string):
    import re
    ret = (string.split("..."))
    final = re.split("!?.",ret)
	
    return final