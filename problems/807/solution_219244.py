def conta_frases(string):
    frases = string.count("...")
    string = string.replace("...", "")
    
    frases += string.count("?")
    frases += string.count("!")
    frases += string.count(".")
    
    return frases