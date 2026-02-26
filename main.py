def main():
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")
    frases = []

    while True:
        entrada = input("> ")
        if entrada.lower() == "sair":
            break
        frases.append(entrada)

    # Criando o arquivo original
    with open("meu_arquivo.txt", "w") as arquivo:
        for frase in frases:
            arquivo.write(frase + "\n")

    print("\nArquivo original criado. Agora vamos manipular os dados.")
    
    dados_modificados = []

    # Lendo o arquivo e modificando os dados
    with open("meu_arquivo.txt", "r") as arquivo:
        for linha in arquivo:
            # strip() remove o pula linha, upper() deixa em maiúsculo
            dados_modificados.append(linha.strip().upper())

    # Sobrescrevendo o arquivo com os dados em maiúsculas
    with open("meu_arquivo.txt", "w") as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + "\n")

    print("O arquivo foi sobrescrito com os dados modificados.")

if __name__ == "__main__":
    main()
