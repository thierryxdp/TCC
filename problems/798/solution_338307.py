# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):    
    	
    for x in str.split(frases):
        a={}
        b=list.count(str.split(frases),x)
        i={x:b}
        a.update(i)
        
        
        
        return i