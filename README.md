# Balanceamento de Árvore Binária


### Contexto

Fatec-RioPreto/SP, 3° semestre do curso Análise e Desnvolvimento de Sistemas, estudando Listas Encadeadas e Árvores Binárias na disciplina Estrutura de Dados, do lendário Professor Dr. Carlos Magnus Carlson Filho.

Para a parte prática, o professor Carlos forneceu um código minimamente estruturado de _Listas Simplesmente Encadeadas_ em ```Python```, porém, estas classes estavam propositalmente incompletas. Após a explicação, o professor passava a complementação destas classes como atividade para nota. O estudante era desafiado a terminar as classes, implementando os métodos com as funcionalidades faltantes, tais como: inserir e remover elementos no início e no final da lista, percorrer os elementos da lista por diferentes percursos, estender o código fornecido a fim de obtermos uma _Lista Duplamente Encadeada_, entre outras.

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


<img width=70% alt="Árvore binária - Escolha do método de balanceamento" title="Árvore binária - Escolha do método de balanceamento" src="images/ab_abertura.png"><br>
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

<img width=70% alt="Escolha da ação a ser executada" title="Escolha da ação a ser executada" src="images/ab_menu2.png"><br>
<sup>_Figura 3: Escolha da ação a ser executada_</sup>

Vamos tratar agora de cada um dos métodos de balacenamento, começando pelo estático. E usaremos o balanceamento estático para mostrar o que faz as opções do segundo _menu_. Nos demais balanceamentos a ação é a mesma, então vamos destacar só alguns diferenciais.

---

## Balanceamento Estático

Único método que permite a inserção de vários valores antes de se fazer o balanceamento. Todos os demais métodos já realizam o balanceamento no momento da inserção. O que o método estático faz basicamente é remover todos os elementos da árvore para depois os reinserir em uma ordem ótima, na qual a árvore ficará balanceada. 

Para inserirmos um nó-folha - porque inicialmente este novo valor ficará em alguma extremidade, fazemos a comparação do valor do nó-folha com o nó corrente. Se o nó-folha for maior, desceremos pelo galho do lado direito, se for menor, desceremos o galho do lado esquerdo. Em uma árvore binária, cada nó pode ter apenas dois nós ligados, um de cada lado. Ao inserimos um novo valor, a árvore será percorrida recursivamente, fazendo a comparação referida, até encontrarmos uma posição vaga, à direita ou à esquerda, de um nó existente na árvore. 
<br>Vamos exemplificar que ficará mais claro.

Para desbalancear a árvore original vamos inserir três valores: 35, 37 e 5, nessa ordem, antes de fazermos o balancemanto. Começamos pelo nó raiz 44 e fazemos a comparação. 35 é maior ou menor que 44? É menor, então descemos pela esquerda até o nó 26. Novamente a comparação: 35 é maior ou menor que 26? É maior, então descemos pela direita até o nó 33. 35 é maior ou menor que 33? É maior, então descemos pela direita e como não há nenhum nó a direita do 33 o 35 encontrou o seu lugar. Ao inserirmos o 37 faremos o mesmo percurso do 35, mas dessa vez a vaga à direta do 33 agora está ocupada pelo 35, então o 37 desce pelo 35 e por ser maior que ele se posicionará a direita do 35. O valor 5 seguirá sempre pelo lado esquerdo, porque 5 é menor que 44, é menor que 26, é menor que 18 e menor que 12, ficando então pendurado no 12 pelo lado esquerdo. Rabiscando um esboço fica muito mais fácil de visualizar.

É aqui que a opção ```2 - Desenhar galhos```, nos ajuda a entender o atual estado da árvore após as três inserções (figura 4).

<img alt="Galhos após e inserções: 35, 37 e 5" title="Galhos após e inserções: 35, 37 e 5" src="images/galhos_apos_3insercoes.png"><br>
<sup>_Figura 4: Galhos após e inserções: 35, 37 e 5_</sup>

Na figura 4 temos uma parte da saída da opção 2. Nela podemos ver todos os nós inseridos, o 5 do lado esquerdo do 12, o 35 à direita do 33 e o 37 à direita do 35. A ordem das inserções faz total diferença. Se tivéssemos inserido o 37 antes do 35, teríamos o galho direito do nó 33 bem diferente, com o 37  à direita do 33 no lugar do 35, e o 35 à esquerda do 37, como visto na figura 5.

<img alt="Galho 33 com 37 inserido antes do 35" title="Galho 33 com 37 inserido antes do 35" src="images/galho33.png"><br>
<sup>_Figura 5: Galho 33 com 37 inserido antes do 35_</sup>

Reiniciamos a nossa árvore com a opção 7 e inserimos novamente os valores 35, 37 e 5, respectivamente, para retomarmos nosso exemplo.

Após a inserção de três elementos, agora é o momento oportuno de verificarmos o balanceamento da árvore com a opção 3. A análise do balancemanento é baseado na altura ou profundidade do nó. Na figura 6 temos o início da saída da opção 3, com altura zero para o nó raiz 44. 

<img width=70% alt="Início da análise do balanceamento da árvore, altura do nó raiz" title="Início da análise do balanceamento da árvore, altura do nó raiz" src="images/estatico_no44.png"><br>
<sup>_Figura 6: Início da análise do balanceamento da árvore: altura do nó raiz_</sup>

Avaliamos o balanceamento de um nó determinando seu fator de balanceamento,```fb```. O fator de balanceamento é a diferença de altura ou profundidade entre os ramos esquerdo e direito do nó. A altura ou profundidade de um ramo é a medida da quantidade de níveis ou camadas abaixo dele. Para que um nó esteja desbalanceado, o módulo do fator de balanceamento deve ser maior ou igual a 2, ```|fb| >= 2```. Se for positivo o ramo esquerdo é mais alto do que o direito, se negativo, o ramo direito é mais alto ou mais profundo do que o esquerdo.

Na figura 7 temos a análise gráfica dos nós 12 e 33. Vemos que o nó 12 está equilibrado, pois está com fator de balanceamento +1, isto é, a diferença entre a profundidade dos ramos esquerdo e direito é de apenas um, e o sinal "+" indica que o ramo maior está do lado esquerdo. Já o nó 33 está desbalanceado (critério: |fator de balanceamento| >= 2), tendo em vista que pelo lado esquerdo não há nenhum outro nó (profundidade zero), entretanto, pelo lado direito há dois níveis de nó (profundidade 2), o nó 35 e logo mais abaixo o 37, deixando seu fator de balanceamento igual a 2 negativo.

<img alt="Análise dos nós 12 e 33" title="Análise dos nós 12 e 33" src="images/estatico_no12_33.png"><br>
<sup>_Figura 7: Análise dos nós 12 e 33_</sup>

---

Fazer o balanceamento pelo método estático é muito dispendioso computacionalmente. Devemos recriar a árvore inteira, removendo todos os elementos ou criando uma totalmente nova, e depois fazer a inserção de todos os elementos na "ordem certa". Se fossemos empregar este método em produção, teriamos duas opções de política a adotar: ou recriar a árvore inteira a cada inserção a fim de que ela esteja sempre balanceada, ou tolerar temporariamente uma árvore desbalanceada e aplicar o balancemanento a um determinado intervalo de tempo, a cada 24h em um horário conveniente, por exemplo. Árvores desbalanceadas deixam a procura da informação mais lenta, pois faremos um maior número de comparações. Em suma, ou temos a inserção demorada e as buscas rápidas ou daremos prioridade às inserções e deixaremos as consultas mais lentas; há que se ponderar pela demanda.

Já mencionamos que a ordem com que se insere os valores afeta a estrutura da árvore. Portanto, precisamos ordenar as inserções de forma que a árvore obtida seja balanceada. Recomendamos consultar o código para saber como estabelecemos esta ordenação otimizada com medianas. 

Escolhendo a opção 4, teremos no terminal todas as etapas do balanceamento: 

1. A análise gráfica do balanceamento;
1. O diagnóstico do estado do balanceamento e em qual nó há um desequilíbrio, se houver;<br>
Havendo a necessidade do balanceamento, prosseguimos com:
1. A geração da lista ordenada de inserções otimizada;
1. A inserção dos elementos recriando a árvore;
1. E a reavaliação do balanceamento para validação do método.

A figura 8 traz as etapas de 2 a 5 do balanceamento estático.

<img width=70% alt="Efetuando o balanceamento estático" title="Efetuando o balanceamento estático" src="images/estatico_balance.png"><br>
<sup>_Figura 8: Efetuando o balanceamento estático_</sup>

Podemos checar a estrutura final da árvore binária, agora balanceada, mandando desenhar os galhos com a opção 2 do _menu_.


## Balanceamento Dinâmico-Estático

Este e os demais métodos a seguir são chamados dinâmicos, porque assim que um novo valor é inserido, é feita a avaliação do balanceamento da árvore, e constatando um desequilíbrio, o balanceamento já é efetuado. No  balanceamento dinâmico-estático o balanceamento é aplicado somente no nó desequilibrado e não em toda a árvore. Vamos inserir o valor 95 e entender melhor o método (figura 9).

<img width=70% alt="Adicionando valor 95 com balanceamento dinâmico-estático" title="Adicionando valor 95 com balanceamento dinâmico-estático" src="images/dim-est_95.png"><br>
<sup>_Figura 9: Adicionando valor 95 com balanceamento dinâmico-estático_</sup>

Após a inserção do elemento 95, avalia-se o balanceamento da árvore. Executa-se uma busca, a partir do nó raiz, se há algum nó cujo módulo 
do fator de balanceamento seja maior ou igual a 2 (fb >=|2|). A inserção do nó 95 faz com que já encontremos um desequilíbrio no nó raiz 44. Entretanto, a busca por nó desequilibrado deve continuar até encotrarmos o verdadeiro nó problematico, o nó 87.

<img alt="Nó 87 causando desquilíbrio colateral no nó 44" title="Nó 87 causando desquilíbrio colateral no nó 44" src="images/dim-est_44_87.png"><br>
<sup>_Figura 10: Nó 87 causando desquilíbrio colateral no nó 44_</sup>

Há ocasiões em que o primeiro nó encontrado com |fb| >= 2 ficou desbalanceado por efeito colateral de um desequilíbrio mais profundo. Portanto, deve-se continuar buscando até se encontrar o nó desequilibrado de maior profundidade. No caso da figura 10, o nó 44 ficou desequilibrado em decorrência do desequilíbrio do nó 87 e é apenas neste galho que deve-se efetuar o balanceamento, não no 44. 

O balanceamento é realizado criando-se um galho clone auxiliar, correspondente a sub-árvore(ramo) desbalanceada, no qual o nó desequilibrado será o nó raiz dessa sub-árvore. Aplica-se o balanceamento estático ao galho desbalanceado (galho clone). Na figura 11 vemos a sub-árvore sendo criada e o método estático econtrando apenas seis elementos em sua varredura nas propriedades da árvore.

<img alt="Balanceamento estático sendo aplicado apenas ao galho desequilibrado" title="Balanceamento estático sendo aplicado apenas ao galho desequilibrado" src="images/galho87.png"><br>
<sup>_Figura 11: Balanceamento estático sendo aplicado apenas ao galho desequilibrado_</sup>

Uma vez que o galho esteja balanceado, precisamos encontrar qual era o nó pai ao qual este galho estava ligado e por qual dos lados.

<img alt="Busca pelo nó pai do galho desequilibrado" title="Busca pelo nó pai do galho desequilibrado" src="images/dim-est_galho-pai.png"><br>
<sup>_Figura 12: Busca pelo nó pai do galho desequilibrado_</sup>

Remove-se o galho desbalanceado e reinsere os elementos do galho amputado, conectando um novo galho com o mesmos elementos, mas agora balanceado. Qualquer nó superior que estivesse desequilibrado, tornar-se-iria equilibrado por corolário do reequilíbrio do ramo mais profundo. Na figura 13 temos as etapas do transplante do galho. Podemos ver que antes do galho ser serrado, havia dezoito elementos e que após a amputação do galho restaram doze elementos. Após o reimplante a árvore voltou a ter 18 nós.

<img alt="Transplante de galho" title="Transplante de galho" src="images/serrote.png"><br>
<sup>_Figura 13: Transplante de galho_</sup>

Após o transplante de galho, realiza-se uma nova checagem no balanceamento. O resultado pode ser visto na figura 14.b. Interessante comparar com as propŕiedades da árvore antes do balanceamento, presente na figura 14.a com o resultado final, na figura 14.b. Observamos que o 95 que desequilibrou a árvore está presente nos percursos tanto da árvore desbalanceada quanto na balanceada, mas notamos que a posição no percurso não coincide, evidenciando a reestruturação ocorrida. Também vemos que a altura ou profundidade mudou, reduzindo a altura de 6 para 5. 

<img width=90% alt="Propriedades da árvore antes do balanceamento" title="Propriedades da árvore antes do balanceamento" src="images/din-est_antes.png"><br>
<sup>_Figura 14.a: Propriedades da árvore antes do balanceamento_</sup>
<img width=90% alt="Propriedades da árvore depois do balanceamento" title="Propriedades da árvore depois do balanceamento" src="images/din-est_depois.png"><br>
<sup>_Figura 14.b: Propriedades da árvore depois do balanceamento_</sup>

Reiteramos que a principal diferença desta abordagem em relação ao balanceamento estático é que, no puramente estático, remove-se todos os elementos, isto é, o balanceamento é aplicado à árvore toda, enquanto que na inserção dinâmica-estática remove-se apenas o ramo problemático, ou seja, aplica-se o balanceamento apenas a um galho, sem afetar o restante da árvore.




