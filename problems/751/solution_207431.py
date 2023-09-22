# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Função que retorna a quantidade de palavras da informação "frase" de entrada: str -> int'''
    
    palavras = str.split(frase)
    
    return len(palavras)