# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que dada uma frase, retorna o número de palavras da frase. Ent-> string  Saida-> int """
    
    frase = frase.strip()
    
    lista = frase.split(' ')
    
    return len(lista)