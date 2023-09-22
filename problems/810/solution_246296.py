def inverte(frase):
    
    nova_frase = ""
    nova_frase = frase
    nova_frase = str.replace(nova_frase,"-","")
    nova_frase = str.replace(nova_frase,",","")
    nova_frase = str.replace(nova_frase,".","")
    nova_frase = str.replace(nova_frase,"!","")
    nova_frase = str.replace(nova_frase,";","")
    nova_frase = str.replace(nova_frase,":","")
    nova_frase = str.replace(nova_frase,"?","")
    nova_frase = str.lower(nova_frase)

    separada = str.split(nova_frase,)
    reverse = list.reverse(separada)
    return separada