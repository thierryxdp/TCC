def freq_palavras(frases):
    """ Funçao que retorne um dicionario em que cada palavra da string dada
    seja uma chave e tenha como valor o numero de vezes que a 
    palavra aparece"""
    
    frases_list = frases.split(" ")
    palavra_dicionario= {}

    for i in frases_list:
        if not i in palavra_dicionario.keys():
            palavra_dicionario[i] = 1
        else:
            palavra_dicionario[i] = palavra_dicionario[i] + 1

    return palavra_dicionario