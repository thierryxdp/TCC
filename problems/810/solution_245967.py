def retira_pontuacao(frase):
    '''funcao que substitui pontuacoes por espacos.str->str'''
    frase_nova1=str.replace(frase,'.',' ')
    frase_nova2=str.replace(frase_nova1,',',' ')
    frase_nova3=str.replace(frase_nova2,'?',' ') 
    frase_nova4=str.replace(frase_nova3,'!',' ')
    frase_nova5=str.replace(frase_nova4,'-',' ')
    return frase_nova5
def letra_minuscula(palavras):
    '''funçao que deixa a frase com letras minusculas.str->str'''
    frase_nova6= str.lower(frase_nova5)
    return frase_nova6
def inverte(frases):
    '''funçao que calcula e retorna a frase sem acentos, com letras minusculas e invertida.str->str'''
    frase_nova7=str.reverte(frase_nova6)
    return frase_nova7