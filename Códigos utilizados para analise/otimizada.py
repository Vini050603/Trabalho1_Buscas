import random
import time


def sequencia_otimizada(vetor, chave):

    for i in range(len(vetor)):
        if vetor[i] == chave:
            return i
        elif vetor[i] > chave:
            return None
    return None


def main():
    # Tamanho da sequência
    n = 100000
    # Número de buscas a serem realizadas sobre a sequência

    q = 100

    # Criação do vetor e do vetor de chaves
    vetor = []
    vetor_chaves = []

    # Colocando os números no vetor
    for i in range(n):
        numero = random.randint(0, 2147483647)
        vetor.append(numero)

    # Colocando os numeros no vetor de chaves
    for i in range(q):
        numero = random.randint(0, 2147483647)
        vetor_chaves.append(numero)

    # Teste da função sequencia_otimizada
    vetor.sort()
    # Teste da função sequencia otimizada sem print
    start_time = time.time()

    for chave in vetor_chaves:
        sequencia_otimizada(vetor, chave)
    execution_time = time.time() - start_time

    print(f"Tempo de execução: {execution_time} segundos")


if __name__ == '__main__':
    main()
