def lingua_p(palavra):
    """Retorna a palavra de entrada traduzida para a líbgua do P.
    string --> string"""
    
    str.lower(palavra)
    lista_palavra = list(palavra)
    lista_nova = []
    
    
    for i in range(len(lista_palavra)):
        if lista_palavra[i] in 'aeiou':
            list.append(lista_nova, i + 'p')
        else:
            list.append(lista_nova,i)
    
    return str.join('',lista_nova)