def posLetra(s,l,n):
    'recebe uma string e descobre a posição de uma letra <l> numa certa occorencia'
    x = s.count(l)
    count = 0
    lista1=[]
    if x < n:
        return -1
    for i in s:
        if i in l:
            lista1.append(i)
        if len(lista1) == n:
            return count
        count = count+1
        
    return count