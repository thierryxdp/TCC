def filtraMultiplos(L1,N):
    '''Filtra os numeros de uma lista(L1) que sao multiplos do numero(N).
    list,int->list'''
        Lista=[]
        x=0
        while x <= len(L1)-1:
                if L1[x]%N==0:
                        list.append(Lista,L1[x])
                        x = x+1
                elif x <= len(L1):
                        L1[x]%N!=0
                        x= x+1

        return Lista