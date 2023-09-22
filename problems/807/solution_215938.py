def conta_frases(frase):
    '''função que retorna a quantidade de frases que existe de entrada, tal que
o separador de cada frase são os pontos: final, exclamação, interrogação e
reticências, tal que quando separados os pontos de exclamação e interregação
não serão repetidos;
string->int'''
    a = str.find(frase,'.')
    b = str.find(frase,'!')
    c = str.find(frase,'?')
    d = str.find(frase,'...')

    a1= str.split(frase[:a],'.')
    b1= str.split(frase[a:b],'!')
    c1= str.split(frase[b:c],'?')
    d1= str.split(frase[c:d],'...')

    frase_nova = (a1+b1+c1+d1)

    return len(frase_nova)