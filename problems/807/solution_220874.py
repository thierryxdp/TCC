def conta_frases(frases):
    result = frases.count(".")
    result2 = frases.count("...")
    result3 = frases.count("!")
    result4 = frases.count("?")
    result =  result - (result2*3) 
    total = result + result2 + result3 + result4
    return total