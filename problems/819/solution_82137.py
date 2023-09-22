def filtraMultiplos(L1,M):
        Lista=[]
        x=0
        while x <= len(L1)-1:
                if L1[x]%M==0:
                        list.append(Lista,L1[x])
                        x = x+1
                elif x <= len(L1):
                        L1[x]%M!=0
                        x= x+1

        return Lista