import random
import time


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
  # Tamanho da sequência
  n = 10000000

  # Número de buscas a serem realizadas sobre a sequência
  q = 100000

  #Criação do vetor e do vetor de chaves
  vetor = []
  vetor_chaves = []

  #Colocando os números no vetor
  for i in range(n):
    numero = random.randint(0, 2147483647)
    vetor.append(numero)

  #Colocando os numeros no vetor de chaves
  for i in range(q):
    numero = random.randint(0, 2147483647)
    vetor_chaves.append(numero)

  """
  # Teste da função binaria
  resultados = []
  chaves_encontradas = 0
  start_time = time.time()
  #ordenando o vetor
  vetor.sort()
  for chave in vetor_chaves:
    result = binaria(vetor, chave)
    resultados.append(result)
    if result is not None:
      chaves_encontradas += 1
  execution_time = time.time() - start_time

  print(f"Vetor: {vetor}, Chaves encontradas: {chaves_encontradas}, Tempo de execução: {execution_time} segundos")
  """
  
  # Teste da função binaria sem print
  start_time = time.time()
  vetor.sort()
  for chave in vetor_chaves:
    binaria(vetor, chave)
  execution_time = time.time() - start_time

  print(f"Tempo de execução: {execution_time} segundos")



if __name__ == '__main__':
  main()
