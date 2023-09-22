# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''
    A função retorna a quantidade de palavras de uma frase, 
    desconsiderando espaços no inicio e final.
    
    string -> int
    '''
    frase = frase.strip()
    return len(frase.split())