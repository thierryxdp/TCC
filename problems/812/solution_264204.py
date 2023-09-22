def retira_pontuacao(frase):
    
    pont== p1= str.join(' ',str.split(frase,'-'))
           p2= str.join(' ',str.split(frase,'.'))
           p3= str.join(' ',str.split(frase,','))
           p4= str.join(' ',str.split(frase,';'))
           p5= str.join(' ',str.split(frase,':'))
           p6= str.join(' ',str.split(frase,'?'))
           p7= str.join(' ',str.split(frase,'!'))
           p8= str.join(' ',str.split(frase,'...'))
        
        
        
    return str.count(pont,'.')+str.count(pont,',')+str.count(pont,'!')+str.count(pont,';')+str.count(pont,'?')+str.count(pont,''...')+str.count(pont,':')+str.count(pont,'-')+str.count(pont'.')