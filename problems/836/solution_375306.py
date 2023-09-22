def busca(informacao,registro):
    """Função que dada o setor da empresa, retorna os dados de todos os
    funcionários daquele setor; str,list->list"""
    resultado=[]
    for elemento in registro:
        i=0
        for dados in elemento:
            if str.lower(informacao)in str.lower(dados):
                resultado+= [elemento[0:i]+elemento[i+1:]]
            i+=1
    return resultado