def insere(lista_numero,n):
    '''Adiciona um elemento à lista sem que comprometa sua ordem
   de crescência. Assinatura: list,int->list'''
    lista=lista_numero.append(n)
    return len(lista)