def filtraMultiplos (listaN,n):
    lResul=[]
    proximoN=0
    while proximoN<len(listaN):
        if listaN[proximoN]%n==0:
            lResul=lResul+[listaN[proximoN],]
        proximoN=proximoN+1
    return lResul
'''dado uma lista e um numero como parametro, 
retorna uma lista com os multiplos do numero
list,int->list'''