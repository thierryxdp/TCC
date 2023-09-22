# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas:list, h:int, l:int)->bool:
    c=medidas[1]
    if c>h and c>l:
        return False
    elif c<=h or c<=l:
        return True
    '''Recebe as medidas do colchão e dois números que representam
    a altura(h) e largura (l) da porta, retornando se o colchão 
    passa (True) ou não (False) pela porta.'''