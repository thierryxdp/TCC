# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''
       Funçao que recebe uma lista com as medidas do colchao e mais dois numeros
       que sao as medidas da porta e retorna se o colchao vai ou nao vai passar
       pela porta
       list, int, int -> bool
    '''
    if H > medidas[0] or H > medidas[1] or H > medidas[2] or L > medidas[0] or L > medidas[1] or L > medidas[2]:
        return True
    else: 
        return False