def busca(setor, matriz):
’’’fun¸c~ao retorna dados de todos os
funcion´arios de determinado setor
str--> list’’’
dados = []
for i in range(len(matriz)):
if setor in matriz[i]:
dados.append(matriz[i])
for j in range(len(dados)):
if dados[j][2] == setor:
del dados[j][2]