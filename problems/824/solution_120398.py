def uppCons(frase):
    '''função que, dada uma frase,retorna a frase com todas as suas 
    consoantes em maiúsculo (e os demais caracteres
    exatamente como estavam na frase original).
    entrada: str
    saida: str
    '''
    i=0
    while i<len(frase):
        if frase[i] not in 'aàáâãAÁÃÂÀeéêEÉÊiíîIÍÎoóôõOÓÕÔuúûUÚÛ':
            frase= str.replace(frase,frase[i],str.upper(frase[i]))
        i=i+1
    return frase