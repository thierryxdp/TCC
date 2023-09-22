def posLetra(palavra,letra,num):
    """funcao que recebe uma string(palavra), um numero(num)
    e uma letra como entrada, e identifica em que posicao a letra 
    aparece na string.
    Num é o numero da ocorrencia da letra, se a letra nao 
    aparecer "num" vezes,a funcao retorna -1. 
    Aparecendo "num" vezes, a funcao retorna a posicao da 
    ocorrencia.
    entrada->str,int
    saida->int"""
    i=0
    vezes=[]
    while i<len(palavra):
        if palavra[i]==letra:
            vezes=vezes+ [i]
        i=i+1
    if num> len(vezes):
            return -1
    else: return vezes[num-1]