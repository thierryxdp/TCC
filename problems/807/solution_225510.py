def conta_frase(frase, palavra, index):
    """função substitui palavra na posição desejada.
    Palavra repetida é coloca em maiúscula, palavra não
    repetida é inserida na posição desejada.
    str, str, int--> str"""

    lista1 = frase.split()  #quebra a frase e transforma a frase em lista
    
    if palavra in lista1:
        lista1[lista1.index(palavra)] = str.upper(palavra)  #rastreia posição da palavra na lista e substitui em maiúsculo
        return str.join(' ', lista1)                        #junta a lista 1 e devolve em formato de string 

    else:
        lista1.insert(index, palavra)    #insere palavra na posição desejada dentro da lista1
        return str.join(' ', lista1)     #junta a lista 1 e devolve em formato de string