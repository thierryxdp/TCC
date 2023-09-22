def posLetra (string,l,o):
    '''função que retorna a posição da letra l de ocorrencia o na string;
    str,str,int->int'''
    posicao = str.find(string,l)
    while o>1:
        posicao=str.find(string,l,posicao+1)
        o=o-1
    return posicao