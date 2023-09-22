def posLetra(frase,letra,n):
    '''indica qual o index da ocorrencia de numero n da letra pedida na frase dada
    str,str,int-->int'''
    if(n>str.count(frase,letra)):
        return -1
    else:
        i=0
        corte=0
        index=0
        while(i<n):
            corte+=str.index(frase[corte:],letra)+1
            index+=corte-1
            i+=1
        return index