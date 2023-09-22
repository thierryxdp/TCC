def hashtag(s):
    '''Esta função recebe uma string e em seu início,meio e fim, insere o caractere #
    assinatura: str -> str
    testes:
    hashtag('papel')='#pa#pel#'
    hashtag('computador')='#compu#tador#'
    hashtag('aula')='#au#la#'
    '''
    return "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"