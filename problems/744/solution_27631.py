def hashtag(s):
    """Função que insere o caractere '#' no início, no meio e no fim de uma string.

    str -> str"""

    if int(len(s)) % 2 == 0:

        return "#" + s[0: int(len(s)/2)] + "#" + s[int(len(s)/2):] + "#"

    else:

        return "#" + s[0: int((len(s)-1)/2)] + "#" + s[int((len(s)-1)/2):] + "#"
    
    
    
    
def teste_hashtag():
    """Função que testa a veracidade da função hashtag(s)"""
    
    print(hashtag("drogaria")) == "#drog#aria#"
    print(hashtag("bit") == "#b#it#")
    print(hashtag("troçar") == "#tro#çar#")