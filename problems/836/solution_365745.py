def busca(setor,matriz):
    '''dada uma matriz com as informacoes de todos os funcionarios de uma empresa, essa funcao
    retorna uma matriz com as informacoes referentes aos funcionarios do setor pedido
    str,list-->list'''
    novamatriz=[]
    j=0
    for i in matriz:
        if i[2]==setor:
            list.append(novamatriz,i)
            list.remove(novamatriz[j],setor)
            j+=1
    return novamatriz