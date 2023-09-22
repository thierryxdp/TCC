def posLetra (string,L,numero):
    """função que dado uma string, uma letra e um número
    a função calcula e identifica a posição da letra indicada no 'número' de ocorrências, 
    da esquerda para a direita 
    1= indice da letra L que aparecer primeiro
    2= imdice da letra L que aparecer em segundo ...
    exemplo:
    posLetra ('carro','r',1)
    2
    posLetra ('carro','r',2)
    3
    posLetra ('carro','o',1)
    4
    
    índices da str'carro'
    c=0 a=1 r=2 r=3 o=4
    
    caso exista menos ocorrência da letra do que a ocorrência pedida
    a função retorna -1
    
    entrada->str,str,int
    retorna->int"""
    
    indice=0
    
    rep=0 
    
    if str.count(string,L)<numero:
        return -1
    else:
        while rep < numero:
            indice=str.find (string,L,indice)
            rep=rep+1
            indicestring= +indice 
        return indicestring