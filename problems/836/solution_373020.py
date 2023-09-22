def busca(setor,matriz):
    """funçao que recebe uma string dizendo o setor de uma
    pessoa que trabalha na empresa e uma matriz com os dados
    dessa pessoa e que retorna uma matriz com somente aquelas
    pessoas que trabalham no setor mencionado, sem o setor 
    na informação
    str,list->list"""
    informacao=[]
    nlin=len(matriz)
    for i in range(nlin):
        if setor in matriz[i]:
            informacao.append(matriz[i])
    for j in range(len(informacao)): 
        del informacao[j][2]
    return informacao