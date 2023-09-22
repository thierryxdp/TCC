def hashtag(s):
    'str -> str ; Função que retorna uma string intercalada de # em palavras com caracteres pares e impares'
    x=len(s)
    y=len(s)/2
    if s%2==0:
        return '#'+s[0:int(y)]+'#'+s[int(y):int(x)]+'#'
    if not(s%2==0):
        y=len(s)//2
        return '#'+s[0:int(y)]+'#'+s[int(y):int(x)]+'#'