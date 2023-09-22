def lingua_p(palavra):
    string_saida=''
    for indice in range(len(palavra)):
        if palavra[indice]in'AEIOUaeiou':
            string_saida+=palavra[indice]+'p'+str(palavra[indice])
        else:
            string_saida+=palavra[indice]
    return string_saida