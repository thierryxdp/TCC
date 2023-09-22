def posLetra(s,l,n):
    'recebe uma string e descobre a posição de uma letra <l> numa certa occorencia'
    count = 0
    lista1 = []
    while len(lista1)<n:
        for i in s:
            count = count + 1
            if i in l:
                lista1.append(i)
    return count