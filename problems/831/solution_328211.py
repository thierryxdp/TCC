def lingua_p(palavra):
    """Retorna a palavra de entrada traduzida para a líbgua do P.
    string --> string"""
    
    str.lower(palavra)
    lista_palavra = list(palavra)
    lista_nova = []
    
    
    for i in range(len(lista_palavra)):
        if lista_palavra[i] in 'aeiouáéíóúãõâêîôû':
            list.append(lista_nova, lista_palavra[i] + 'p' + lista_palavra[i])
        else:
            list.append(lista_nova,lista_palavra[i])
    
    return str.join('',lista_nova)