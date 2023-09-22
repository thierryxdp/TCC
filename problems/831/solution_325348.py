def lingua_p(palavra): #Recebe uma str
    palavra = palavra.lower() #Passa as letras para minúsculo
    lista = [] 
    for letra in palavra:
        list.append(lista, letra)
        if letra in 'aeiouéíóúáãõ':
            list.append(lista, 'p') #Caso a letra seja vogal, a letra p será adicionada após ela
            list.append(lista, letra)
    retorno = ''.join(lista) #Junta as letras
    return retorno #Retorna a palavra encriptada