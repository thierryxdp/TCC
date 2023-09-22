def uppCons(frase):
    counter = 0
    vogais = ['A', 'E', 'I', 'O', 'U']
    frase_final = ""
    
    for letra in frase:
        letra_maiuscula = letra.upper()
        if letra_maiuscula in vogais:
            frase_final += letra
        else:
            frase_final += letra_maiuscula
            
        counter += 1
    
    return frase_final