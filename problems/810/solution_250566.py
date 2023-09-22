def inverte(frase):
    frase=str.replace(frase,";","")
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,"!","")
    frase=str.replace(frase,";","")
    frase=str.replace(frase,"?","")
    frase=str.replace(frase,",","")
    frase=str.replace(frase,":","")
    frase=str.replace(frase,".","")
    
    frase_2=str.lower(frase)
    lista=str.split(frase_2,' ')
    lista_2=lista[::-1]
    return str.join(" ",lista_2)
'''funcao que fornecida uma frase, retorna uma outra frase que contem as mesmas palavras da frase original na ordem inversa, sem letras maiusculas e pontuacao.
entrada:str
saida:str'''