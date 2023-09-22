def busca(setor,M):
    """Função que recebe uma matriz com os funcionários e as informações sobre
    os mesmos e a partir do setor informado como primeiro argumento da função,
    retorna as demais informações de todos os funcionários que trabalham nele
    em forma de outra matriz, como descrito no enunciado.
    str,list->list"""
    resultado=[]
    for f in range(len(M)):
        if M[f][2]==setor:
            list.append(resultado,[M[f][0],M[f][1],M[f][3]])
    return resultado