def lingua_p(palavra):
    """ Recebe uma palvra e retorna essa mesma palavra traduzida para a língua do P;
    string->string """
    palavra2=''
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiou':
            palavra2+=palavra[i]+'p'+palavra[i]
        else:
            palavra2+=palavra[i]
    return palavra2.lower()