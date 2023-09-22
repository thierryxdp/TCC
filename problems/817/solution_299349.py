def maiores(lista_numero,n):

    ''' A função recebe como parametro uma lista de numeros inteiros e um numero inteiro (n),
        torna n uma lista unitaria, soma com lista_numero gerando uma nova lista ordenada,
        reconhece o indice de n, retorna os valores depois de n na sequencia e exclui n da lista;
        list,int --> list
        
    '''

    junta_listas = sorted(lista_numero + [n])

    x = junta_listas.index(n)

    lista_junta = junta_listas[x:]

    lista_junta.remove(n)

    
    return  lista_junta


def acima_da_media(notas_alunos):

    
    media = ((sum(notas_alunos)/ len(notas_alunos)))

    return maiores ( notas_alunos, media)