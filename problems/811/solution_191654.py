def colchao(dados,H,L):
    """ entra com os dados do móvel e retorna true ou false
    list, string - > bool"""
    dados.sort()
    if dados[0][0] > dados[1] and dados[0][2] > dados[2] :
        return True
    else :
        return False