def retira_pontuacao(frase):
    ''' dada uma frase, retorna essa frase com espaços vazios no lugar 
        dos caracteres de pontuação. 
        str-->str'''
    ponto = str.count(frase,'.')
    travessao = str.count(frase,'-')
    virg = str.count(frase,',')
    doisp = str.count(frase,':')
    pontovirg = str.count(frase,';')
    exclam = str.count(frase,'!')
    interrog = str.count(frase,'?')
    comando1 = str.replace(frase, '.' , ' ', ponto)
    comando2 = str.replace(frase, '-' , ' ', travessao)
    comando3 = str.replace(frase, ',' , ' ', virg)
    comando4 = str.replace(frase, ':' , ' ', doisp)
    comando5 = str.replace(frase, ';' , ' ', pontovirg)
    comando6 = str.replace(frase, '!' , ' ', exclam)
    comando7 = str.replace(frase, '?' , ' ', interrog)
    
    return comando7