def busca(setor,dados):
    '''Retorna uma lista com os dados de
       todos os funcionários do setor a partir
       dos dados de entrada; str,matriz->list'''
    retorno=[]
    i=len(dados)-1
    for s in dados:
        if setor in dados[i]:
            retorno.append(dados[i])
            del retorno[i][2]
        i-=1
    return retorno