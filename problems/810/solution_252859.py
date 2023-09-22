def inverte(frase):
    '''Funçao que, dada uma frase, retorne a
frase onde todos os caracteres de pontuaçao sao substituidos por
espaço. str->str'''
    repor0=frase.replace('.',' ')
    repor1=repor0.replace('?',' ')
    repor2=repor1.replace('...',' ')
    repor3=repor2.replace('!',' ')
    repor4=repor3.replace(';',' ')
    repor5=repor4.replace('-',' ')
    repor6=repor5.replace(',',' ')
    repor7=repor6.replace(':',' ')
    return repor7.split(' ').reverse().join('')