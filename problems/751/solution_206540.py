# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """essa função recebe um string contendo uma frase, contando que duas palavras são sempre separadas pos espaçoes, irei contar esses espaços revelando o nu
    mero de palavras"""
    str.rstrip(frase)
    str.lstrip(frase)
    
    return str.count(frase, ' ')+1