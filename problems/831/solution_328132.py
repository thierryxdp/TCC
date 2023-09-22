def lingua_p(frase):
    """ funcao que recebe uma palavra e retorna esta mesma palavra traduzida
    para a lingua do P. quando é traduzida para esta lingua, após cada vogal
    acresceta o P mais a vogal original. obs(frase em portugues). e retornar
    a frase em minusculo. str->str"""
    soma=0
    frase2=''
    while soma<len(frase):
        if frase[soma]in'aeiou':
            frase2 = frase2 +frase[soma]+ 'p'+ frase[soma]
        if frase[soma] not in 'aeiou':
            frase2= frase2+ frase[soma]
        soma +=1
    return frase2