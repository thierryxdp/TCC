def insere(lista_numero,n):
    ''' funcao que insere um numero n e ordena a lista em ordem crescente
        list[int,int,int,int] --> list[int,int,int,int,int] '''
    
    insere_numero = list.append(lista_numero,n)
    ordena_numeros = list.sort(insere_numero)
    
    return ordena_numeros