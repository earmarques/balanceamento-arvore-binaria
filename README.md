# Balanceamento de Árvore Binária


### Contexto

Fatec-RioPreto/SP, 3° semestre do curso Análise e Desnvolvimento de Sistemas, estudando Listas Encadeadas e Árvores Binárias na disciplina Estrutura de Dados, do lendário Professor Dr. Carlos Magnus Carlson Filho.

Para a parte prática, o professor Carlos forneceu um código minimamente estruturado de _Listas Simplesmente Encadeadas_ em ```Python```, porém, estas classes estavam propositalmente incompletas. Após a explicação, o professor passava a complementação destas classes como atividade para nota. O estudante era desafiado a terminar as classes, implementando os métodos faltantes de funcionalidades como: inserir e remover elementos no início e no final da lista, percorrer os elementos da lista por diferentes percursos, estender o código fornecido a fim de obtermos uma _Lista Duplamente Encadeada_, entre outras.

Sedimentados os conceitos de listas encadeadas entramos em _Árvores Binárias_. Vimos dois métodos de balanceamento de árvore, o balanceamento estático e o método soviético AVL (_Adelson Velsky e Landis_). Para essa parte o professor não tinha códigos de demonstração. 
O que fizemos foi implementar em ```Python``` quatro métodos de balanceamento, os dois vistos nas aulas, o **```estático```**, o **```dinâmico russo AVL```** e mais 2 hidridos que criamos mesclando ideias dos dois anteriores, que os chamamos de **```dinâmico-estático```** e **```dinâmico-rotacional```**.

No material, o professor se utilizava sempre de uma mesma árvore binária, inseria um elemento que a desbalanceava e dai partia para explicar o algoritimo. Nosso código dá suporte à estas aulas, logo, carregamos esta árvore previamente no código e a partir dela sugerimos inserções que provocarão certos desbalanceamentos específicos. 

O grande diferencial didático é que, desde a árvore binária, todo o processo de balanceamento é desenhado passo a passo no terminal, o aluno pode acompanhar graficamente as alterações nos galhos da árvore. E depois de bem compreendido o comportamento do algoritmo de balanceamento escolhido, o estudante fica tentado a correr as linhas do código, reconhecendo as etapas do processo, aprendendo tanto os conceitos quanto a programação destes.


