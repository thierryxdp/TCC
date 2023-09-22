def lingua_p(palavra):
    vogais = 'aeiouáéíóúâêîôûãõ'
    resultado = []
    for i in range(len(palavra)):
        if palavra[i] in vogais:
           substituicao = palavra[i]+'p'+palavra[i]
           list.append(resultado,substituicao)
        else:
            list.append(resultado, palavra[i])
    return str.join('', resultado)