def busca(string,matriz):
    '''funçao que recebe uma string e uma matriz e faz uma busca pelo
certo da empresa, dado o seu nome, e retorna uma lista com os dados de
todos do setor.
'list -> list'''
    busca=[]
    contador=0
    for linha in matriz:
        if string in linha:
            busca+=[linha,]
            busca[contador].remove(string)  
            contador+=1
    return busca