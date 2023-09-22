def retira_pontuacao(f):
    '''usamos a funcao str.replace('x','y') para substituir o tipo de caracter que
    desejamos substituir (x) pelo que queremos colocar (y), criamos uma nova string
    que contanha os valores ja substituidos, ate acabar as substituicoes, por final
    retornamos a ultima string apos todas as alteracoes
    string -> string'''
    x=f.replace(".", " ")
    y=x.replace(":", " ")
    z=y.replace(";", " ")
    w=z.replace("-", " ")
    q=w.replace(",", " ")
    e=q.replace("?", " ")
    r=e.replace("!", " ")
    return r