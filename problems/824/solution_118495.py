def uppCons(frs):
    ''' Função que retorna frase com as suas consoantes maiuscula
        str--->str'''
    i=0
    consoantes = ''
    while i<len(frs):
        if frs[i]in 'b, c, d, f, g,,h j, k, l, m, n, p, q, r, s,t,v,w, x,z':
           consoantes+=str.upper(frs[i])
        elif frs[i]in'a,e,i,o,u,ã,õ,í,ó,á,ú,ô,â,é':
            consoantes+=str.lower(frs[i])
        elif frs[i]in'A,E,I,O,U,Ã,Õ,Í,Ó,Á,Ú,Ô,Â,É':
            consoantes+=str.upper(frs[i])
        elif frs[i]in ' ':
            consoantes+= ' '
        elif frs[i] in '!':
            consoantes+= '!'
        elif frs[i] in '?':
            consoantes+= '?'
        elif frs[i] in '.':
            consoantes+='.' 
        elif frs[i] in ',':
            consoantes+= ','
        elif frs[i]in 'B, C, D, F, G,,H J, K, L, M, N, P, Q, R, S,T,V,W, X,Z':
            consoantes+= str.upper(frs[i])
        elif frs[i] in '-':
            consoantes+= '-'
        i+=1
    return consoantes