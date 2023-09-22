def insere(lista_numero,n):
    ''' funcao que insere um numero n e ordena a lista em ordem crescente
        list[int,int,int,int] --> list[int,int,int,int,int] '''
    
    inserenumero = list.append(lista_numero,n)
    ordenanumeros = list.sort(inserenumero)
    
    return ordenanumeros