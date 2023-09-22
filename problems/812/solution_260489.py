def retira_pontuacao(frase):
    '''Recebe uma frase e retorna essa frase com espaços no lugar da pontuação (travessão, 
    virgula, dois pontos, ponto e virgula, ponto final, exclamação, interrgação e reticências)'''
    a = str.join(' ',srt.split(texto,'-'))
    b = str.join(' ',srt.split(a,','))
    c = str.join(' ',srt.split(b,':'))
    d = str.join(' ',srt.split(c,';'))
    e = str.join(' ',srt.split(d,'...'))
    f = str.join(' ',srt.split(e,'!'))
    g = str.join(' ',srt.split(f,'?'))
    h = str.join(' ',srt.split(g,'.'))
    return str.strip(h)