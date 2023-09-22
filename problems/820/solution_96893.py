def posLetra(palavra,letra,num):
    '''retorna a posição da letra, dado a palavra
    e a ocorrencia desejada da letra(num). str,str,int->int'''
    posicao= 0
    n = 0
    while posicao != num:
        n=n+str.find(palavra,letra,n)+1
        posicao = posicao + 1       
    return str.find(palavra,letra,n-1)