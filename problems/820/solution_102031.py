def posLetra(string,letra,num):
#Funcao que recebe como entrada: String, uma letra e um numero
    i=0
    cont=0
    while i<len(string):
        if string[i]==letra:
            cont+=1
        if cont==num:
            return i
#Retorna em que posição da string aquela ocorrencia da letra esta
        i+=1
    if cont<num:
#Caso exista menos ocorrencia da letra do que a ocorrencia pedida a funcao retorna -1
        return -1