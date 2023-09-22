def uppCons(frase):
    '''	Função que transforma toda consante em maiuscula
    enquanto a demais continuam as mesmas
    entrada=string
    saida=string'''
    h=''
    i=0
    while i<len(frase):
        if frase[i] in 	'qwrtyhpçlkjhgfdszxcvbnm':
            h= h+frase[i].upper()
        else:
            h=h+frase[i]
        i=i+1
    return h