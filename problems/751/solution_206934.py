# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """retorna quantas palavras existem no arg frase
    o arg deve ser escrito entre aspas
    str -> int"""
    
    palavras = str.split(frase,' ')
    
    return len(palavras)