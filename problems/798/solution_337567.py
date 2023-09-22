def freq_palavras(string):
    """ Funçao que retorne um dicionario em que cada palavra da string dada
    seja uma chave e tenha como valor o numero de vezes que a 
    palavra aparece"""
    
    string_list = string.split(" ")
    palavra_dict = {}

    for palavra in string_list:
        if not palavra in palavra_dict.keys():
            result_dict[palavra] = 1
        else:
            result_dict[palavra] = result_dict[word] + 1

    return result_dict