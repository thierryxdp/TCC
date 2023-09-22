def quant_palavras(frase):
    """funcao que dada uma frase de entrada, retorna o numero
    de palavras dessa frase;
    string -> int"""
    
    if (frase[0] == '' and not frase[-1] == '') or (not frase[0] == '' and frase[-1] == ''):
        return str.count(frase,'')
    elif frase[0] == '' and frase[-1] == '':
        return str.count(frase,'') - 1
    else:
        return str.count(frase,'') + 1