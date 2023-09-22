def lingua_p(palavra):
    """ Recebe como parametro uma palavra em portugues e retorna esta mesma palavra traduzida para a a lingua do P
    str -> str """
    saida = ''
    palavra = palavra.lower()
    for i in range(len(palavra)):
        saida+=palavra[i]
        if palavra[i] in 'aeiouáéíóúâêîôûãõàèìòù':
            saida+='p'+palavra[i]
    return saida