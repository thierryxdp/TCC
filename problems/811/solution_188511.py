def colchao(medidas,H,L):
    ''' Entrada: medidas -> lista com as dimenções do colchão,
    			ordenadas da maior para a menor
                 H -> altura da porta em cm (inteiro)
                 L -> largura da porta em cm (inteiro)
        
         Saída: Função retorna True quando o colchão passa pela porta
         e False caso contrário (booleano)
         
         list,int,int -> bool'''
    
    a,b,c = medidas 
    return (a<=H and b<=L) or (a <= L and b <= H) or (a <= H and c <=L) or (a <= L and c <= H) or (c <= H and b <= L) or (c <= L and b <= H)