def lingua_p(palavra):
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            novo = letra + 'p' + letra
        	palavra = palavra.replace(letra, novo) 
    return palavra