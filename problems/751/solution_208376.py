def quant_palavras(string):
    '''Dado uma string, retorna o número
       de palavras que a formam;
       str -> int'''
    nova_string = str.strip(string)
    return str.count(nova_string, ' ')+1