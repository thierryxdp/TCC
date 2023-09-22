def conta_frases(texto):
    '''função que retorna a quantidade de frases que existe de entrada, tal que
o separador de cada frase são os pontos: final, exclamação, interrogação e
reticências, tal que quando separados os pontos de exclamação e interregação
não serão repetidos;
string->int'''
    a = str.find(texto,'.')+1

    texto_completo = str.split(str.replace(str.replace(str.replace(texto,'!','.'),'?','.'),'...',''),'.')
    texto_apenas_ponto = str.split(str.replace(texto[a::-1],'.',''),'.')

    if str.count(texto,'.')==str.count(texto,'!')==str.count(texto,'?')==str.count(texto,'...'):
        return len(texto_completo)
    elif str.count(texto,'.')>1 and (str.count(texto,'!')==str.count(texto,'?')==str.count(texto,'...'))==0:
        return len(texto_apenas_ponto)