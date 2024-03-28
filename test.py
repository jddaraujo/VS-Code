import random

# Lista de piadas
jokes = [
    "Por que o elefante não pega fogo? Porque ele já é cinza!",
    "Qual é o fim da picada? Quando o mosquito vai embora.",
    "O que é um pontinho vermelho no meio da sala? Uma cereja perdida.",
    "Por que o boi foi para o espaço? Para encontrar a vaquinha de estimação.",
    "O que o tomate foi fazer no banco? Tirar extrato.",
    "O que é um pontinho vermelho no meio da geladeira? Um morango de castigo.",
    "O que é um pontinho verde no meio do mar? Um pinto nadando de cueca.",
    "Qual é o contrário de volátil? Vem cá, sobrinho.",
    "Por que o cachorro entrou na igreja? Para correr atrás do osso da fé.",
    "Qual é o lugar mais quente do mundo? O teclado, porque fica em cima da CPU."
]

# Escolhe uma piada aleatória
random_joke = random.choice(jokes)

# Imprime a piada escolhida
print(random_joke)