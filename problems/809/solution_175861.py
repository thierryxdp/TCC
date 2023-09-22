def intercala(lista1, lista2):
    """A função ao receber dois parâmetros, cada qual uma
    lista, gerará como retorno uma terceira lista que é
    formada intercalando os elementos das duas listas 
    definidas anteriormente.
    Entrada: List, List 
    Saída: List"""
    
    [a,b,c] = lista1
    [d,e,f] = lista2
    lista3 = [lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]
    
    return lista3