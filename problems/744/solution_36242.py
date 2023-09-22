def hashtag(s):
    "Função que recebe uma string e retorna a mesma string"
    return '#' + s[:len(s)//2:] + '#' + s[:len(s)//2:] + '#'