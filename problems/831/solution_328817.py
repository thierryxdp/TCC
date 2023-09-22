def lingua_p(palavra):
    """ Recebe uma palvra e retorna essa mesma palavra traduzida para a língua do P;
    string->string """
    i=0
    palavra2=''
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiouáéíóú':
            palavra2+=palavra[i]+'p'+palavra[i]
        else:
            palavra2+=palavra[i]
        i=i+1
    return palavra2.lower()