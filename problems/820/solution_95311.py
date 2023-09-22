def posLetra (string, letra, num) :
    i=0
    contagem: 0
        if string.count(letra) >=num :
            while contagem !=num :
                if letra == string [i]:
                    contagem +=1
                    i+=1
                    return i-1
                else:
                    return -1