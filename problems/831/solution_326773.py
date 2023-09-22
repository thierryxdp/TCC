def lingua_p(palavra):
    """..."""
    
    lista1 = []
    contador = 0
    
    for letra in palavra:
        list.append(lista1,letra)

    for item in lista1:
        if item in 'AEIOUaeiou':
            list.insert(lista1,contador+1,'p'+ str(item))
        contador = contador + 1
        
    return str.lower(str.join('',lista1))