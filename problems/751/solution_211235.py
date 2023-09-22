def quant_palavras(frase):
    '''dada uma string de uma frase, retorna a quantidade de palavras na frase; str -> int'''
    lista = []
    lista[:] = frase
    if frase[0] == ' ' and frase[-1] == ' ':
        return list.count(lista,' ') - 1
    elif (frase[0] == ' ' and frase[-1] != ' ') or (frase[0] != ' ' and frase[-1] == ' '):
        return list.count(lista,' ')
    else:
        return list.count(lista,' ') + 1