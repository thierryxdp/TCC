def conta_frases(abc):
      t1=str.split(abc,'...')
      t2=str.join('.',t1)
      
      return t2.count('?')+t2.count('!')+t2.count('.')
       
       #dps de 15h tentando consegui. no começo 
        #subustitui os 3 pontos por 1 só, pois na contagem 
        #dos pontos os 3 é considerado só uma pausa.
        #então a função cont conta qnts vezes aparece 
        #o final de uma frase
        # o certo seria utilizar a função slit e utilizar o 
        #caracter que finaliza uma frase, porem, não consegui funcionar 
        #aqui, somente do IDLE. Vou enviar o codigo aqui
        #def s(abc):
          
       # a função slit esta unificando strings com um caracter separdor
       #especifico, e limitando para somente uma frase por caracter sepador
       # entao a função len esta contando as frases que foram unificadas com
       #o comando splt
       #s1=str.split(abc,'?',0)
       #s2=str.split(abc,'.',0)
       #s3=str.split(abc,'...',0)
       #s4=str.split(abc,'!',0)

       #return len(s1+s2+s3+s4)