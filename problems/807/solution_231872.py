def conta_frases(abc):
          
       # a função slit esta unificando strings com um caracter separdor
       #especifico, e limitando para somente uma frase por caracter sepador
       # entao a função len esta contando as frases que foram unificadas com
       #o comando splt
       conta_frases1=str.split(abc,'?',0)
       conta_frases2=str.split(abc,'.',0)
       conta_frases3=str.split(abc,'...',0)
       conta_frases4=str.split(abc,'!',0)

       return len(conta_frases1+conta_frases2+conta_frases3+conta_frases4)