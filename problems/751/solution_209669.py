# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    ''' docs '''
    
    # Passo 1. Remover espaços no inicio e final
    frase = str.strip(frase, ' ')
    
    # Passo 2. Dividir a frase em palavras
    frase_dividida = str.split(frase, ' ')
    
    # Passo 3. Contar quantas palavras existem
    qtd = len(frase_dividida)
    
    return qtd