def acima_da_media(notas):
    type(notas)==list
    
    def acima_da_media(notas):
        type(notas)==list
        media=()
        media=sum(notas)//len(notas)
        for i in notas:
            if i >=media:
                media.append(i)
                
        return sorted(media)