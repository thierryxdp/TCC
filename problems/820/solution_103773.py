def posLetra(string,l,n):
    a = string.count(l)
    i = frequencia = 0
    if n <= a:
        while n != frequencia:
            if string[i]!=str(l):
                i+=1
            if string[i]==str(l):
                    frequencia +=1
            if frequencia == n:
                break
            i+=1
        return i
    else:
        return -1