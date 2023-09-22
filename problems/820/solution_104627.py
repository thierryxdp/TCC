def posLetra(frase,letra,p):
    '''retorna em que posição da string aquela ocorrência da letra está , caso existam menos ocorrências do que a pedida, a função deve restornar -1
    string, string, int-> int'''
    i=0
    ocorrencia=[]
    while i<=len(frase):
        if frase[i]==letra:
            ocorrencia += ocorrencia[i]
        if (len(ocorrencia+1) <= p:
           return -1
        if (len(ocorrencia)+1) > p:
            return ocorrencia[p-1]
      i = i+1
   return ocorrencia