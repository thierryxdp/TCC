# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ retorna o número de palavras da frase, incluindo espaços no início e no final"""
    
    if frase[-1]=='':
        frase=frase[:-2]
        frase=frase.split('')
        
       return len(frase)
    else:
        frase=frase.split('')
        
       return len(frase)