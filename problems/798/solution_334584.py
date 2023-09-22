def freq_palavras(frases):
    '''Função que recebe uma frase e retorna cada palavra como a chave
    	de um dicionário e seus números de repetições como os valores
        
        str -> dict'''
    
    x=str.split(frases,' ')
    d={}
    y=[]
    for i in range(len(x)):
        d[x[i]]=list.count(x,x[i])
    return d