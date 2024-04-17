# Jogo de Blackjack Simples

Este é um programa Python que implementa um jogo de Blackjack (ou 21) simples. O jogo inclui funções para criar um baralho, distribuir cartas para o jogador, calcular pontos de uma mão, determinar o resultado do jogo e permitir ao jogador pedir mais cartas.

## Funcionalidades Principais

### Criar um Baralho
A função `create_deck()` cria um baralho padrão de 52 cartas.

### Distribuir uma Mão
A função `create_hand(deck)` distribui uma mão de duas cartas para o jogador, removendo essas cartas do baralho.

### Calcular Pontos
A função `points(hand)` calcula os pontos de uma mão de acordo com as regras do Blackjack, onde as cartas numéricas valem seu valor, as cartas "K", "Q" e "J" valem 10 pontos cada, e o "A" pode valer 1 ou 11 pontos dependendo da situação.

### Determinar o Resultado
A função `result(hand)` determina o resultado do jogo com base nos pontos da mão do jogador. Se os pontos forem exatamente 21, o jogador ganha. Se os pontos excederem 21, o jogador perde.

### Pedir Mais Cartas (Hit)
A função `hit(deck, hand)` permite ao jogador pedir mais uma carta, adicionando-a à sua mão e removendo-a do baralho.

## Como Jogar
Para jogar o jogo, basta executar o código Python fornecido. O jogo irá distribuir uma mão inicial para o jogador e, em seguida, perguntar se deseja pedir mais cartas ou parar. O objetivo é obter o maior número de pontos possível sem exceder 21.

## Contribuição
Sinta-se à vontade para contribuir com melhorias neste projeto. Você pode abrir problemas para relatar bugs ou propor novos recursos. Pull requests também são bem-vindos.


