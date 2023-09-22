# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Dado uma frase, é retornado o número de palavras
    que esta frase contém
    entrada:str
    saída:int'''
    x = str.count(frase,'.','!','?','&')
    return str.count(x,".")+str.count(x,"!")+str.count(x,"?")+str.count(x,"&")