def freq_palavras(frases):
    ''' funcao  que recebe  uam string e retorna um dicionario; 
    str-> dicionario'''
    dici={}
    frases=frases.split()
    for pal in frases:
        if pal not in dici:
            dici[pal]=frases.count(pal)
            
           
    return dici