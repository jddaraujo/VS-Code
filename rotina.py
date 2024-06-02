def is_bissexto(ano):
    """
    Determina se um ano é bissexto.
    Um ano é bissexto se for múltiplo de 4, exceto os múltiplos de 100,
    que não são bissextos a menos que também sejam múltiplos de 400.
    """
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def valida_sigla_estado(sigla):
    """
    Valida uma sigla de estado brasileiro.
    Verifica se a sigla está na lista de siglas válidas.
    """
    estados_validos = [
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SP", "SE", "TO"
    ]
    return sigla.upper() in estados_validos

def main():
    # Verificação de ano bissexto
    ano = int(input("Digite o ano (AAAA): "))
    if is_bissexto(ano):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

    # Validação de sigla de estado
    sigla = input("Digite a sigla do estado (ex.: SP, RJ, MG): ")
    if valida_sigla_estado(sigla):
        print(f"A sigla '{sigla.upper()}' é válida.")
    else:
        print(f"A sigla '{sigla.upper()}' não é válida.")

# Execução da função principal
if __name__ == "__main__":
    main()