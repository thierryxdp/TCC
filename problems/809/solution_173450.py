# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
#função que dadas duas listas L1 3 L2 de tamaho 3 gera uma lista L3 que é formada intercalando o elementos d L1 e L2    lista3 = [ ]
# list,list -> list
                  lista3 = [ ]
    for i in range(0, len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return lista3