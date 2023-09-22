def uppCons(frase):
    #contador
    i=0
    #acumulador - frase com consoantes em maiúsculo
    fraseConsUpp=' '
    #condição de parada: varrer toda a frase de entrada (frase)
    #ação que se repete: verificar para caractere cons é minusc torcar para maiusc
    while (i<len(frase)):
        caractere = frase[i]
        if(frase[i] in 'bcdfghjklmnpqrstwxyzç')
            caractere.upper()
        fraseConsUpp = fraseConsUpp+caractere
        i+=1
    return fraseConsUpp