def retira_pontuacao(frase):
    
    pont== [p1= str.join(' ',str.split(frase,'-'))
           p2= str.join(' ',str.split(p1,'.'))
           p3= str.join(' ',str.split(p2,','))
           p4= str.join(' ',str.split(p3,';'))
           p5= str.join(' ',str.split(p4,':'))
           p6= str.join(' ',str.split(p5,'?'))
           p7= str.join(' ',str.split(p6,'!'))
           p8= str.join(' ',str.split(p7,'...'))]
        
        
        
    return str.count(pont,'.')+str.count(pont,',')+str.count(pont,'!')+str.count(pont,';')+str.count(pont,'?')+str.count(pont,''...')+str.count(pont,':')+str.count(pont,'-')+str.count(pont'.')