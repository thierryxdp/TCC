def insere(lista_numero,n):
    ''' funcao que insere um numero n e ordena a lista em ordem crescente
        list[int,int,int,int] --> list[int,int,int,int,int] '''
    
    resultado1 = list.append(lista_numero, n)
    resultado2 = list.sort(resultado1)
    
    return resultado2