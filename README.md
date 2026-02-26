📝 Manipulador de Frases em Python
Este projeto foi desenvolvido como parte dos meus estudos iniciais em Análise e Desenvolvimento de Sistemas na Estácio. O objetivo é demonstrar a aplicação de lógica de programação para manipulação de arquivos de texto (.txt) utilizando Python.

🚀 Funcionalidades
O script executa um fluxo completo de tratamento de dados:


Entrada Dinâmica: Coleta frases digitadas pelo usuário via console.


Persistência de Dados: Cria e escreve as informações em um arquivo externo.


Processamento de Strings: Lê o arquivo gerado e aplica transformações (remoção de espaços e conversão para maiúsculas).


Atualização de Arquivo: Sobrescreve o arquivo original com os dados já tratados.

🛠️ Tecnologias Utilizadas

Python 3.


Manipulação de IO (Input/Output): Uso de contextos com with open para segurança de dados.

📖 Como Rodar o Projeto
Certifique-se de ter o Python instalado.

Clone este repositório.

Execute o arquivo python.sql (ou renomeie para .py para execução padrão).

Digite suas frases e finalize com a palavra-chave "sair".

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
