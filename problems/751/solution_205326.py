# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que dada uma frase, conta o número de caracteres que ela ocupa,podendo ter espaçoes no incio e fim"""
    
    return len(str.strip(frase," "))