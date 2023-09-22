# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
   '''essa função pega duas listas e as intercala
uma na outra formando assim um terceira lista a qual é retornada'''
   lista3=[]
   lista3=lista3+lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]
   return lista3