def freq_palavras(frase):
    '''Recebe uma string e retorna um dicionario no qual cada
    palavra da string seja uma chave e tenha como valor o 
    numero de vezes que cada palavra aparece;
    str->dict'''
    
    palavras = frase.split()
    dicionario = {}
    
    for i in palavras:
        contador = palavras.count(i)
        dicionario.update({i:contador})
    return dicionario