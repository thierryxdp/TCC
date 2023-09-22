# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
 
def quant_palavras(frase):
    '''recebe uma frase e retorna a quantidade de itens nessa mesma frase, strin->int'''
    
    
    frase2 = frase.split()
    qntd = len(frase2)
    return qntd