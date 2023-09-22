# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''
       funcao que transforma uma lista
       de string em substrings, e retorna quantas 
       substrings contem na lista
       
       builtin_function_or_method-> int
       
    
    '''
    p=str.strip(frase)
    s= str.split(p)
    return len(s)