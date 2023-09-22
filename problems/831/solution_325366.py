def lingua_p(palavra):
    """ Retorna a palavra traduzida para a lingua do p; string -> string """
    traducao=[];
    for i in range(0,len(palavra)):
        if palavra[i] in 'aeiouáéíóúâêîôû':
            list.append(traducao,palavra[i]+'p'+palavra[i]);
        else:
            list.append(traducao,palavra[i]);
    return str.join("",traducao);