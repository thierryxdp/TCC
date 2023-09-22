def lingua_p(palavra):
    for letra in palavra:
        if letra in 'aeiou':
            palavra.replace(letra, 'p' + letra)
            
    		return palavra