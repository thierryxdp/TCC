# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''
       funcao que retorna uma lista
       com as substrings de string
    
    '''
    p=str.strip(frase)
    s= str.split(p)
    return len(s)