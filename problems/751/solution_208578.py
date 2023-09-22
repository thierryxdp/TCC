# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que calcula a quantidade de palavras numa Frase em String
    String -> int"""
    
   	listaFrase = str.split(frase, " ")
    return len(listaFrase)