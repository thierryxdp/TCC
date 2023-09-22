def faltante(l):
    '''funcao que retorna a peca faltante de um quebra cabeca
    entrada:list
    saida:int'''
    n=1
    while n<=len(l)+1:
        if n not in l:
            return n
        n+=1