from itertools import combinations


def asteriscos(n):
    #Transforma retorno em lista
    retorno = list()

    #Loop em for para repetir o laço N vezes, sendo que a cada laço é adicionado na lista uma string com N asteriscos dependendo do contador
    for _ in range(n):
        retorno.append('*' * (_ + 1))
    
    return retorno


def menor_diff(array):
    #Separa os numeros através do argumento ', ', ou seja, retirar todas as virgulas seguidas de espaço
    array = array.split(', ')
    #Transforma elemento por elemento em inteiro pois inicialmente são string apenas para fazer o split
    array = [int(n) for n in array]

    #Ordenando todos os elementos em reverse para que o maior numero sempre fique do lado esquerdo do par
    array.sort(reverse=True)

    #declara retorno como lista para receber os pares
    retorno = list()

    #declara menor como um float 'infinito'
    menor = float('inf')
    
    #Um for que irá percorrer de 0 até o tamanho - 1 da array porque desta forma no final não teremos o problema de utilizar
    #um indice que não existe ao somar array(_ + 1)
    for _ in range(len(array) - 1):
            #Atribui ao diff a diferença absoluta
            diff = abs(array[_] - array[_ + 1])

            #Se diff for igual ao menor então significa que temos mais de um par com essa diferença
            if diff == menor:
                retorno.append((array[_], array[_+1]))

            #Caso diff for menor que o menor, então novamente a lista retorno só terá um par dessa diferença
            elif diff < menor:
                menor = diff
                retorno = [(array[_], array[_ + 1])]
            
    return retorno


def subconjuntos(conjunto):
    conjunto = conjunto.split(', ')
    conjunto = [int(n) for n in conjunto]
    conjunto.sort()
    
    retorno = list()
    for _ in range(len(conjunto) + 1):
        #o segundo for faz combinações de tudo que há no conjunto até o número do _, ou seja, se estiver em 0 irá fazer combinações de 0
        #Quando estiver em 1, fará combinações de 1, em 2 combinações de 2 e isso seguindo a ordem contida no conjunto.
        for subconjunto in combinations(conjunto, _):
             retorno.append(list(subconjunto))
    
    
    return retorno