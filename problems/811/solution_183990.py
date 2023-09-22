def colchao(medidas,H,L):
    """Dado como entrada a lista medidas, altura H e a largura L, retorna se o colchao consegue passar pela porta
    list,float,float==>bool"""
    hipot = (H**2+L**2)**(1/2)
    hipot2 = (medidas[0]**2+medidas[1])**2)**(1/2)
    hipot3 = (medidas[1]**2+medidas[2])**2)**(1/2)
    hipot4 = (medidas[0]**2+medidas[2])**2)**(1/2)
    if hipot<= hipot2 or hipot<= hipot3 or hipot<=hipot4:
        return False
    else:
        return True