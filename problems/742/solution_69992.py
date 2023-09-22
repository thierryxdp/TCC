def substitui(s,x,i):
    ''' Função que recebe uma strig s,um caractere x e um número inteiro entre 0 e o
    comprimento da strig, e retorna uma strig parecida com a strig de entrada, porém
    com o elemento da posição i alterado para o caracter x
    str,str,int -> strg '''
    

    posicao = i+1
    nova_s =  s[:i]+s[posicao:]
    return nova_s[:i]+ x + s[posicao:]