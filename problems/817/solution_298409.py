def insere(lista_numero,n):
    """retorna a lista_numero de entrada em ordem crescente
    com a insercao do numero n de entrada na posicao correta
    respeitando a ordem
    list, int-->list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista,n):
    """dada uma lista de entrada, retorna todos os valores
    maiores que o argumento n de entrada em ordem crescente
    list,int-->list"""
    x=insere(lista,n)
    indicesplit=list.index(x,n)
    return x[indicesplit+1:]

def acima_da_media (notas):
    """dada uma lista com as notas dos alunos,
    retorna as notas que ficaram acima de media,
    ordenando-as de forma crescente
    list-->list"""
    mediaNotas=sum(notas)/len(notas)
    maioresNotas=maiores(notas,mediaNotas)
    if mediaNotas in maioresNotas
    return list.remove(maioresNotas,mediaNotas)