def filtraMultiplos(a,b):
    '''recebe uma lista e um numero e retorna outra lista com os multiplos desse numero'''
    '''entrada: str,int'''
    '''saida: str'''
    varia=0
    lista=[]
    while varia<len(a):
        if a[varia]%b==0:
            list.append(lista,a[varia])
        varia+=1
    return lista