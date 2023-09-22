def acima_da_media(a):
    t1=[i for i in a if i>sum(a)/len(a)]
    return sorted(t1)

# é defido que para o elemento fazer parte da nova lista 
# ele deve ser maior que a somo de todos os elementos, 
## divido pela quantidade existente deles. ou seja , a media