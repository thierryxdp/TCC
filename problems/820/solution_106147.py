def posLetra(frase,letra,ocorrencia):
    vez=0
    x=0
    resultado=-1
    whilw x<len(frase):
        if frase[x].lower()== letra:
            vez+=1
        if vez == ocoreencia:
            resultado =x
            break
        x +=1
    return resultado