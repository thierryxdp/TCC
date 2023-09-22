def hashtag(string):
    "dado uma string retorne o caractere no inicio, meio e fim. str-->str"
        return ('#'+ string[ :len(string)//2] + '#' + string[len(string)//2: ] + '#')