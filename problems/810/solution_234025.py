def inverte(frase):
    """funcao que dada uma frase retorne uma outra frase que contenha
    as mesmas palavras da frase de entrada na ordem inversa sem letra maiùscula e sem pontuaçao"""
    a = (frase[-1:]) 
string_nova = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', string_velha.decode('utf-8'))            
    lista = str.split(frase)
    lista.reverse()
    #lista = list.reverse(lista)
    frase = str.join(lista)
    return frase