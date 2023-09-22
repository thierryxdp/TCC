def freq_palavras(string):
    """ Funçao que retorne um dicionario em que cada palavra da string dada
    seja uma chave e tenha como valor o numero de vezes que a 
    palavra aparece"""
    
    string_list = string.split(" ")
    palavra_dict = {}

    for palavra in string_list:
        if not palavra in palavra_dict.keys():
            palavra_dict[palavra] = 1
        else:
            palavra_dict[palavra] = palavra_dict[word] + 1

    return palavra_dict