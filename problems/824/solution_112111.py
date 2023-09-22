def remove(caracter):
    consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y""z","ç"]
    return str.upper(caracter) if caracter in consoantes else caracter

def uppCoins(frase):
    frase = str.join(list(map(remove, frase)))
    return frase