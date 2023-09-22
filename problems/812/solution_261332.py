#A função dada uma frase, retorna a frase onde todos os caracteres de pontuação('-',':',';','.')
#frase: frase a ser inserida.
#string->string

def retira_pontuacao(frase):
    
        frase=str.replace(frase,'-',' ')      
    
        frase=str.replace(frase,',',' ')
    
        frase=str.replace(frase,'?',' ') 
    
        frase=str.replace(frase,'!',' ')     
   
        frase=str.replace(frase,'.',' ')
         
        frase=str.replace(frase,':',' ')
    
        frase=str.replace(frase,';',' ')
   
        frase=str.replace(frase,'?',' ') 
    
        frase=str.replace(frase,'!',' ')