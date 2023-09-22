def inverte(frase):
    ponto=frase.replace('.',' ')
    virgula=ponto.replace(',',' ')
    pontovirg=virgula.replace(';',' ')
    exclamacao=pontovirg.replace('!',' ')
    interrogacao=exclamacao.replace('?',' ')
    travessao=interrogacao.replace('-',' ')
    reticencia=travessao.replace('...',' ')
    ponto2=reticencia.replace(':',' ')
    frase2=ponto2.split(' ')
    list.reverse(frase2)
        
       if frase2[0]==' '
       del frase2[0]
       
       return' '.join(frase2)