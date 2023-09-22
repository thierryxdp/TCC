# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    """ Dado uma frase retorna um dicionário qu indica quantas vees cada palavra da frase foi epetida.
    entrada string -> saida dicionario. """
   	
    dicionario = {}
    
    for proximo in frases:
        if proximo not in dicionario:
            dicionario[proximo] = 1
        else:
            dicionario[proximo] = dicionario[proximo] + 1
    return dicionario