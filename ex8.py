notas = [5,7,3,4]
somatoria = 0

for nota in notas:
    somatoria = somatoria + nota

media = somatoria/4

if(media > 7):
    print('Aprovado!')
else:
    notaProvaFinal = 10
    media = (media + notaProvaFinal)/2
    if(media>5):
        print('Aprovado')
    else:
        print('Reprovado')    