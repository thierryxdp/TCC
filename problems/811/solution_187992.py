def colchao(medidas,H,L):
    if medidas[1]<=H:
        return True
    if medidas[2]<=H:
        return True
    if medidas[1]>H and medidas[2]<=L:
        return True
    if medidas[1]>H or medidas[1]!=H:
        return False
    if medidas[2]>H or medidas[2]!=H:
        return False
'''dado uma lista com as dimensoes do colchao, a altura 
e a largura de uma porta retorna True se o colchao consegue passar 
pela porta e False caso o colchao nao passe
list,int->bool