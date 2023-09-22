def retira_pontuacao(frase):
    
    return  str.join(' ',str.split(frase,'-'))+str.join(' ',str.split(frase,'.'))+str.join(' ',str.split(frase,','))+str.join(' ',str.split(frase,';'))+str.join(' ',str.split(frase,':'))+str.join(' ',str.split(frase,'?'))+str.join(' ',str.split(frase,'!'))+str.join(' ',str.split(frase,'...'))