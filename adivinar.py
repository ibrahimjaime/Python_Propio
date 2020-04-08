import random
numero = random.randint(0,2)
i=0
bucle = True
print(numero)

while bucle:
    resp = int(input('ingrese un valor: '))
    if numero == resp:
        print('ganaste')
        break
    elif numero != resp:
        i=i+1
        if i == 2:
            print('perdiste')
            break
        continue
