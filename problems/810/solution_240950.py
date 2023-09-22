def inverte(frase1):
    """função que retira pontuação de uma frase
    str -> str"""

    frase2=frase1.replace('-',' ')  
    frase3=frase2.replace(',',' ')
    frase4=frase3.replace(':',' ')
    frase5=frase4.replace(';',' ')
    frase6=frase5.replace('.',' ')
    frase7=frase6.replace('!',' ')
    frase8=frase7.replace('?',' ')
    
   
    list_frase = frase8.split(' ')
    list_frase[-1:len(list_frase)-1:-1]
    Frase_inv=list_frase.join(' ')
    return Frase_inv