# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """A função recebe uma strin contendo uma frase ou uma palavra, a função removbe os espaçoes vazios do inicio e fim e 
    conta o numero de espaços vazios e a partir disso o numero de palavras será o numero de 
    espaçoes vazio mais um.
    string------>int
    exemplo:
    entrada = 'leo lucena saida = 2
    entrada = 'leo'       saida = 1'"""
    frase1 = str.strip(frase)
    return(str.count(frase1, " ")+1)