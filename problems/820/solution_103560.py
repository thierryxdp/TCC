def posLetra(frase,letra,ocorrencia):
    '''analisa e retorna o lugar da letra na frase na ocorrencia desejada
    	str,str,int->int'''
    
    i=0
    
    while i<len(frase):
        
        frase_nova=str.replace(frase,letra,'-',ocorrencia-1)
        lugar=frase_nova.find(letra)
        i=i+1
        
    return lugar