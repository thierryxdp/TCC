def maiores(lista_inteiros,n):
    # Adiciona o numero na lista
    list.append(lista_inteiros,n)
    # Ordena na lista, crescente
    list.sort(lista_inteiros)
    # Pega  a primeira ocorrencia do n, na lista
    posicao = list.index(lista_inteiros,n)
    # Verifica a quantidade de n na lista
    contagem = list.count(lista_inteiros,n)
    # Caso tenha apenas 1 caso na lista, segue essa ordem
    if contagem == 1:
        # Pega lista depois do n
        return lista_inteiros[posicao+1:]
    # Caso tenha mais de 1 caso na lista, segue essa ordem
    if contagem > 1:
        # Pega lista depois do n
        return lista_inteiros[posicao+contagem+1:]
def acima_da_media(lista_inteiros):
    n = sum(lista_inteiros)/len(lista_inteiros)
    media = maiores(lista_inteiros,n)
    return media