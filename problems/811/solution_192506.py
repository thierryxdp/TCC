def colchao(medidas,H,L):
    medidaA=int(medidas[0])
    medidaB=int(medidas[1])
    medidaC=int(medidas[2])
    if medidaA<=int(L) and medidaB<=int(H):
        mensagem=True
    else:
        mensagem=False
	return mensagem