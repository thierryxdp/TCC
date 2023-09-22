def substituir(frase):
    return  str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '),'!',' '),'?',' '),'-',' '),',',' '),':',' '),';',' ')



def inverte(frase):
    '''funçao que dada uma frase, inverte suas palavras e retira sua pontuação. str->str'''
    frase1= substituir(frase)

    seq1=str.split(frase1)
    seq2=seq1[::-1]

    frase2=str.join(' ',seq2)

    return frase2