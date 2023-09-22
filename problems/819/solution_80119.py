def filtraMultiplos(li,num):
    '''Verifica na lista li se há um número que é multiplo
    de número num
    list,int->list'''
    filtrados=[]
    i=0
    while i<len(li):
        if li[i]%num==0:
        	filtrados=filtrados+[li[i]]
        i=i+1
    return filtrados