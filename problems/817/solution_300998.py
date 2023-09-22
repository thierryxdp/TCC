def acima_da_media(lista):
    """
    lista--->lista
    Foi utilizada a função sum para obter a soma de todos as notas,
    e após isso a soma dividida pela quantidade de valores na lista
    para se obter a média. Foi utilizada a funcao do exercicio anterior
    para a ordem ser crescente, e antes disso o valor x foi adicionado
    à lista. Para finalizar, foi necessario retornar a lista deletando
    dos valores mais baixos até o valor x da média previamente adicionado.
    Caso a lista possua um valor igual ao da média, esse será deletado
    """
    
    x=sum(lista)/len(lista)
    list.append(lista,x)
    list.sort(lista)
    
    z=list.index(lista,x)
    del lista[0:z+1]
    
    if x in lista:
        x=int(x)
        del lista[z]
        return lista
    
    else:
        return lista