def inverte(frase):
    x = str.replace(frase,'.' , ' ')
    y = str.replace(x,',', ' ')
    z = str.replace(y,'!', ' ')
    t = str.replace(z,'-', ' ')
    i = str.replace(t,'?', ' ')  
    m = str.lower(i)
    s = str.split(m)
    l = s[::-1]
    j = str.join(' ', l)
    """ Função que dada uma frase, retorna uma outra frase
    que contenha as mesmas palavras da frase de entrada
    na ordem inversa, sem letras maiúsculas, e sem
    pontuação
    Entrada: String
    Saída : String"""       
    return j