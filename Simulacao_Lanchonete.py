# Lanchonete
print('Bem vindo a Lanchonete do Lucas Gabriel de Moura Santos(RU:3927427)\n'
      'Cardápio\n'
      '| Código |       Descrição       | Valor(R$) |\n'
      '|   100  |    Cachorro-Quente    |    9,00   |\n'
      '|   101  | Cachorro-Quente Duplo |   11,00   |\n'
      '|   102  |        X-Egg          |   12,00   |\n'
      '|   103  |        X-Salada       |   13,00   |\n'
      '|   104  |        X-Bacon        |   14,00   |\n'
      '|   105  |        X-Tudo         |   17,00   |\n'
      '|   200  |    Refrigerante Lata  |    5,00   |\n'
      '|   201  |       Chá Gelado      |    4,00   |\n')

# variável vf foi atribuido um valor 0 para conseguir fazer a conta dentro do if/elif
vf = 0
# variável x atribuido um valor de 1 para usar mais na frente do codigo caso o cliente queira mais coisas ou não.
x = 1

# while True usado para criar um loop infinito até que o cliente deseje finalizar o pedido.
while True:
    # Try usado para controlar se a variável "codigo" vai receber algo númerico.
    try:
        # variável codigo usada para perguntar ao cliente o código do produto que deseja, com base no cardápio mostrado.
        codigo = int(input('Entre com o código desejado: '))
    # Except usado para caso seja digitado uma string na variável "codigo", avisa o erro e volta para "codigo".
    except(ValueError, TypeError):
        # mostra na tela que não foi digitado algo númerico.
        print('Caracteres não são válidos!\n'
              'Tente novamente.')
        # continue usado para voltar e pedir o código novamente.
        continue

    # se o codigo digitado for 100, será mostrado a escolha do Cachorro Quente e seu valor.
    if codigo == 100:
        # vf += usado para calcular a soma dos produtos escolhidos, caso a escolha for apenas essa não irá somar.
        vf += 9.00
        # mostra na tela o que foi escolhido.
        print('Você pediu um Cachorro Quente no valor de R$9,00')
    # se o codigo digitado for 101, será mostrado a escolha do Cachorro Quente Duplo e seu valor.
    elif codigo == 101:
        vf += 11.00
        # mostra na tela o que foi escolhido.
        print('Você pediu um Cachorro-Quente Duplo no valor de R$11,00')
    # se o codigo digitado for 102, será mostrado a escolha do X-Egg e seu valor.
    elif codigo == 102:
        vf += 12.00
        # mostra na tela o que foi escolhido.
        print('Você pediu um X-Egg no valor de R$12,00')
    # se o codigo digitado for 103, será mostrado a escolha do X-Salada e seu valor.
    elif codigo == 103:
        vf += 13.00
        # mostra na tela o que foi escolhido.
        print('Você pediu um X-Salada no valor de R$13,00')
    # se o codigo digitado for 104, será mostrado a escolha do X-Bacon e seu valor.
    elif codigo == 104:
        vf += 14.00
        # mostra na tela o que foi escolhido.
        print('Você pediu um X-Bacon no valor de R$14,00')
    # se o codigo digitado for 105, será mostrado a escolha do X-Tudo e seu valor.
    elif codigo == 105:
        vf += 17.00
        # mostra na tela o que foi escolhido.
        print('Você pediu um X-Tudo no valor de R$14,00')
    # se o codigo digitado for 200, será mostrado a escolha do Refrigerante Lata e seu valor.
    elif codigo == 200:
        vf += 5.00
        # mostra na tela o que foi escolhido.
        print('Você pediu um Refrigerante Lata no valor de R$5,00')
    # se o codigo digitado for 201, será mostrado a escolha do Chá Gelado e seu valor.
    elif codigo == 201:
        vf += 4.00
        # mostra na tela o que foi escolhido.
        print('Você pediu um Chá Gelado no valor de R$4,00')

    # se não for digitado nenhum dos código dos cardápio, avisa o usuário e pede para tentar novamente com um válido.
    else:
        # mostra na tela que o código não é válido.
        print('Codigo inválido!.\n'
              'Tente novamente com um código do cardápio.')
        # volta para a variável "codigo".
        continue

    # Pergunta ao usuário se deseja mais algum item ou se pode fechar a conta.
    x = int(input('Deseja pedir mais alguma coisa?\n'
                  '1 - Sim\n'
                  '0 - Não\n'))
    # condição se a variável "x" for diferente de 1, para encerrar a conta.
    # caso a opção escolhida seja 1, fará o loop novamente.
    if x != 1:
        # mostra na tela quanto ficou o valor final
        print('O total a ser pago é R${:.2f}'.format(vf))
        # break força o código a parar e encerra a conta.
        break
