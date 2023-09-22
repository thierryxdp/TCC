def faltante(lista):
    '''Função que retorna o número da peça que está faltando no
    quebra-cabeça do Joãozinho;recebe como parâmetro uma lista com
    a numeração das peças; List--> int'''
    list.sort(lista)
    i=0
    if lista[i]!=1:
        return 1
    elif lista[len(lista)-1]!=len(lista)+1:
        return len(lista)+1
    else:
        while i<len(lista):
            if i==len(lista)-1:
            	i=len(lista)+1
            else:
                if lista[i+1]==lista[i]+1:
                    i=i+1
                else:
                    return lista[i]+1