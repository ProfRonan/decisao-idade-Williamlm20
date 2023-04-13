numero = input('digite um numero: ')
numero = int(numero)

impossivel = False
maior = False
menor = False
velho = False

if numero < 0:
    print('impossível!')
    impossivel = True
elif numero < 18:
    print('não precisa se alistar.')
    maior = True
elif 18 < numero < 65:
    print('Não esqueça de votar na próxima eleição.')
    menor = True
elif numero > 65:
    print('Vá descansar.')
    velho = True
else:
    print('eita!')
