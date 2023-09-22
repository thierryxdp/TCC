def uppCons(frase):
    '''funçao que recebe uma frase de entrada e retorna 
    esta mesma frase com todas as suas consoantes maiusculas e
    os demais caracteres iguais aos da frase original; str->str'''
    i=0
    nf=''
    while i<len(frase):
        if frase[i] not in 'a,e,i,o,u,à,á,ã,é,ê,í,ô,ó,ú':
            x=x+str.upper(frase[i])
        else:
            nf=nf+frase[i]
        i=i+1
    return nf