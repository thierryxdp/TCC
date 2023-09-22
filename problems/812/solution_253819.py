def substitui(cadeia):
    vogais = "aeiou"
    for car in vogais:
        cadeia = cadeia.replace(car, " ")
    
    print cadeia
    return cadeia