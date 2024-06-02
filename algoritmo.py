def main():
    # Declaração dos vetores
    vetor1 = [''] * 10
    vetor2 = [''] * 10
    vetor_uniao = [''] * 20

    # Entrada de dados para o vetor1 e vetor2
    for i in range(10):
        vetor1[i] = input(f"Digite o caractere para o vetor1 na posição {i}: ")
        vetor2[i] = input(f"Digite o caractere para o vetor2 na posição {i}: ")

    # Construção do vetor_uniao
    for i in range(10):
        vetor_uniao[i] = vetor1[i]
        vetor_uniao[i + 10] = vetor2[i]

    # Exibir os vetores
    print("Conteúdo do vetor1: ")
    for i in range(10):
        print(vetor1[i], end=" ")
    print()  # Para quebrar a linha

    print("Conteúdo do vetor2: ")
    for i in range(10):
        print(vetor2[i], end=" ")
    print()  # Para quebrar a linha

    print("Conteúdo do vetor_uniao: ")
    for i in range(20):
        print(vetor_uniao[i], end=" ")
    print()  # Para quebrar a linha

# Execução da função principal
if __name__ == "__main__":
    main()