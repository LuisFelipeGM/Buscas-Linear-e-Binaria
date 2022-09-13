# Busca Linear
# Exemplo lista.index(item)

def busca_linear(valor, lista):
    for i in lista:
        if i == valor:
            return i
    return None

def busca_linear2(valor, lista):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return None

def busca_linear3(valor, lista):
    for i, item in enumerate(lista):
        if item == valor:
            return (i, valor)

#Principal
lista = [3, 5, 5, -2, 10, 20, 30]
print(f'Item : {busca_linear(10, lista)}')
print(f'Indice : {busca_linear2(10, lista)}')
print(busca_linear3(5, lista))