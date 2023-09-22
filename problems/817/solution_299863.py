def acima_da_media(notas):
        type(notas)==list
        media=sum(notas)//len(notas)
        for i in notas:
            if i >=media:
                notas.append(i)
        return sorted(notas)