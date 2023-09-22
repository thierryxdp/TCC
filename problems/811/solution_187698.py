# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas: list[int], h: int, l:int) -> bool:
    '''Recebe dimenções do colchão, a altura da porta e largura da porta. Retorna se é possível
    passar com o colchão pela porta'''
    
    #É possível deitar e girar o colchão para não ter que se procupar com o lado maior
    #Atribuido à variáveis o menores lados, que serão usados na comparação
    lado1 = medidas[0]
    lado2 = medidas[1]
    
    #Considerando que a porta é retangular, entao h > l
    if(lado1 < l and lado2 < h):
        return true
    else:
        return false