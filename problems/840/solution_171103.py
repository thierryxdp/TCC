def bolos(farinha,ovos,leite):
"""calcula quantos bolos podem ser feitos com os ingredientes fornecidos sendo que a farinha e medida em xicaras e o leite em colheres de sopa"""
nfarinha = (farinha // 2)
novos = (ovos // 3)
nleite = (leite // 5)
nbolos = min(nfarinha,novos,nleite)
return nbolos