def lingua_p(palavra):
    """ Retorna a palavra traduzida para a lingua do p; string -> string """
    traducao="";
    for i in range(1,len(palavra)):
        if palavra[i] in 'aeiou':
            traducao=traducao+palavra[i-1]+palavra[i]+'p'+palavra[i]    
    return traducao