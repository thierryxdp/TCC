def conta_frases(abc):
          
       # a função slit esta unificando strings com um caracter separdor
       #especifico, e limitando para somente uma frase por caracter sepador
       # entao a função len esta contando as frases que foram unificadas com
       #o comando splt
       s1=str.split(abc,'.')
       if len(s1)<0
         len(s1)=0
       s2=str.split(abc,'!',0)
          if len(s2)<0
        len(s2)=0
       s3=str.split(abc,'-',0)
          if len(s3)<0
        len(s3)=0
       s4=str.split(abc,'.',0)
            if len(s4)<0
        len(s4)=0
       s5=str.split(abc,'...',0)
             if len(s5)<0
        len(s5)=0
       return len(s1)+len(s2)+len(s3)+len(s4)+len(s5)