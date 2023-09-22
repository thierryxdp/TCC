def divisores(numero):
    ''' função que recebe um numero e retorna a quantidade 
    de divisores desse numero.
    float -> int
    Explicação: para um numero ser divisivel por outro, o resto
    de sua divisão deve ser zero, por isso usamos o for para rodar o valor 
    de e depois verificamos se ele tem divisores, por fim contamos quantos.'''
    div=[]
    for c in range(1,numero+1):
        if numero%c==0:
            div=(div+[c])
    return len(div)