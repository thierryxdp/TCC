def conta_frases(abc):
          
       # a função slit esta unificando strings com um caracter separdor
       #especifico, e limitando para somente uma frase por caracter sepador
       # entao a função len esta contando as frases que foram unificadas com
       #o comando splt
       s1=str.split(abc,'?',0)
       s2=str.split(abc,'.',0)
       s3=str.split(abc,'...',0)
       s4=str.split(abc,'!',0)

       return len(s1+s2+s3+s4)