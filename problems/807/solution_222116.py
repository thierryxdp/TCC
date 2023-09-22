def conta_frases (texto1):
    """dado um texto como parâmetro, a função calcula o numero de frases desse mesmo texto;
    str -> int"""
    lista1 = str.split (texto1, '!')
    texto2 = str(lista1)[2:-2]
    
    lista2 = str.split(texto2, '?')
    texto3 = str(lista2)[2:-2]
    
    lista3 = str.split(texto3, '...')
    texto4 = str(lista3)[2:-2]
    
    listafinal = str.split(texto4, '.')
    textofinal = str(listafinal)[2:-2]
    
    textofinal2 = str.split(textofinal, ',') 
    if ' \'' in textofinal2:
        list.remove(textofinal2,' \'')
    
    return len(textofinal2)