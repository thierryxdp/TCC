def posLetra(frase,letra,n):
    '''Função que recebe uma string uma letra e um número e retorna em que posição
da string aquele número da letra está
Entrada(string,letra,int)
Saída(int)'''
    tamanho=len(frase)
    indice=0
    achei=False
    retorno=-1
    contador=0
    while indice < tamanho and not achei:
        if frase[indice]==letra:
            contador+=1
        if contador==n:
            retorno=indice
            achei=True
        indice+=1
    return retorno