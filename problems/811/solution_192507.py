def colchao(medidas,H,L):
    medidaA=int(medidas[0])
    medidaB=int(medidas[1])
    medidaC=int(medidas[2])
    if medidaA<=min(H,L) and medidaB<=max(H,L):
        mensagem=True
    else:
        mensagem=False
    return mensagem