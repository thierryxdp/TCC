def hashtag(s):
    """Esta função recebe uma string e em seu inicio, meio e fim.
    assinatura: str -> str
    testes:
    hashtag('duda')='#du#da#'
    hashtag('alma')='#al#ma#'
    hashtag('lupa')='#lu#pa#'
    """
    return "#"+ s[:len(s)//2] + "#" + s[len(s)//2:] + "#"