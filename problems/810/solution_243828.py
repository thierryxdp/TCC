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
    comando2 = str.replace(comando1, '-' , ' ', travessao)
    comando3 = str.replace(comando2, ',' , ' ', virg)
    comando4 = str.replace(comando3, ':' , ' ', doisp)
    comando5 = str.replace(comando4, ';' , ' ', pontovirg)
    comando6 = str.replace(comando5, '!' , ' ', exclam)
    comando7 = str.replace(comando6, '?' , ' ', interrog)
    minusc = str.lower(comando7)
    dividir = str.split(minusc)
    invert = dividir[::-1]
    frase_final = str.join(' ', invert)
    return frase_final