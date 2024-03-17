import time
import numpy


def binaria(vetor, chave):
    base = 0
    topo = len(vetor) - 1
    while base <= topo:
        meio = (base + topo) // 2
        if vetor[meio] == chave:
            return meio
        elif vetor[meio] < chave:
            base = meio + 1
        elif vetor[meio] > chave:
            topo = meio - 1
    return None


def main():
    n = 10000
    q = 100

    vetor = numpy.random.randint(0, 2147483647, n)
    vetor_chaves = numpy.random.randint(0, 2147483647, q)

    start_time = time.time()
    vetor.sort()
    for chave in vetor_chaves:
        binaria(vetor, chave)
    execution_time = time.time() - start_time

    print(f"Tempo de execução: {execution_time} segundos")


if __name__ == '__main__':

    main()
