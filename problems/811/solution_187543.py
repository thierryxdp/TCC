def colchao(a,b,c):
    tupla1= int(a[1])
    tupla2= int(a[2])
    nu1= b
    nu2= c
    return condicao1(tupla1,nu1,nu2)
def condicao1(a,b,c):
    if a<=b or a<=c:
        return True
    else:
          return False
colchao([36, 190, 209], 187, 248)