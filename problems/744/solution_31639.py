"retorna uma string com o caractere '#' no começo, meio e fim da mesma"
def hashtag(s):
    return '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'