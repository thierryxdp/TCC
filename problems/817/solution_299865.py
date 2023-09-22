def acima_da_media(notas):
        type(notas)==list
        nova_lista=[]
        media=sum(notas)//len(notas)
        for i in notas:
            if i >=media:
                nova_lista=notas.append(i)
                return sorted(nova_lista)