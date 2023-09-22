def uppCons(frs):
    ''' Função que retorna frase com as suas consoantes maiuscula
        str--->str'''
    i=0
    consoantes = ''
    while i<len(frs):
        if frs[i]in 'b, c, d, f, g,,h j, k, l, m, n, p, q, r, s,t,v,w, x,z':
           consoantes+=str.upper(frs[i])
        elif frs[i]in'a,e,i,o,u,ã,õ':
            consoantes+=str.lower(frs[i])
        elif frs[i]in'A,E,I,O,U,Ã,Õ':
            consoantes+=str.upper(frs[i])
        elif frs[i]in ' ':
            consoantes+= ' '
        elif frr[i] in '!':
            consoantes+= '!'
        elif frr[i] in '?':
            consoantes+= '?'
        elif frr[i] in '.':
            consoantes+='.' 
        elif frr[i] in ',':
            consoantes+= ','
        
        i+=1
    return consoantes