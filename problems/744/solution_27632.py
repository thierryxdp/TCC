def hashtag(x: str) -> str:
    """Adiciona hashtag(#) no início, meio e fim de uma string

       Parameters:
       x: String a ser modificada entre parênteses

       Return:
       A string representada pelo parâmetro "x", mas adicionados os hashtags(#)
       no início, meio e fim dessa string

       Examples:
       hashtag("abcd") == '#ab#cd#'
       hashtag("abcde") == '#ab#cde#'
       hashtag("oi") == '#o#i#'
    """

    a = len(x)
    b = a % 2
    
    if (b == 0):
        y = int(a / 2)
        return "#" + x[:y] + "#" + x[y:] + "#"
    else:
        z = a // 2
        return "#" + x[:z] + "#" + x[z:] + "#"