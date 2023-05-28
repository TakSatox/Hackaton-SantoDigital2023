from functions import asteriscos, menor_diff, subconjuntos


while(True):
    e = int(input('Digite o número do exercício: '))
    
    if e == 1:
        n = int(input('N: '))
        response = asteriscos(n)
        print(response)


    elif e == 2:
        array = input('Digite os números separando por vírgula (1, 2, ..., N): ')
        response = menor_diff(array)
        print(response)

    elif e == 3:
        conjunto = input('Digite os números do conjunto separando por vírgula (1, 2, ..., N): ')
        response = subconjuntos(conjunto)
        print(response)