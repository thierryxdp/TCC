def lingua_p(palavra):
    """ Recebe uma palvra e retorna essa mesma palavra traduzida para a língua do P;
    string->string """
    palavra2=''
    for i in palavra:
        if i in 'AEIOUaeiouáéíóú':
            palavra2+=i+'p'+i
        else:
            palavra2+=i
    return palavra2.lower()