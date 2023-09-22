def retira_pontuacao(frase):
    '''retorna a frase escrita no arg substituindo todas as pontuacoes
    por espaco
    str -> str'''

    a = str.count(frase , '-')
    b = str.count(frase , ',')
    c = str.count(frase , ':')
    d = str.count(frase , ';')
    e = str.count(frase , '.')
    f = str.count(frase , '!')
    g = str.count(frase , '?')

    if a != 0 or b!= 0 or c!=0 or d!=0 or e!=0 or f!=0 or g!=0:

        spont_1 = str.replace(frase , '-' , ' ')
        spont_2 = str.replace(spont_1 , ',' , ' ')
        spont_3 = str.replace(spont_2 , ':' , ' ')
        spont_4 = str.replace(spont_3 , ';' , ' ')
        spont_5 = str.replace(spont_4 , '.' , ' ')
        spont_6 = str.replace(spont_5 , '!' , ' ')
        spont_7 = str.replace(spont_6 , '?' , ' ')

        
    return spont_6

    else:
        return frase