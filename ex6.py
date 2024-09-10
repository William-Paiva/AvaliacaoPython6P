cpf = input('Digite seu cpf: ')

contador = 0
sum = 0

while contador < 14:
    for x in cpf:
        if(contador == 3 | contador == 6 | contador == 9):
            sum = sum + 0
        else:
            sum = sum + x
contador = contador + contador
    
if(sum%2 == 0):
    print('cpf par')
else:
    print("cpf ímpar")