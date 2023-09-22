def hashtag(s):
    'retorna a string s de modo que esta agora tenha o caractere # no comeco, meio e fim. Str->str'
    return '#'+s[:int((len(s))/2)]+'#'+s[int((len(s))/2):]+'#'