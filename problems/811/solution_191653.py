def colchao(dados,H,L):
    """ entra com os dados do móvel e retorna true ou false
    list, string - > bool"""
    dados.sort()
    if colchao[0][0] > colchao[1] and colchao[0][2] > colchao[2] :
        return True
    else :
        return False