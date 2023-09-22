def colchao (medidas,H,L):
    '''Função com o objetivo de saber se um colchao entra pela 
    porta. Para se passar de uma porta, pelo menos duas dimensões
    de uma face do colchão devem ser menores ou iguais que as 
    dimensões da porta. Para saber quantas dimensões do colchão
    a altura ou a largura da porta são maiores ou iguais, foi 
    criado um sistema de pontos a partir de testes if, onde a 
    dimensão da porta ganhava 1 ponto por cada dimensão do colchão
    que fosse menor. Por exemplo: se a altura fosse maior que 
    as dimensões A e B mas menor que C, a altura recebe dois 
    pontos. Por esse sistema, o colchao deve passar se pelo 
    menos uma dimensão da porta tiver 2 pontos e a outra tiver
    pelo menos 1.
    Os primeiros três testes comparam a entrada H da altura e
    as três entradas da lista medidas que corresponde ao colchão.
    Os três seguintes comparam a entrada L de largura com as 
    mesmas entradas da lista medidas. Nestes testes há a soma 
    de pontos registradas nas variáveis testealtura e 
    testelargura. O último teste compara os valores dessas
    variáveis com os valores 2 e 1 para retornar se passa ou
    não o colchão'''
    if H >= medidas[0]:
        testealtura = 1
    else:
        testealtura = 0
    if H >= medidas[1]:
        testealtura += 1
    if H >= medidas[2]:
        testealtura += 1
        
    if L >= medidas[0]:
        testelargura = 1
    else:
        testelargura = 0
    if L >= medidas[1]:
        testelargura += 1
    if L >= medidas[2]:
        testelargura += 1
        
    if (testelargura >= 2 and testealtura >=1) or (testealtura >=2 and testelargura >=1):
        return True
    else:
        return False