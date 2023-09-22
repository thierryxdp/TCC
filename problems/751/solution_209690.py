# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    string--->int
    O comando split separa as palavras(por estarem com o espaço umas entre
    as outras), enquanto o len faz a contagem de quantas strings a frase 
    da entrada possuía 
  
    """
    x=frase.split()
    
    return len(x)