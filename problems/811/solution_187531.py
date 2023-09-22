def colchao(a,b,c):
    tupla1= int(a[1])
    tupla2= int(a[2])
    nu1= b
    nu2= c
    return vix(tupla1,nu1)
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
def passa1(a):
    if (a)==1:
        return True
    else:
        return False
def vix(a,b):
    if (condicao1(a,b)):
       return True 
    else:
          return False
colchao([24, 187, 207], 194, 99)