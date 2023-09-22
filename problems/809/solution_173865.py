import math
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    lista3=[]
    for i in range(6):
        if(i%2==0):
            if(i==0):
                lista3[i]=lista2[i]
            else:
                lista3[i]=lista2[i//2]
        else:
            lista3[i]=lista1[math.ceil(i//2)]