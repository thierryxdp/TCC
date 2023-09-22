def hashtag(s):
    """ retorna a uma string dada pelo paramentro 's' com
    	o caractere '#' no inicio, meio e fim da palavra
        str --> str"""
    
    string = '#' + s[:(len(s)//2)] + '#' + s[(len(s)//2):] + '#'

    return string