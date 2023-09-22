def busca(setor,dados):
    '''Retorna uma lista com os dados de
       todos os funcionários do setor a partir
       dos dados de entrada; str,matriz->list'''
    retorno=[]
    i=0
    for s in dados:
        if setor in dados[i]:
            del dados[i][2]
            retorno.append(dados[i])
        i+=1
    return retorno