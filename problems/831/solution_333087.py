def lingua_p(palavra):
    #vogais = ['a', 'e', 'i', 'o', 'u']
   	minuscula = palavra.lower()    
    for letra in vogais:
        minuscula = minuscula.replace(letra, letra + 'p' + letra)
    return minuscula