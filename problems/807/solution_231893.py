def conta_frases(abc):
          
       # a função slit esta unificando strings com um caracter separdor
       #especifico, e limitando para somente uma frase por caracter sepador
       # entao a função len esta contando as frases que foram unificadas com
       #o comando splt
       s1=str.split(abc,'?',)
       s2=str.split(abc,'!',)
       s3=str.split(abc,'-',)
       s4=str.split(abc,'. ',)
       s5=str.split(abc,'...',)
       s6=str.split(abc,'; ',)
       

       return len(s1)-1+len(s2)-1+len(s3)-1+len(s4)-1+len(s5)-1+len(s6)-1