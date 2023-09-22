# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que retorna o numero de palavras que possui na frase. str->int"""
    frase1 = str.strip(frase)
    frase2 = str.split(frase1)
    frase3 = str.join(' ',frase2)
    frase4 = str.replace(frase3,frase3[-1:],' ')
    frase10 = str.count(frase4,' ')
    return frase10