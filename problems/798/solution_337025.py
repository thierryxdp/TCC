def freq_palavras (frase):
    '''
    função que recebe uma string e retorna um dicionario onde cada ´palavra da string seja uma chave e tenha
    como valor o número de vezes que uma palavra aparece
    str-->dict
    '''
   
    dicio={}
    lista=frase.split(' ')
    for el in lista:
        list.count(lista,el)
        dicio[el]=(list.count(lista,el))
    return dicio