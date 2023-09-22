def uppCons(frase):
    '''retorna a frase com todas as suas consoantes em maiusculas
    sem alterar os demais caracteres
    str -> str'''
    
    i=0
    consoante=''
    
    while i < len(frase):
          if frase[i] not in 'AEIOUaeiouãéíóú':
                consoante = consoante + str.upper(frase[i])
          else:
            consoante = consoante + frase[i]
          i=i+1
        
    return consoante