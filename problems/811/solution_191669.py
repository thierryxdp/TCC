def movel(dados,H,L):
    """ entra com os dados do móvel e retorna true ou false
    list, string - > bool"""
    dados.sort()
    if movel[0][0] > movel[1] and movel[0][2] > movel[2] :
        return True
    else :
        return False