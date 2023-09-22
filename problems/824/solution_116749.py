def uppCons(frase):
    '''função que recebe como entrada uma frase e retorna a frase com todas as suas consoantes em maiúsculas e os demais caracteres exatamente como estavam na frase original; str -> str'''
    i=0
    frase1=''
    while i<len(frase):
        if frase[i] in 'AEIOUÃÕÁÉÍÓÚaeiouãõáéíóú':
            frase1+=frase[i]
        else:
            frase1+=str.upper(frase[i])
        i=i+1
    return frase1