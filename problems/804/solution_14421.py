#Start your python function here
def filtra_pares(tupla):
    return [n for n in tupla if n%2 != 0]
tpl=(1,2,3,4)
lst= filtra_pares(tpl)
print (tpl)
print (lst)