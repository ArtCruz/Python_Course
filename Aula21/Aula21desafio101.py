def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos: VOTO FACULTATIVO'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
data = int(input('Que ano você nasceu? '))
print(voto(data))
print()