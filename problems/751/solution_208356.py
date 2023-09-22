# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída
       str->int"""
    a=str.strip(frase,'.')
    a=str.strip(frase,'...')
    a=str.strip(frase,'!')
    a=str.strip(frase,'?')
    
    return len(str.split(a))