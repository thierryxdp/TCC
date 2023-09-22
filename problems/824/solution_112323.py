def uppCons(frase):
    """Funcao que recebe uma frase como valor de entrada
    e retorna a frase com todas as suas consoantes em maiusculo.
    Os demais caracteres ficam exatemente como estavam na frase original;
    str -> str"""
    contador=0
    acumulador=''
    while contador<len(frase):
        if not frase[contador] in 'AEIOUaeiouÁÉÍÓáéíóÀàÃã':
            acumulador+=str.upper(frase[contador:contador+1])
        else:
            acumulador+=frase[contador]
        contador+=1
    return acumulador