def lingua_p(frase):
    """ funcao que recebe uma palavra e retorna esta mesma palavra traduzida
    para a lingua do P. quando é traduzida para esta lingua, após cada vogal
    acresceta o P mais a vogal original. obs(frase em portugues). e retornar
    a frase em minusculo. str->str"""
    
    frase2=''
    for letra in frase:
        if letra in'aeiouáéíóú':
            frase2 = frase2 + letra + 'p'+ letra
        if letra not in 'aeiouáéíóú':
            frase2= frase2+ letra
        
    return frase2