def lingua_p(palavra):
    "função que retorna a tradução de uma palavra em português para a língua do p"
    "str -> str"
    lista=[]
    lista_p=[]
    
    for letra in palavra:
        lista.append(letra)
    
    for vogal in lista:
        if vogal in 'aeiouáéíóú':
            lista_p.append(vogal+"p"+vogal)
        else:
            lista_p.append(vogal)
    string= " ".join(lista_p)
    return string.lower()