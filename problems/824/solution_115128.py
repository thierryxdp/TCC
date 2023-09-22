def uppCons(frase):
    '''função que deixa todas as consoantes de uma frase,frase, em maiúsculo, exceto vogais'''
    ponto=0
    cons=[]
    while ponto< len(frase):
        if str.lower(frase[ponto]) in "bcdfghjklmnpqrstvxywzç":
            list.append(cons, str.upper(frase[ponto]))
        else:
            list.append(cons,frase[ponto])
        ponto=ponto+1    
    return str.join("", cons)