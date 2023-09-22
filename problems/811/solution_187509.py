# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(a,b,c):
    tupla= a[0]
    tupla1= tupla[1]
    tupla2= tupla[2]
    nu1= b
    nu2= c
    return vix(tupla1,nu1,tupla2,nu2)
def condicao1(a,b):
    if a<=b:
        return 1
    else:
          return 2
def condicao2(a,b):
    if a<=b:
        return 1
    else:
          return 2
def passa1(a,b):
    if condicao1(a,b)==1:
        return True
    else:
        return False
def passa2(a,b):
    if condicao2(a,b)==1:
        return True
    else:
        return False
def vix(a,b,c,d):
    if condicao1(a,b)==condicao2(c,d):
        return True 
    else:
          return False