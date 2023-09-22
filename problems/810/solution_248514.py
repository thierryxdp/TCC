def inverte(frase):
    
    """
    str--->str
    Apesar de longo, o código se mostrou funcional. Após transformar as
    letras da frase em minusculo e retirar a pontuação delas, deve-se 
    usar o compando split para trocar a ordem das palavras com o comando
    reverse(só disponivel em listas,na qual o comando split ja transforma).
    Após isso se transforma a lista em string novamente e se retira o que
    sobrou das listas(colchetes e virgulas) para formar a string desejada.

    
    """
    
    frase0=str.lower(frase)
    frase1=str.replace(frase0,'-',' ')
    frase2=str.replace(frase1,';',' ')
    frase3=str.replace(frase2,':',' ')
    frase4=str.replace(frase3,'.',' ')
    frase5=str.replace(frase4,',',' ')
    frase6=str.replace(frase5,'?',' ')
    frase7=str.replace(frase6,'!',' ')
    
    lista1=str.split(frase7)
    lista2=lista1[::-1]
    
    frase8=str(lista2)
    frase9=str.replace(frase8,',','')
    frase10=str.replace(frase9,"'","")
    frase11=str.replace(frase10,"[","")
    
    return str.replace(frase11,"]","")