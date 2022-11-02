# Balanceamento de Árvore Binária


### Contexto

Fatec-RioPreto/SP, 3° semestre do curso Análise e Desnvolvimento de Sistemas, estudando Listas Encadeadas e Árvores Binárias na disciplina Estrutura de Dados, do lendário Professor Dr. Carlos Magnus Carlson Filho.

Para a parte prática, o professor Carlos forneceu um código minimamente estruturado de _Listas Simplesmente Encadeadas_ em ```Python```, porém, estas classes estavam propositalmente incompletas. Após a explicação, o professor passava a complementação destas classes como atividade para nota. O estudante era desafiado a terminar as classes, implementando os métodos faltantes de funcionalidades como: inserir e remover elementos no início e no final da lista, percorrer os elementos da lista por diferentes percursos, estender o código fornecido a fim de obtermos uma _Lista Duplamente Encadeada_, entre outras.

Sedimentados os conceitos de listas encadeadas entramos em _Árvores Binárias_. Vimos dois métodos de balanceamento de árvore, o balanceamento estático e o método soviético AVL (_Adelson Velsky e Landis_). Para essa parte o professor não tinha códigos de demonstração. 
O que fizemos foi implementar em ```Python``` quatro métodos de balanceamento, os dois vistos nas aulas, o **```estático```**, o **```dinâmico russo AVL```** e mais 2 hidridos que criamos mesclando ideias dos dois anteriores, que os chamamos de **```dinâmico-estático```** e **```dinâmico-rotacional```**.

No material, o professor se utilizava sempre de uma mesma árvore binária, inseria um elemento que a desbalanceava e dai partia para explicar o algoritimo. Nosso código dá suporte à estas aulas, logo, carregamos esta árvore previamente no código e a partir dela sugerimos inserções que provocarão certos desbalanceamentos específicos. 

O grande diferencial didático é que, desde a árvore binária, todo o processo de balanceamento é desenhado passo a passo no terminal, o aluno pode acompanhar graficamente as alterações nos galhos da árvore. E depois de bem compreendido o comportamento do algoritmo de balanceamento escolhido, o estudante fica tentado a correr as linhas do código, reconhecendo as etapas do processo, aprendendo tanto os conceitos quanto a programação destes.

---
## Abertura

Na primeira tela da execução do programa mostramos a árvore binária que servirá de base para testes de todos os métodos de balanceamento. Em _Propriedades da Árvore_ imprimimos as três formas de percorrer a árvore, a quantidade de elementos, a altura ou profundidade da árvore, e por último damos o diagnóstico de que a nossa árvore de referência está balanceada.
A seguir é oferecido um menu numérico para o usuário escolher o método de ordenação:
<br>```1 - Estático```
<br>```2 - Dinâmico-Estático```
<br>```3 - Dinâmico-Rotacional```
<br>```4 - Dinâmico Russo-AVL```
<br>```9 - Sair do programa```


<img width=60% alt="Árvore binária - Escolha do método de balanceamento" title="Árvore binária - Escolha do método de balanceamento" src="https://github.com/earmarques/balanceamento-arvore-binaria/blob/main/images/ab_abertura.png"><br>
<sup>_Figura 2: Árvore binária - Escolha do método de balanceamento_</sup>

Não importa o balanceamento escolhido, o segundo menu é sempre o mesmo da figura 3:
<br>```0 - Informações sobre o método``` |=> breve explicação do algoritmo
<br>```1 - Inserir valor``` |=> adiciona um nó folha à árvore
<br>```2 - Desenha galhos``` |=> percorre toda a árvore desenhando cada nó com seus nós vizinhos, à direita e à esquerda
<br>```3 - Checar balancenamento da árvore``` |=> avalia o balancenamento de cada nó, informando o nó desbalanceado se for o caso
<br>```4 - Balancear árvore binária ``` |=> executa o balanceamento e vai imprimindo todas as etapas do processo
<br>```7 - Reiniciar árvore binária original ``` |=> descarta a árvore que estiver sendo usada e recria a árvore base de testes
<br>```8 - Voltar à escolha do método de balanceamento ``` |=> retorna o primeiro menu
<br>```9 - Sair do programa```

<img width=60% alt="Escolha da ação a ser executada" title="Escolha da ação a ser executada" src="https://github.com/earmarques/balanceamento-arvore-binaria/blob/main/images/ab_menu2.png"><br>
<sup>_Figura 3: Escolha da ação a ser executada_</sup>


---
## 

