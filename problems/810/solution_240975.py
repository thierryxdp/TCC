def inverte(frase1):
    """função que retira pontuação de uma frase
    str -> str"""
    
    frase2=frase1.replace('-',' ')  
    frase3=frase2.replace(',','')
    frase4=frase3.replace(':','')
    frase5=frase4.replace(';','')
    frase6=frase5.replace('.','')
    frase7=frase6.replace('!','')
    frase8=frase7.replace('?','')
    
    frase_lista=frase8.split(' ')
    range_lista=(len(frase_lista)+1)
    fatiamento_inverso = frase_lista[-1:-(range_lista):-1]
    inverso = str.join(' ', fatiamento_inverso)
    
    return str.lower(inverso)