# Brainy

É uma linguagem de programação esotérica baseada no Brainf#ck/BF(mais uma para a lista das linguagens que não serve para porr4 nenhuma) cujo autor eu desconheço e só obtive informações dela a partir do Chat GPT. 

Neste código eu fiz meu interpretador em Python por pura falta do que fazer, portanto, serviu de aprendizado para criação de linguagens esotéricas. Seu uso é simples, apenas utiliza instruções como Brainfuck, mas com algumas novidades diferente do brainfuck tradicional.



# Funcionamentos
Segundo o Chat GPT(A Ia que de vez em quando tira algumas ideias do buraco), as instruções funcionam da seguinte forma:
```
>: move o ponteiro para a direita
<: move o ponteiro para a esquerda
+: incrementa o valor da célula em que o ponteiro está
-: decrementa o valor da célula em que o ponteiro está
.: imprime o valor da célula em que o ponteiro está como caractere ASCII correspondente
,: lê um caractere ASCII do usuário e armazena o valor na célula em que o ponteiro está
[: começa um loop enquanto o valor na célula atual for diferente de zero
]: termina um loop
@: imprime o valor na posição atual da fita de memória como um número decimal

#: comentário de linha única
```

# Exemplo

```
#Multiplicação

++
[
    >++<
    -
]>@ #2 * 2
>
++++
[
    >++++<
    -
]>@ # 4 * 4
```
E por enquanto é isso. Qualquer sugestão eu aceitarei!
Discord: JikanTribal#1067
