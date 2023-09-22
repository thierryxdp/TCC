def insere(lista_numero,n):
    ''' funcao que insere um numero n e ordena a lista em ordem crescente
        list[int,int,int,int] --> list[int,int,int,int,int] '''
    
    resultado1 = lista_numero + [n]
    resultado2 = sorted(resultado1)
    
    return resultado2