def insere(lista_numero, n):
    '''Insere um número inteiro na posição corretade uma lista crescente de números inteiros;
    como prova da mudança, retorna a lista atualizada;
    entrada: lista;
    saída: lista;
    '''
    lista_numero=list.append(lista_numero,n)
    lista_numero=list.sort(lista_numero)
    return lista_numero