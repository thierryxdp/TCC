def insere(lista_numero,n):
    '''Insere o número n na lista de entrada de tal modo que
	   seja mantido seu arranjo em ordem crescente;
       list, float -> list'''
    l=lista_numero.append(n).sort()
    return l