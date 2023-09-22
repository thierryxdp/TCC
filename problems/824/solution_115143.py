def uppCons (frase):
    con='b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z','ç'
    i=0
    while i < len(frase):
          if frase[i] in con:
            frase=frase.replace(frase[i],frase[i].upper())    
          i=i+1
    return frase
'''funcao que recebe uma frase como parametro e retorna
a frase com todas as suas consoantes em letra maiúscula
str->str'''