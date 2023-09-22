def freq_palavras(fraes)
''' função que recebe uma string e retorna um dicionario em que cad
 palavra da string seja uma chave e 
 tenha como valoro numero de vezes de aparição da palavra'''
palavras = frases.split()
dicionario = {}

 for i in palavras:
        contador = palavras.count(i)
        dicionario.update({i:contador})
        return dicionario