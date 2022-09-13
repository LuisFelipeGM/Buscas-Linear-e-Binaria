def busca_binaria(valor, lista):
    inicio = 0
    fim = len(lista) - 1

    while(inicio <= fim):
        # O // pega somente numero inteiro das divisões
        meio = (inicio + fim) // 2
        if valor == lista[meio]:
            return valor
        elif valor < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1