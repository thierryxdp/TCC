def uppCons(x):
    'recebe uma string e retorna outra string com todas consoantes em maiusculo'
    'entrada: str'
    'saida: str'
    i=0
    abc= {'b':'B','c':'C','d':'D','f':'F','g':'G','h':'H','j':'J','k':'K','l':'L','m':'M','n':'N','p':'P','q':'Q','r':'R','s':'S','t':'T','v':'V','w':'W','x':'X','y':'Y','z':'Z','Ç':'ç'}
    while i<len(x):
        if x[i] in 'bcdfghjklmnpqrstvwxyz':
          x=x.replace(x[i],abc[x[i]])
        i= i+1
    return x