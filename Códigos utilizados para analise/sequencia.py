import random
import time

def sequencia(vetor, chave):

    for i in range(len(vetor)):
        if vetor[i] == chave:
            return i
    return None


def main():
    # Tamanho da sequência
    n = 10000000

    # Número de buscas a serem realizadas sobre a sequência
    q = 100000

    #Criação do vetor e do vetor de chaves
    vetor = []
    vetor_chaves= []

    #Colocando os números no vetor
    for i in range(n) :
        numero = random.randint(0, 2147483647)
        vetor.append(numero)

    #Colocando os numeros no vetor de chaves
    for i in range(q):
      numero = random.randint(0, 2147483647)
      vetor_chaves.append(numero)

    """ Teste da função sequencia com print
    resultados = []
    chaves_encontradas = 0
    start_time = time.time()
    for chave in vetor_chaves:
      result = sequencia(vetor, chave)
      resultados.append(result)
      if result is not None:
        chaves_encontradas += 1
    execution_time = time.time() - start_time
  
    print(f"Vetor: {vetor}, Chaves encontradas: {chaves_encontradas}, Tempo de execução: {execution_time} segundos")
    """
  
    # Teste da função sequencia sem print
    start_time = time.time()
    for chave in vetor_chaves:
      sequencia(vetor, chave)
    execution_time = time.time() - start_time

    print(f"Tempo de execução: {execution_time} segundos")

    


if __name__ == '__main__':
  main()