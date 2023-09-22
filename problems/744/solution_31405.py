def hashtag(string):
    "dado uma string retorne o caractere no inicio, meio e fim. str-->str"
    if len(string)//2:
        return ('#'+ string[0:2] + '#' + string[2: ] + '#')