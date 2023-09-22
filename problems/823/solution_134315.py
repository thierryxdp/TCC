def faltante(lista):
    '''Função que retorna a peça faltante de um quebra-cabeça;
    recebe como parâmetro uma lista que contém a numeração de 
    peças do quebra-cabeça; List-->Int'''
    i=0
    list.sort(lista)
    while i<len(lista):
        if i==len(lista)-1:
            i=len(lista)+1
        else:
            if(lista[i+1]==lista[i]+1):
                i=i+1
            else:
                return lista[i]+1