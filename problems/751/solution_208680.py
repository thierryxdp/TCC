# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """uma função que conta o número de palavras numa frase
   str->int"""
    listafrase= split(frase)
    if listafrase[0]== ' ':
        list.remove(listafrase,' ')
    if listafrase[-1]==' ':
        list.remove(listafrase,' ')
    else:
        return listafrase