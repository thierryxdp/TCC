def retira_pontuacao(frase):
    '''Dada uma frase, a função retorna a frase sem os caracteres
    str -> str'''
    palavra = str.replace(frase,'?',' ')
    palavra = str.replace(palavra,'.',' ')
    palavra = str.replace(palavra,',',' ')
    palavra = str.replace(palavra,'!',' ')
    palavra = str.replace(palavra,'-',' ')
    return palavra


def inverte(frase):
    '''Dada uma frase, a função inverte, deixa-a em minuscula e 
    retira a pontuação, retornando uma frase com as alteraçoes
    str->str'''
    frase = frase[0:-1]
    frase = retira_pontuacao(str.lower(frase))
    frase = str.split(frase,)
    list = frase
    list.reverse()
    a = str.join(' ',list)
    
    return a