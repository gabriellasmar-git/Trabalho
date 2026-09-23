# SISTEMA DE ATENDIMENTO E PEDIDOS
# TRABALHO PRÁTICO - ALGORITMOS E PROGRAMAÇÃO


def mostrar_cardapio():
    print("\n===== CARDÁPIO =====")
    print("1 - X-Burguer ........ R$ 18,00")
    print("2 - X-Tudo ........... R$ 30,00")
    print("3 - Batata Frita ..... R$ 12,00")
    print("4 - Refrigerante ..... R$ 7,00")
    print("5 - Suco Natural ..... R$ 10,00")
    print("0 - Finalizar pedido")
    print("==============================")


def calcular_desconto(total):
    if total < 50:
        percentual = 0

    elif total < 100:
        percentual = 5

    else:
        percentual = 10

    valor_desconto = total * percentual / 100
    valor_final = total - valor_desconto

    return percentual, valor_desconto, valor_final


def escolher_pagamento():
    pagamento_valido = False
    forma_pagamento = ""

    while pagamento_valido == False:
        print("\n===== FORMA DE PAGAMENTO =====")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão")

        opcao_pagamento = input("Escolha uma opção: ")

        if opcao_pagamento == "1":
            forma_pagamento = "Dinheiro"
            pagamento_valido = True

        elif opcao_pagamento == "2":
            forma_pagamento = "PIX"
            pagamento_valido = True

        elif opcao_pagamento == "3":
            forma_pagamento = "Cartão"
            pagamento_valido = True

        else:
            print("Opção de pagamento inválida!")

    return forma_pagamento


def mostrar_resumo(nome, total, percentual, desconto, valor_final, pagamento):
    print("\n========== RESUMO DO PEDIDO ==========")
    print("Cliente:", nome)
    print(f"Valor original: R$ {total:.2f}")
    print(f"Desconto aplicado: {percentual}%")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
    print("Forma de pagamento:", pagamento)
    print("======================================")
    print("Obrigado pela preferência!")


def realizar_pedido():
    print("=========================================================")
    print("                 SISTEMA DE PEDIDO")
    print("=========================================================")

    nome = input("Digite o nome do cliente: ")

    total = 0
    continuar = True

    while continuar:
        mostrar_cardapio()

        codigo = input("Digite o código do pedido: ")

        if codigo == "0":
            continuar = False

        elif codigo == "1":
            preco = 18.00
            produto = "X-Burguer"

            quantidade = int(input("Digite a quantidade: "))

            if quantidade > 0:
                subtotal = preco * quantidade
                total = total + subtotal

                print("\nProduto:", produto)
                print("Quantidade:", quantidade)
                print(f"Subtotal: R$ {subtotal:.2f}")

            else:
                print("Quantidade inválida!")

        elif codigo == "2":
            preco = 30.00
            produto = "X-Tudo"

            quantidade = int(input("Digite a quantidade: "))

            if quantidade > 0:
                subtotal = preco * quantidade
                total = total + subtotal

                print("\nProduto:", produto)
                print("Quantidade:", quantidade)
                print(f"Subtotal: R$ {subtotal:.2f}")

            else:
                print("Quantidade inválida!")

        elif codigo == "3":
            preco = 12.00
            produto = "Batata Frita"

            quantidade = int(input("Digite a quantidade: "))

            if quantidade > 0:
                subtotal = preco * quantidade
                total = total + subtotal

                print("\nProduto:", produto)
                print("Quantidade:", quantidade)
                print(f"Subtotal: R$ {subtotal:.2f}")

            else:
                print("Quantidade inválida!")

        elif codigo == "4":
            preco = 7.00
            produto = "Refrigerante"

            quantidade = int(input("Digite a quantidade: "))

            if quantidade > 0:
                subtotal = preco * quantidade
                total = total + subtotal

                print("\nProduto:", produto)
                print("Quantidade:", quantidade)
                print(f"Subtotal: R$ {subtotal:.2f}")

            else:
                print("Quantidade inválida!")

        elif codigo == "5":
            preco = 10.00
            produto = "Suco Natural"

            quantidade = int(input("Digite a quantidade: "))

            if quantidade > 0:
                subtotal = preco * quantidade
                total = total + subtotal

                print("\nProduto:", produto)
                print("Quantidade:", quantidade)
                print(f"Subtotal: R$ {subtotal:.2f}")

            else:
                print("Quantidade inválida!")

        else:
            print("\nCódigo inválido! Escolha uma opção do cardápio.")


    percentual, desconto, valor_final = calcular_desconto(total)

    pagamento = escolher_pagamento()

    mostrar_resumo(
        nome,
        total,
        percentual,
        desconto,
        valor_final,
        pagamento
    )


realizar_pedido()
       

       

