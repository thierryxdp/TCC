def inverte(frase:str)->str:
    "Dada uma frase, retorna ela invertida."
    
    #colocando a frase com letras minúscula.
    frase1 = str.lower(frase)
    
    #retirando a pontuação.
    frase2 = str.replace('.', ' ')
    frase2 = str.replace(',', ' ')
    frase2 = str.replace('-', ' ')
    frase2 = str.replace(';', ' ')
    frase2 = str.replace(':', ' ')
    frase2 = str.replace('?', ' ')
    frase2 = str.replace('!', ' ')
    frase2 = str.replace('...', ' ')
    
    #inverter a frase.
    fraseInvertida = str.reverse(frase2)
    
    return fraseInvertida