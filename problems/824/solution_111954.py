def uppCons(frase):
    '''Função que recebe umafrase e retorna a
    frase com todas as consoantes em maiúsculo;
    str->str'''
    indice= 0
    listafrase= list(frase)[:]
    lista= []
    
    while indice < len(frase):
        if frase[indice] not in 'AEIOUaeiou':
            listafrase= str.replace(frase,frase[indice],str.upper(frase[indice]))
        list.append(lista,listafrase[indice])
        indice +=1
    return str.join(' ',lista)