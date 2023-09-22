def uppCons(frase):
    """Retorna a frase colocando todas as consoantes como maiúsculas, string->string """;
    prox=0
    upp=''
    while prox<len(frase):
        if frase[prox] in 'bcdfghjklmnpqrstvwxyzç':
            upp=upp+frase[prox].upper();
        else:
            upp=upp+frase[prox];
        prox+=1;
    return upp;