# Balanceamento de Árvore Binária


### Contexto

Fatec-RioPreto/SP, 3° semestre do curso Análise e Desnvolvimento de Sistemas, estudando Listas Encadeadas e Árvores Binárias na disciplina Estrutura de Dados, do lendário Professor Dr. Carlos Magnus Carlson Filho.

Para a parte prática, o professor Carlos forneceu um código minimamente estruturado de _Listas Simplesmente Encadeadas_ em ```Python```, porém, estas classes estavam propositalmente incompletas. Após a explicação, o professor passava a complementação destas classes como atividade para nota. O estudante era desafiado a terminar as classes, implementando os métodos faltantes de funcionalidades como: inserir e remover elementos, no início e no final da lista, percorrer os elementos da lista por diferentes percursos, estender o código fornecido a fim de obtermos uma _Lista Duplamente Encadeada_, entre outras.

Sedimentados os conceitos de listas encadeadas entramos em _Árvores Binárias_. Vimos dois métodos de balanceamento de árvore, o balanceamento estático e o método soviético AVL (_Adelson Velsky e Landis_). Para essa parte o professor não tinha códigos de demonstração. 
O que fizemos foi implementar em ```Python``` quatro métodos de balanceamento, os dois vistos nas aulas, o **```estático```**, o **```dinâmico russo AVL```** e mais 2 hidridos que criamos mesclando ideias dos dois anteriores, que os chamamos de **```dinâmico-estático```** e **```dinâmico-rotacional```**.

No material, o professor se utilizava sempre de uma mesma árvore binária, inseria um elemento que à desbalanceava e dai partia para explicar o algoritimo. Nosso código dá suporte à estas aulas, logo, carregamos esta árvore previamente no código e a partir dela sugerimos inserções que provocarão certos desbalanceamentos específicos. 

O grande diferencial didático é que, desde a árvore binária, todo o processo de balanceamento é desenhado passo a passo no terminal. O aluno pode acompanhar graficamente as alterações nos galhos da árvore. E depois de bem compreendido o comportamento do algoritmo de balanceamento escolhido, o estudante fica tentado a correr as linhas do código, reconhecendo as etapas do processo, aprendendo tanto os conceitos quanto a programação destes.

---
## Abertura

Na primeira tela da execução do programa mostramos a árvore binária que servirá de base para testes de todos os métodos de balanceamento. Em _Propriedades da Árvore_ imprimimos as três formas de percorrer a árvore, a quantidade de elementos, a altura ou profundidade da árvore, e por último damos o diagnóstico de que a nossa árvore de referência está balanceada.
A seguir é oferecido um menu numérico para o usuário escolher o método de balanceamento:
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

Vamos tratar agora de cada um dos métodos de balacenamento, começando pelo estático. E usaremos o balanceamento estático para mostrar o que faz as opções do segundo _menu_. Nos demais balanceamentos a ação é a mesma, então vamos destacar só alguns diferenciais.

---

## Balanceamento Estático

Único método que permite a inserção de vários valores antes de se fazer o balanceamento. Todos os demais métodos já realizam o balanceamento no momento da inserção. O que o método estático faz basicamente é remover todos os elementos da árvore para depois os reinserir em uma ordem ótima, na qual a árvore ficará balanceada. 

Para inserirmos um nó-folha, porque inicialmente este nó-valor ficará em alguma extremindade, fazemos a comparação do valor do nó-folha com o nó corrente. Se o nó-folha for maior, então descemos pelo lado direito, se for menor, descemos o galho pelo lado esquerdo. Numa árvore binária, cada nó pode ter apenas dois nós ligados, um de cada lado. Ao inserimos um novo valor, a árvore será percorrida recursivamente, fazendo a comparação até encontrarmos uma posição vaga, a direita ou a esquerda, de um nó existente na árvore. Vamos exemplificar que ficará mais claro.

Para desbalancear a árvore original vamos inserir três valores, 35, 37 e 5, nessa ordem, antes de fazermos o balancemanto. Começamos pelo nó raiz 44 e fazemos a comparação. 35 é maior ou menor que 44? É menor, então descemos pela esquerda até o nó 26. Novamente a comparação: 35 é maior ou menor que 26? É maior, então descemos pela direita até o nó 33. 35 é maior ou menor que 33? É maior, então descemos pela direita e como não há nenhum nó a direita do 33 o 35 encontrou o seu lugar. Ao inserirmos o 37 faremos o mesmo percurso do 35, mas dessa vez a vaga à direta do 33 agora está ocupada pelo 35, então o 37 desce pelo 35 e por ser maior que ele se posicionará a direita do 35. O valor 5 seguirá sempre pelo lado esquerdo, porque 5 é menor que 44, é menor que 26, é menor que 18 e menor que 12, ficando então pendurado no 12 pelo lado esquerdo. Rabiscando um esboço fica muito mais fácil.

É aqui que a opção 2, ```Desenhar galhos```, nos ajuda a entender o atual estado da árvore após as três inserções (figura 4).

<img alt="Galhos após e inserções: 35, 37 e 5" title="Galhos após e inserções: 35, 37 e 5" src="https://github.com/earmarques/balanceamento-arvore-binaria/blob/main/images/galhos_apos_3insercoes.png"><br>
<sup>_Figura 4: Galhos após e inserções: 35, 37 e 5_</sup>

Na figura 4 temos uma parte da saída da opção 2. Nela podemos ver todos os nós inseridos, o 5 do lado esquerdo do 12, o 35 à direita do 33 e o 37 à direita do 35. A ordem das inserções faz total diferença. Se tivéssemos inserido o 37 antes do 35, teríamos o galho do nó 33 bem diferente, com o 37  à direita do 33 no lugar do 35, e o 35 à esquerda do 37, como visto na figura 5.

<img alt="Galho 33 com 37 inserido antes do 35" title="Galho 33 com 37 inserido antes do 35" src="https://github.com/earmarques/balanceamento-arvore-binaria/blob/main/images/galho33.png"><br>
<sup>_Figura 5: Galho 33 com 37 inserido antes do 35_</sup>

Reiniciamos a nossa árvore com a opção 7 e inserimos novamente os valores 35, 37 e 5, respectivamente, para retomarmos nosso exemplo.

Após a inserção de três elementos, agora é o momento oportuno de verificarmos o balanceamento da árvore com a opção 3. A análise do balancemanento é baseado na altura ou profundidade do nó. Na figura 6 temos o início da saída da opção 3, com altura zero para o nó raiz 44. 

<img alt="Início da análise do balanceamento da árvore, altura do nó raiz" title="Início da análise do balanceamento da árvore, altura do nó raiz" src="https://github.com/earmarques/balanceamento-arvore-binaria/blob/main/images/estatico_no44.png"><br>
<sup>_Figura 6: Início da análise do balanceamento da árvore: altura do nó raiz_</sup>

A altura ou profundidade de um nó é a diferença entre a quantidade de níveis ou camadas entre os ramos esquerdo e direito. Se for positivo o ramo esquerdo é mais alto do que o direito, se negativo, o ramo direito é mais alto que o esquerdo. Para que um nó esteja desbalanceado, o módulo da altura deve ser maior ou igual a 2 (|altura do nó| >= 2).

Na figura 7 temos a análise dos nós 12 e 33. Vemos que o nó 12 está equilibrado, pois está com balanceamento +1, isto é, a diferença entre a profundidade dos ramos esquerdo e direito é de apenas um, e o sinal "+" indica que o ramo maior está do lado esquerdo. Já o nó 33 está desbalanceado (critério: |balanceamento| >= 2), porque pelo lado esquerdo não há nenhum outro nó, entretanto, pelo lado direito há dois níveis de nó, o nó 35 e logo mais abaixo o 37, deixando seu balanceamento igual a 2 negativo.

<img alt="Análise dos nós 12 e 33" title="Análise dos nós 12 e 33" src="https://github.com/earmarques/balanceamento-arvore-binaria/blob/main/images/estatico_no12_33.png"><br>
<sup>_Figura 7: Análise dos nós 12 e 33_</sup>






