# Calculadora de Partidas Rankeadas

Projeto desenvolvido como parte do desafio **Calculadora de Partidas Rankeadas** da DIO.

## Objetivo

Criar uma função que recebe a quantidade de vitórias e derrotas de um jogador, calcula o saldo de partidas rankeadas e determina seu nível de acordo com a quantidade de vitórias.

O saldo é calculado através da fórmula:

`saldo = vitórias - derrotas`

## Níveis

| Vitórias    | Nível    |
| ----------- | -------- |
| Até 10      | Ferro    |
| 11 a 20     | Bronze   |
| 21 a 50     | Prata    |
| 51 a 80     | Ouro     |
| 81 a 90     | Diamante |
| 91 a 100    | Lendário |
| 101 ou mais | Imortal  |

## Conceitos utilizados

* Variáveis
* Operadores
* Estruturas de decisão (`if`, `elif` e `else`)
* Laço de repetição (`while`)
* Funções
* Entrada de dados com `input()`
* Saída de dados com `print()`
* F-strings

## Funcionamento

O programa solicita ao usuário a quantidade de vitórias e derrotas, calcula o saldo e identifica o nível do jogador.

Após apresentar o resultado, o usuário pode escolher se deseja realizar um novo cálculo.

### Exemplo

```text
Digite a quantidade de vitórias: 101
Digite a quantidade de derrotas: 30

O Herói tem de saldo de 71 está no nível de Imortal

Deseja continuar? (s/n): n
```

## Tecnologia

* Python

## Desafio

Projeto desenvolvido para praticar conceitos fundamentais de lógica de programação durante a formação da DIO.
