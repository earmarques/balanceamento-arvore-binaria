
#coding=utf-8

 ###################################################
#                                                  #
# Author: Éder A. R. Marques                       #
# Email:  earmarques@gmail.com                     #
# Local:  São José do Rio Preto/SP Brazil          #
# Core:     10/12/2020                             #
# UI Added: 10/19/2021                             #
# Versioned for Python 3                           #
# ------------------------------------------------ #
# Professor: Carlos Magnus Carlson Filho           #
# Course:    Estruturas de Dados                   #
# Program:   Análise e Desenvolvimento de Sistemas #
# College:   Fatec Rio Preto                       #
#                                                  #
###################################################


# ==================================================================================================
# Árvore Binária - Classe Principal     ============================================================
# ==================================================================================================

class ArvoreBinaria:

  # ================================================================================================
  # Classe Interna Privada Noh_ArvoreBinaria     ===================================================

  class __Noh_ArvoreBinaria:

    # Construtor     -------------------------------------------------------------------------------
    def __init__(self, valor):
      self.__subarvore_esquerda = None
      self.__conteudo           = valor
      self.__inativo            = False
      self.__subarvore_direita  = None


    # Getter's/Setter's     ------------------------------------------------------------------------

    # conteudo
    def get_conteudo(self):
      return self.__conteudo

    def set_conteudo(self, valor):
      self.__conteudo = valor


    # inativo
    def is_inativo(self):
      return self.__inativo

    def set_inativo(self, valor_booleano):
      self.__inativo = valor_booleano


    # subarvore_esquerda
    def get_subarvore_esquerda(self):
      return self.__subarvore_esquerda

    def set_subarvore_esquerda(self, referencia):
      self.__subarvore_esquerda = referencia


    # subarvore_direita
    def get_subarvore_direita(self):
      return self.__subarvore_direita

    def set_subarvore_direita(self, referencia):
      self.__subarvore_direita = referencia


    # 'printer default' da classe - equivale ao toString() do Java
    def __str__(self):
      return str(self.__conteudo)

  # ================================================================================================


  # Construtor da Classe ArvoreBinaria     ---------------------------------------------------------

  def __init__(self):
    self.__raiz    = None
    self.__quantidade_noh = 0


  # Getter's/Setter's     --------------------------------------------------------------------------

  # raiz
  def get_raiz(self):
    return self.__raiz

  def set_raiz(self, referencia):
    self.__raiz = referencia

  # quantidade_noh
  def get_quantidade_noh(self):
    return self.__quantidade_noh

  def set_quantidade_noh(self, valor):
    self.__quantidade_noh = valor


  # Arvore Vazia     -------------------------------------------------------------------------------

  def arvore_vazia(self):
    return self.__raiz == None


  # Limpar a Árvore - Desfolhar     ----------------------------------------------------------------

  def clear(self):
    self.set_raiz(None)


  # Método de Busca     ----------------------------------------------------------------------------

  # Wrapper
  def busca_noh(self, valor, debug=True):

    return self.__busca_noh_recursivo(self.__raiz, valor, debug)

  # Busca Recursiva
  def __busca_noh_recursivo(self, noh_atual, valor, debug=True):

    if self.arvore_vazia():
      if debug: print('Árvore vazia. O elemento \"{}\" não está na árvore.'.format(valor))
      return None

    if valor is noh_atual.get_conteudo():
      if debug: print( '{}\nEncontrado !!!'.format(noh_atual) )
      return noh_atual


    if valor < noh_atual.get_conteudo():
      galho = noh_atual.get_subarvore_esquerda()
      if not ( galho == None ):
        if debug: print('E > ', end='')     # indo para esquerda
        return self.__busca_noh_recursivo(galho, valor, debug)    # RECURSÃO !!!

      else:
        if debug: print('\nO elemento \"{}\" não está na árvore.'.format(valor) )
        return None

    else:   # valor > noh_atual
      galho = noh_atual.get_subarvore_direita()
      if not ( galho == None ):
        if debug: print('D > ', end='')     # indo para direita
        return self.__busca_noh_recursivo(galho, valor, debug)    # RECURSÃO !!!

      else:
        if debug: print('\nO elemento \"{}\" não está na árvore.'.format(valor) )
        return None


  # Método de Exclusão (status inativo)     --------------------------------------------------------

  # Wrapper
  def excluir_noh(self, valor, debug=True):

    return self.__excluir_noh_recursivo(self.__raiz, valor, debug)

  # Busca Recursiva - Apagar(inativar) quando encontrar
  def __excluir_noh_recursivo(self, noh_atual, valor, debug=True):

    if self.arvore_vazia():
      if debug: print('Árvore vazia. Não é possível excluir nenhum elemento.')
      return None

    if valor is noh_atual.get_conteudo():
      noh_atual.set_inativo(True)
      if debug: print( '{} foi excluído com sucesso !'.format(noh_atual) )
      return noh_atual


    if valor < noh_atual.get_conteudo():
      galho = noh_atual.get_subarvore_esquerda()
      if galho:   # != None
        if debug: print('E > ', end='')     # indo para esquerda
        return self.__excluir_noh_recursivo(galho, valor)    # RECURSÃO !!!

      else:
        msg = '\nNão é possível excluir o elemento \"{}\", '
        msg += 'pois ele não está na árvore.'
        if debug: print(msg.format(valor))
        return None

    else:   # valor > noh_atual
      galho = noh_atual.get_subarvore_direita()
      if galho:
        if debug: print('D > ', end='')     # indo para direita
        return self.__excluir_noh_recursivo(galho, valor)    # RECURSÃO AQUI !

      else:
        msg = '\nNão é possível excluir o elemento \"{}\", '
        msg += 'pois ele não está na árvore.'
        if debug: print(msg.format(valor))
        return None



  # ================================================================================================
  # Percursos   ------------------------------------------------------------------------------------

  # Percurso Simétrico |=> E -> R -> D     ---------------------------------------------------------

  def percurso_simetrico(self):
    self.__percurso_simetrico_recursivo(self.get_raiz())


  def percurso_simetrico_outra_arvore(self, outra_arvore):
    self.__percurso_simetrico_recursivo(outra_arvore.get_raiz())


  def __percurso_simetrico_recursivo(self, noh_atual):

    # fim da galhada
    if noh_atual == None:
      return


    # percorrer galhada recursivamente

    self.__percurso_simetrico_recursivo(noh_atual.get_subarvore_esquerda())   # E ->

    if not noh_atual.is_inativo():                                            # R ->
       print(noh_atual, end=' ')

    self.__percurso_simetrico_recursivo(noh_atual.get_subarvore_direita())    # D


  # Percurso Pré-Ordem |=> R -> E -> D     ---------------------------------------------------------

  def percurso_pre_ordem(self):
    self.__percurso_pre_ordem_recursivo(self.get_raiz())

  def __percurso_pre_ordem_recursivo(self, noh_atual):

    # cheguei na pontinha da folha
    if noh_atual == None:
      return


    #continuar descendo recursivamente

    if not noh_atual.is_inativo():
       print(noh_atual, end=' ')                                             # R ->

    self.__percurso_pre_ordem_recursivo(noh_atual.get_subarvore_esquerda())  # E ->

    self.__percurso_pre_ordem_recursivo(noh_atual.get_subarvore_direita())   # D


  # Percurso Pré-Ordem |=> E -> D -> R     ---------------------------------------------------------

  def percurso_pos_ordem(self):
    self.__percurso_pos_ordem_recursivo(self.get_raiz())

  def __percurso_pos_ordem_recursivo(self, noh_atual, debug=False):

    # se chegou a um final de ramo
    if noh_atual == None:
      return


    # segue percorrendo recursivamente

    self.__percurso_pos_ordem_recursivo(noh_atual.get_subarvore_esquerda()) # E ->

    self.__percurso_pos_ordem_recursivo(noh_atual.get_subarvore_direita())  # D ->

    if not noh_atual.is_inativo():                                          # R
       print(noh_atual, end=' ')


  # ------------------------------------------------------------------------------------------------
  # Balanceamento Estático     ---------------------------------------------------------------------

  def balanceamento_estatico(self, debug=False):

    self.__balanceamento_estatico(self, debug)

  def __balanceamento_estatico(self, arvore, debug=False):

    if arvore is None:
      if debug: print('#__balanceamento_estatico: parâmetro \"arvore\" está None')
      return None


    if debug:
      print('\n{: ^80}'.format('  ***  __BALANCEAMENTO ESTÁTICO__  ***  '))
      self.imprimir_propriedades()

    if debug:
      print(self.__cabecalho('Análise do Balanceamento', ' '))

    noh_desbalanceado = arvore.get_noh_mais_profundo_desbalanceado(debug)

    if debug:
      if noh_desbalanceado:
        print('\nRESULTADO >> Árvore desbalanceada no noh {}'.format(noh_desbalanceado))
      else:
        print('\nRESULTADO >> A árvore está balanceada.')

    # Árvore Balanceada - nada a fazer
    if not noh_desbalanceado:
      return None


    # Lista Otimizada para Inserção Balanceada
    lista_insercao = arvore.get_pilha_insercao_balanceada()
    if debug:
      print(self.__cabecalho('Lista Otimizada para Inserção Balanceada', ' '))
      print(lista_insercao)

    # Cortando a Árvore Pela Raiz
    if debug:
      print(self.__cabecalho('Cortando a Árvore Pela Raiz',' '))
      print('Árvore com galhos e folhas:', end=' ')
      arvore.percurso_simetrico()

    if debug:
      print('\nÁrvore arrancada pela raiz.')
      print('Árvore com galhos e folhas:', end=' ')
    arvore.clear()
    arvore.percurso_simetrico()
    if debug: print('-?-  (^o^)  \n')

    # Replantando a Árvore - Utilizando lista otimizada de inserção
    if debug:
      print(self.__cabecalho('Replantando a árvore com a lista otimizada para inserção',' '))
      print('Semeando...')

    for i, ramo in enumerate(lista_insercao):
      arvore.insere_noh(ramo)
      if debug:
        print('..{}'.format(ramo), end='\n' if (i+1) % 10 == 0 else '')


    # A árvore já está balanceada.
    # Se estiver em modo debug, então vamos fazer a conferência
    #  do balanceamento e apresentar o resultado.
    # Senão, este processamento é desnecessário.
    #
    if debug:
      print('\n\n')
      print('{: ^80}'.format('  ***  __RESULTADO BALANCEAMENTO ESTÁTICO__  ***  '))
      self.imprimir_propriedades()
      print(self.__cabecalho('Análise Descendente do Balanceamento', ' '))
      noh_desbalanceado = arvore.get_noh_mais_profundo_desbalanceado()
      if noh_desbalanceado:
        print('\nRESULTADO >> Árvore desbalanceada no noh {}'.format(noh_desbalanceado))
      else:
        print('\nRESULTADO >> A árvore está balanceada.')


  # ================================================================================================
  # Inserções de Noh's     -------------------------------------------------------------------------

  # Inserção Comum - Sem Balanceamento     ---------------------------------------------------------

  def insere_noh(self, valor, debug=False):

    self.__insere_noh_recursivo(self.__raiz, valor, debug)


  def __insere_noh_recursivo(self, noh_atual, valor, debug=False):

    if self.arvore_vazia():
      noh_folha = self.__Noh_ArvoreBinaria(valor)
      self.set_raiz(noh_folha)
      self.set_quantidade_noh( 1 )
      return noh_folha


    # Descer pelo galho da esquerda
    if valor < noh_atual.get_conteudo():
      galho = noh_atual.get_subarvore_esquerda()
      # se tiver galho, continuar descendo
      if not ( galho == None ):
        self.__insere_noh_recursivo(galho, valor, debug)    # RECURSÃO !!!
      else:
        # estou na extremidade, adicionar noh_folha
        noh_folha = self.__Noh_ArvoreBinaria(valor)
        noh_atual.set_subarvore_esquerda(noh_folha)
        self.set_quantidade_noh( self.get_quantidade_noh() + 1 )
        if debug:
          caixa = self.__encaixotar(noh_folha, posicao=4)
          print('\nNoh inserido..\n{}\n----------'.format(caixa))
        return noh_folha

    else:
      # Descer pelo galho da direita
      galho = noh_atual.get_subarvore_direita()
      if not ( galho == None ):
        self.__insere_noh_recursivo(galho, valor, debug)    # RECURSÃO !!!
      else:
        # já estou na ponta, adicionar noh-folha
        noh_folha = self.__Noh_ArvoreBinaria(valor)
        noh_atual.set_subarvore_direita(noh_folha)
        self.set_quantidade_noh( self.get_quantidade_noh() + 1 )
        if debug:
          caixa = self.__encaixotar(noh_folha, posicao=4)
          print('\nNoh inserido..\n{}\n----------'.format(caixa))
        return noh_folha


  # Inserção Com Balanceamento Dinâmico-Estático     -----------------------------------------------

  def insere_noh_dinamico_estatico(self, valor, debug=False):

    """ Inserção Com Balanceamento Dinâmico-Estático

    Ao contrário do balanceamento dinâmico que remove todos os elementos da árvore
    e os reinsere numa ordem tal que a árvore fica balanceada, nesta inserção
    o balenceamento é aplicado apenas no galho desbalanceado.

    O algorítimo deste método de inserção é o seguinte. Faz-se a inserção do elemento
    normalmente e depois confere-se o balanceamento. Havendo necessidade de balancear,
    identifica-se em qual galho, no nível mais profundo da árvore, há o desbalanceamento.
    Remove-se o galho desequilibrado e cria-se um novo galho, com os mesmos elementos,
    porém, agora balanceado. Por fim, insere-se o novo galho no lugar do antigo.

    Args:
      valor (int): Valor a ser inserido na árvore.
      debug (bool, optional): Chaveamento para imprimir todos os passos intermediários.
      Defaults to False.

    Returns:
        None: Nada a retorna.

    """

    self.__insere_noh_dinamico_estatico_recursivo(self.__raiz, valor, debug)


  def __insere_noh_dinamico_estatico_recursivo(self, noh_atual, valor, debug=False):

    #  Etapas:
    # .1  Faz-se a inserção comum.
    # .2  Avalia-se o balanceamento da árvore buscando o noh de maior
    #      profundidade, cujo módulo do fator de balanceamento seja maior ou igual a 2 (fb >=|2|).
    # .2a Se nenhum noh desbalanceado for encontrado, a árvore está balanceada.
    # .2b Se a árvore estiver desbalanceada, procede-se o balanceamento:
    # __ BALANCEAMENTO  ---------------
    # .3  Cria-se um galho clone auxiliar com os elementos da sub-arvore
    #      na qual o noh desequilibrado será o noh-raiz.
    # .4  Aplica-se o balanceamento estático ao galho desbalanceado (galho clone).
    # .5  Remove-se o galho desbalanceado.
    # .6  Reinsere os elementos do galho amputado conectando o novo galho balanceado.
    #

    if self.arvore_vazia():

      if debug: print('#.__insere_noh_dinamico_estatico: A árvore está vazia.')

      noh_folha = self.__insere_noh_recursivo(self.__raiz, valor, debug)

      if debug:
        caixa = self.__encaixotar(noh_folha, posicao=4)
        print('\nNoh inserido..\n{}\n----------'.format(caixa))

      return noh_folha


    # Iniciando Etapas
    if debug:
      print('\n{: ^80}'.format('  ***  __INSERÇÃO COM BALANCEAMENTO DINÂMICO-ESTÁTICO__  ***  '))


    # .1 Inserção Comum

    noh_folha = self.__insere_noh_recursivo(self.__raiz, valor, debug)

    if debug:
      self.imprimir_propriedades()

    # .2 Análise do Balanceamento

    if debug:
      print(self.__cabecalho('Análise Descendente do Balanceamento', ' '))

    noh_desbalanceado = self.get_noh_mais_profundo_desbalanceado(debug)

    if debug:
      if noh_desbalanceado:
        print('\nRESULTADO >> Árvore desbalanceada no noh {}'.format(noh_desbalanceado))
      else:
        print('\nRESULTADO >> A árvore está balanceada.')

    # .2a Árvore Balanceada - nada a fazer
    if not noh_desbalanceado:
      return noh_folha


    # Realizando o Balanceamento     ...........................................

    # .3 Galho Clone Auxiliar

    if debug:
      print(self.__cabecalho('Realizando o Balanceamento','.'))
      print(self.__cabecalho('Criando Sub-Árvore Auxiliar do Noh_Desbalanceado',' '))

    galho  = self.criar_arvore(noh_desbalanceado)

    if debug:
      print('Percurso:', end=' ')
      galho.percurso_simetrico()
      print( '\nTotal de elementos: {}\n'.format(galho.get_quantidade_noh()) )


    # .4 Fazendo o Balanceamento do Galho

    if debug:
      print(self.__cabecalho('Fazendo o Balanceamento do Galho', ' '))
      #galho.desenhar_todos_galhos()

    galho.balanceamento_estatico(debug)


    # .5 Remoção do Galho Desbalanceado

    # Encontrando o Noh_Pai
    #
    # O noh_pai é necessário porque o noh_filho desbalanceado será cortado.
    # E precisamos saber de que lado está, para cortar o galho certo.
    #
    if debug:
      print('{:_<55}'.format(''))
      print(' OK >> Galho-Clone pronto para ser enxertado na árvore.\n')

      print(self.__cabecalho('Remoção do Galho Desbalanceado',' '))
      print('Encontrando o Noh_Pai do Noh_Desequilibrado',' ')

    pai = self.get_noh_pai(noh_desbalanceado, debug)

    if debug: print('Pai do filho rebelde:', pai)

    if pai:
      if debug: print('\nDescobrindo por qual mão o pai segura seu filho',' ')
      mao_esquerda = pai.get_subarvore_esquerda()
      mao_direita  = pai.get_subarvore_direita()

      if noh_desbalanceado == mao_esquerda:
        if debug: print('>> mão esquerda')
        mao_direita = None
      else:
        if debug: print('>> mão direita')
        mao_esquerda = None

    # else o noh desbalanceado é o noh_raiz(pai=None)


    # Removendo Noh Filho

    if debug:
      print('\nRemovendo o noh-filho desbalanceado do noh-pai.....\n__________________________')
      print(' Árvore antes da remoção:')
      print('Percurso:', end='')
      self.percurso_simetrico()
      print( '\nTotal de elementos: {}\n'.format(self.get_quantidade_noh()) )
      print('...passando o serrote...')
      print('\n   [D:/¨¨¨¨¨¨¨¨¨¨\\\n      ^^^^^^^^^^^^')

    if pai:
      if mao_esquerda:
        pai.set_subarvore_esquerda(None)
      else:
        pai.set_subarvore_direita(None)
    else:
      self.set_raiz(None)
      if debug: print('Árvore inteira extirpada !!! O noh desbalanceado era o próprio noh raiz.')


    # Atualização da Contagem de Elementos

    if debug: print('\nAtualizando quantidade de elementos na árvore...')

    self.set_quantidade_noh( self.get_quantidade_noh() - galho.get_quantidade_noh() )

    if debug:
      print('\n Árvore após remoção do galho com cupins:')
      print('Percurso:', end='')
      self.percurso_simetrico()
      print( '\nTotal de elementos: {}'.format(self.get_quantidade_noh()) )
      print('_________________\nGalho removido !\n')
      print(self.__cabecalho('Reinserção do Novo Galho Balanceado',' '))


    # .6 Reinsere os elementos através do galho balanceado

    if pai:
      if mao_esquerda:
        pai.set_subarvore_esquerda(galho.get_raiz())
      else:
        pai.set_subarvore_direita(galho.get_raiz())
    else:
      self.set_raiz(galho.get_raiz())


    # Atualização da Contagem de Elementos

    if debug: print('\nAtualizando quantidade de elementos na árvore...')

    self.set_quantidade_noh(self.conta_noh())

    if debug:
      print('>> Árvore com os noh\'s reinseridos.')
      self.percurso_simetrico()
      print( '\nTotal de elementos: {}\n'.format(self.get_quantidade_noh()) )


    # Conferindo o Balanceamento

    if debug:
      print(self.__cabecalho('Conferindo o Balanceamento','.'))
      noh_desbalanceado = self.get_noh_mais_profundo_desbalanceado(debug)
      self.imprimir_propriedades()
      if noh_desbalanceado:
        print('\nRESULTADO >> Árvore desbalanceada no noh {}'.format(noh_desbalanceado))
      else:
        print('\nRESULTADO >> A árvore está balanceada.')



    return self.busca_noh(valor, debug=False)


  # Inserção Com Balanceamento Dinâmico-Rotacional     ---------------------------------------------

  def insere_noh_dinamico_rotacional(self, valor, debug=False):

    self.__insere_noh_dinamico_rotacional_recursivo(self.__raiz, valor, debug)


  def __insere_noh_dinamico_rotacional_recursivo(self, noh_atual, valor, debug=False):

    #  Etapas:
    # .1  Faz-se a inserção comum.
    # .2  Avalia-se o balanceamento da árvore buscando o noh de maior
    #      profundidade, cujo módulo do fator de balanceamento seja maior ou igual a 2 (fb >=|2|).
    # .2a Se nenhum noh desbalanceado for encontrado, a árvore está balanceada.
    # .2b Se a árvore estiver desbalanceada, procede-se o Balanceamento
    # __ BALANCEAMENTO  ---------------
    # .3  Encontra o noh_pai do noh desequilibrado
    # .4  Rotaciona para balancear - o método #rotacionar identifica o tipo de rotação
    #      e aplica a rotação adequada.
    #
    if self.arvore_vazia():

      if debug: print('#.__insere_noh_dinamico_rotacional: A árvore está vazia.')

      noh_folha = self.__insere_noh_recursivo(self.__raiz, valor, debug)

      if debug:
        caixa = self.__encaixotar(noh_folha, posicao=4)
        print('\nNoh inserido..\n{}\n----------'.format(caixa))

      return noh_folha


    # Iniciando Etapas
    if debug:
      print('\n{: ^80}'.format('  ***  __INSERÇÃO COM BALANCEAMENTO DINÂMICO-ROTACIONAL__  ***  '))


    # .1 Inserção Comum

    noh_folha = self.__insere_noh_recursivo(self.__raiz, valor, debug)

    if debug:
      self.imprimir_propriedades()

    # .2 Análise do Balanceamento

    if debug:
      print(self.__cabecalho('Análise Descendente do Balanceamento', ' '))

    noh_desbalanceado = self.get_noh_mais_profundo_desbalanceado(debug)

    if debug:
      if noh_desbalanceado:
        print('\nRESULTADO >> Árvore desbalanceada no noh {}'.format(noh_desbalanceado))
      else:
        print('\nRESULTADO >> A árvore está balanceada.')


    # .2a Árvore Balanceada - nada a fazer
    if not noh_desbalanceado:
      return noh_folha


    # Realizando o Balanceamento     ...........................................

    # .3 Busca do Noh Pai

    if debug: print(self.__cabecalho('Encontrando o Noh_Pai do Noh_Desequilibrado',' '))

    pai = self.get_noh_pai(noh_desbalanceado, debug)

    if debug:
      print('Pai do filho rebelde:', pai)
      print(self.__cabecalho('Rotacionar para Balancear', '.'))

    self.rotacionar(noh_desbalanceado, pai, debug)    # Onde a mágica acontece


    # Conferindo o Balanceamento

    if debug:
      print(self.__cabecalho('Conferindo o Balanceamento','.'))
      noh_desbalanceado = self.get_noh_mais_profundo_desbalanceado(debug)
      self.imprimir_propriedades()
      if noh_desbalanceado:
        print('\nRESULTADO >> Árvore desbalanceada no noh {}'.format(noh_desbalanceado))
      else:
        print('\nRESULTADO >> A árvore está balanceada.')

    return self.busca_noh(valor, debug=False)


  # Inserção Russa AVL     -------------------------------------------------------------------------

  def insere_noh_avl(self, valor, debug=False):

    historico_geracoes = list()   # uma PILHA, na verdade
    if debug: print(self.__cabecalho('Inserção do valor: {}'.format(valor), ' '))

    self.__insere_noh_avl_recursivo(self.__raiz, valor, historico_geracoes, debug)

    # Conferindo o Balanceamento
    if debug:
      print(self.__cabecalho('Conferindo o Balanceamento','.'))
      noh_desbalanceado = self.get_noh_mais_profundo_desbalanceado(debug)
      self.imprimir_propriedades()
      if noh_desbalanceado:
        print('\nRESULTADO >> Árvore desbalanceada no noh {}'.format(noh_desbalanceado))
      else:
        print('\nRESULTADO >> A árvore está balanceada.')


  def __insere_noh_avl_recursivo(self, noh_atual, valor, historico_geracoes, debug=False):

    historico_geracoes.append(noh_atual)  # EMPILHA

    if self.arvore_vazia():

      if debug: print('#.__insere_noh_dinamico_rotacional: A árvore está vazia.')

      noh_folha = self.__insere_noh_recursivo(self.__raiz, valor, debug)

      if debug:
        caixa = self.__encaixotar(noh_folha, posicao=4)
        print('\nNoh inserido..\n{}\n----------'.format(caixa))

      return noh_folha


    # Descer pelo galho da esquerda
    if valor < noh_atual.get_conteudo():
      galho = noh_atual.get_subarvore_esquerda()

      # se tiver galho, continuar descendo  |=>   RECURSÃO !!!
      if not ( galho == None ):
        self.__insere_noh_avl_recursivo(galho, valor, historico_geracoes, debug)
      else:
        # estou na extremidade, adicionar noh_folha
        noh_folha = self.__Noh_ArvoreBinaria(valor)
        noh_atual.set_subarvore_esquerda(noh_folha)
        self.set_quantidade_noh( self.get_quantidade_noh() + 1 )
        # Registro de nascimento
        historico_geracoes.append(noh_folha)

        if debug:
          caixa = self.__encaixotar(noh_folha, posicao=4)
          print('\nNoh inserido..\n{}\n----------'.format(caixa))

        # FIZ A INSERÇÃO >> Verificar balanceamento

        # Conferindo equilíbrio da árvore de baixo para cima  ................
        #
        # Preciso tratar o noh_raiz_problema, o desbalanceado que seja o mais profundo,
        #  não os desequilibrados por efeito colateral.
        #
        # No loop, o noh que está sendo avaliado é o noh_filho.
        # Pode acontecer do noh desbalanceado ser o próprio noh_raiz.
        # Neste caso, o noh_filho será o noh_raiz e o noh_pai será None.

        noh_filho = historico_geracoes.pop()  # último a ser inserido
        noh_pai   = historico_geracoes.pop()

        if debug:
          print(self.__cabecalho('Análise Ascendente do Balanceamento',' '))
          print('Subindo pelo caminho da descida a partir do noh inserido:')
          primeira_vez = True

        while noh_filho:
          if debug:
            if not primeira_vez: print('>> UP!!')
            primeira_vez = False

          balanceamento = self.__get_balanceamento(noh_filho)
          if debug:
            self.desenhar_noh(noh_filho, balanceamento)

          if abs(balanceamento) > 1:  # noh desbalanceado
            if debug:
              msg = '>> Desequilíbrio encontrado do lado '
              msg += 'esquerdo !' if balanceamento > 0 else 'direito !'
              print(msg)

            self.rotacionar(noh_filho, noh_pai, debug)

            break   # pára tudo, serviço pronto

          # desempilha - sobe pela árvore
          noh_filho = noh_pai
          noh_pai   = historico_geracoes.pop() if historico_geracoes else None

        else:
          if debug: print('Balanceamento: OK ')

    else:
      # Descer pelo galho da direita
      galho = noh_atual.get_subarvore_direita()

      # se tiver galho, continuar descendo  |=>   RECURSÃO !!!
      if not ( galho == None ):
        self.__insere_noh_avl_recursivo(galho, valor, historico_geracoes, debug)
      else:
        # já estou na ponta, adicionar noh-folha
        noh_folha = self.__Noh_ArvoreBinaria(valor)
        noh_atual.set_subarvore_direita(noh_folha)
        self.set_quantidade_noh( self.get_quantidade_noh() + 1 )
        historico_geracoes.append(noh_folha)

        if debug:
          print('Noh inserido.\n{}\n----------'.format(self.__encaixotar(noh_folha,posicao=4)))

        # FIZ A INSERÇÃO >> Verificar balanceamento

        noh_filho = historico_geracoes.pop()  # último a ser inserido
        noh_pai   = historico_geracoes.pop()

        if debug:
          print(self.__cabecalho('Análise Ascendente do Balanceamento',' '))
          print('Subindo pelo caminho da descida a partir do noh inserido:')
          primeira_vez = True

        while noh_filho:
          if debug:
            if not primeira_vez: print('>> UP!!')
            primeira_vez = False

          balanceamento = self.__get_balanceamento(noh_filho)
          if debug:
            self.desenhar_noh(noh_filho, balanceamento)

          if abs(balanceamento) > 1:  # noh desbalanceado
            if debug:
              msg = '>> Desequilíbrio encontrado do lado '
              msg += 'esquerdo !' if balanceamento > 0 else 'direito !'
              print(msg)

            self.rotacionar(noh_filho, noh_pai, debug)

            break   # pára tudo, serviço pronto

          # desempilha - sobe pela árvore
          noh_filho = noh_pai
          noh_pai   = historico_geracoes.pop() if historico_geracoes else None

        else:
          if debug: print('Balanceamento: OK ')

    return self.busca_noh(valor, debug=False)


  # ================================================================================================
  # Rotações     -----------------------------------------------------------------------------------

  # Diagnosticar Tipo de Rotação     ---------------------------------------------------------------

  def diagnosticar_tipo_rotacao(self, noh_desbalanceado, debug=False):

    if not noh_desbalanceado:
      return None

    tipos = {
      'se' : 'SIMPLES_ESQUERDA',
      'sd' : 'SIMPLES_DIREITA',
      'dd' : 'DUPLA_DIREITA',
      'de' : 'DUPLA_ESQUERDA'}

    tipo = None

    # Modelagem & Concepção     --------------------------------------------------------------------
    #                            _____         ===
    #                           | avo |           |
    #                     _____ /¨¨¨¨¨            |
    #                    | pai |                  |
    #            _______ /¨¨¨¨¨                    >  Níveis
    #           | filho |                         |
    #    ______ /¨¨¨¨¨¨¨                          |
    #   | neto |                                  |
    #    ¨¨¨¨¨¨                                ===
    #
    # O noh-avo (+2 ou -2) foi desbalanceado pelo nascimento de um netinho(ou além*),
    #  pela inserção do noh-neto na árvore genealógica da família.
    # (* - econtrei um caso de tataraneto..., a causa pode estar bem mais abaixo)
    #
    # SIMPLES_DIREITA  -> se o filho estiver a esquerda de um pai também a esquerda do avo
    #                  _____
    #                 | avo |
    #           _____ /¨¨¨¨¨
    #          | pai |
    #  _______ /¨¨¨¨¨
    # | filho |
    #  ¨¨¨¨¨¨¨
    # SIMPLES_ESQUERDA -> se o filho estiver a direita de um pai também a direita do avo
    #    _____
    #   | avo |
    #    ¨¨¨¨¨\ _____
    #          | pai |
    #           ¨¨¨¨¨\ _______
    #                 | filho |
    #                  ¨¨¨¨¨¨¨
    # DUPLA_DIREITA  -> se o filho estiver a direita de um pai que esteja a esquerda do avo
    #                  _____
    #                 | avo |
    #           _____ /¨¨¨¨¨
    #          | pai |
    #           ¨¨¨¨¨\ _______
    #                 | filho |
    #                  ¨¨¨¨¨¨¨
    # DUPLA_ESQUERDA -> se o filho estiver a esquerda de um pai que esteja a direita  do avo
    #    _____
    #   | avo |
    #    ¨¨¨¨¨\ _____
    #          | pai |
    #  _______ /¨¨¨¨¨
    # | filho |
    #  ¨¨¨¨¨¨¨
    # ----------------------------------------------------------------------------------------------

    # Perguntado aos varões "De que lado está o netinho" - mais velhos primeiros

    avo = noh_desbalanceado

    # "Ooh vô, onde que eu acho o netinho"
    balanceamento = self.__get_balanceamento(avo)

    if balanceamento > 0:
      # R_avo: vá para a esquerda
      pai = avo.get_subarvore_esquerda()

      # "Pai, cadê seu filho"
      balanceamento = self.__get_balanceamento(pai)

      if balanceamento > 0:   # R_pai: está a esquerda
        tipo = tipos.get('sd')
        if debug: print('SIMPLES_DIREITA: pai_esquerda - filho_esquerda')

      else:                   # R_pai: está a direita
        tipo = tipos.get('dd')
        if debug: print('DUPLA_DIREITA: pai_esquerda - filho_direita')
    else:
      # R_avo: vá para direita
      pai = avo.get_subarvore_direita()

      # "Pai, cadê seu filho"
      balanceamento = self.__get_balanceamento(pai)

      if balanceamento > 0:   # R_pai: está a esquerda
        tipo = tipos.get('de')
        if debug: print('DUPLA_ESQUERDA: pai_direita - filho_esquerda')
      else:                   # R_pai: está a direita
        tipo = tipos.get('se')
        if debug: print('SIMPLES_ESQUERDA: pai_direita - filho_direita')

    return tipo


  # Rotacionar - Seletor de Rotação     ------------------------------------------------------------

  def rotacionar(self, avo, bisavo, debug=False):

  # param: avo é o noh desbalanceado

    if debug: print(self.__cabecalho('Diagnóstico do Tipo de Rotação',' '))

    tipo = self.diagnosticar_tipo_rotacao(avo, debug)

    if debug: print(self.__cabecalho('Invocando Rotação',' '))

    if tipo == 'SIMPLES_DIREITA':
      self.rotacionar_simples_direita(avo, bisavo, debug)

    elif tipo == 'SIMPLES_ESQUERDA':
      self.rotacionar_simples_esquerda(avo, bisavo, debug)

    elif tipo == 'DUPLA_DIREITA':
      self.rotacionar_dupla_direita(avo, bisavo, debug)

    elif tipo == 'DUPLA_ESQUERDA':
      self.rotacionar_dupla_esquerda(avo, bisavo, debug)



  # Rotacionar - Simples a Direita     -------------------------------------------------------------

  def rotacionar_simples_direita(self, avo, bisavo, debug=False):

    # OBS.: avo pode ser o noh-raiz..., e portanto bisavo = None
    if bisavo:
      # descobrindo de que lado o avo está do bisavo
      mao_esquerda = bisavo.get_subarvore_esquerda()
      mao_direita  = bisavo.get_subarvore_direita()

      if avo == mao_esquerda:   # avo segura a mão esquerda do bisavo
        mao_direita = None
      else:                     # avo segura a mão direita  do bisavo
        mao_esquerda = None

    pai   = avo.get_subarvore_esquerda()
    filho = pai.get_subarvore_esquerda()            # certamente tem
    filho_direito = pai.get_subarvore_direita()     # pode ser None

    if debug:
      print('{:_<31}'.format(''))
      print('|{:_^29}|'.format('Rotação Simples Direita'))
      print('| bisavo        {: <14}|'.format(str(bisavo)))
      print('| avo           {: <14}|'.format(str(avo)))
      print('| pai           {: <14}|'.format(str(pai)))
      print('| filho         {: <14}|'.format(str(filho)))
      print('| filho_direito {: <14}|'.format(str(filho_direito)))
      print('\'{:-<29}\''.format(''))


    # Quebrando laços familiares

    if debug: print('\n *** \"[\" - Quebrando laços de família ***')

    # BISAVO -> None | AVO solto
    if debug: print('\n[ #.1 - Desprende avo do bisavo, se existir')

    if bisavo:  # se existir
      if debug:
        print('>> Antes:')
        self.desenhar_noh(bisavo)

      if mao_esquerda:
        bisavo.set_subarvore_esquerda(None)                             # [1.a
      elif mao_direita:
        bisavo.set_subarvore_direita(None)                              # [1.b

      if debug:
        print('Depois:')
        self.desenhar_noh(bisavo)

    # AVO_esquerda -> None | PAI solto
    if debug:
      print('\n[ #.2 - Desprende pai do avo')
      print('>> Antes:')
      self.desenhar_noh(avo)

    avo.set_subarvore_esquerda(None)                                    # [2

    if debug:
      print('>> Depois:')
      self.desenhar_noh(avo)

    # PAI_direita -> None | FILHO solto
    if debug:
      print('\n[ #.3 - Desprende filho direito do pai')
      print('>> Antes:')
      self.desenhar_noh(pai)

    pai.set_subarvore_direita(None)                                     # [3

    if debug:
      print('>> Depois:')
      self.desenhar_noh(pai)


    # Reencarnações fazendo novos laços de família

    if debug: print('\n *** \"]\" - Reencarnações fazendo novos laços familiares ***')

    # AVO_esquerda -> FILHO_direito
    if debug:
      print('\n#.3] - Prendendo filho_direito ao avo')
      print('>> Antes:')
      self.desenhar_noh(avo)

    avo.set_subarvore_esquerda(filho_direito)                           # 3]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(avo)

    # PAI_direita -> AVO
    if debug:
      print('\n#.2] - Reconecta avo ao pai')
      print('>> Antes:')
      self.desenhar_noh(pai)

    pai.set_subarvore_direita(avo)                                      # 2]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(pai)

    # BISAVO -> PAI
    if debug: print('\n#.1] - Reconecta a prole ao bisavo')

    if bisavo:  # se existir
      if debug:
        print('>> Antes:')
        self.desenhar_noh(bisavo)

      if mao_direita:
        bisavo.set_subarvore_direita(pai)                               # 1.b]
      elif mao_esquerda:
        bisavo.set_subarvore_esquerda(pai)                              # 1.a]

      if debug:
        print('Depois:')
        self.desenhar_noh(bisavo)


  # Rotacionar - Simples a Esquerda     ------------------------------------------------------------

  def rotacionar_simples_esquerda(self, avo, bisavo, debug=False):

    # OBS.: avo pode ser o noh-raiz..., e portanto bisavo = None
    if bisavo:
      # descobrindo de que lado o avo está do bisavo
      mao_esquerda = bisavo.get_subarvore_esquerda()
      mao_direita  = bisavo.get_subarvore_direita()

      if avo == mao_esquerda:   # avo segura a mão esquerda do bisavo
        mao_direita = None
      else:                     # avo segura a mão direita  do bisavo
        mao_esquerda = None

    pai   = avo.get_subarvore_direita()
    filho = pai.get_subarvore_direita()            # certamente tem
    filho_esquerdo = pai.get_subarvore_esquerda()  # pode ser None

    if debug:
      print('{:_<31}'.format(''))
      print('|{:_^29}|'.format('Rotação Simples Direita'))
      print('| bisavo         {: <13}|'.format(str(bisavo)))
      print('| avo            {: <13}|'.format(str(avo)))
      print('| pai            {: <13}|'.format(str(pai)))
      print('| filho          {: <13}|'.format(str(filho)))
      print('| filho_esquerdo {: <13}|'.format(str(filho_esquerdo)))
      print('\'{:-<29}\''.format(''))


    # Quebrando laços familiares

    if debug: print('\n *** \"[\" - Quebrando laços de família ***')

    # BISAVO -> None | AVO solto
    if debug: print('\n[ #.1 - Desprende avo do bisavo, se existir')

    if bisavo:  # se existir
      if debug:
        print('>> Antes:')
        self.desenhar_noh(bisavo)

      if mao_esquerda:
        bisavo.set_subarvore_esquerda(None)                             # [1.a
      elif mao_direita:
        bisavo.set_subarvore_direita(None)                              # [1.b

      if debug:
        print('Depois:')
        self.desenhar_noh(bisavo)

    # AVO_direita -> None | PAI solto
    if debug:
      print('\n[ #.2 - Desprende pai do avo')
      print('>> Antes:')
      self.desenhar_noh(avo)

    avo.set_subarvore_direita(None)                                     # [2

    if debug:
      print('>> Depois:')
      self.desenhar_noh(avo)

    # PAI_esquerda -> None | FILHO solto
    if debug:
      print('\n[ #.3 - Desprende filho esquerdo do pai')
      print('>> Antes:')
      self.desenhar_noh(pai)

    pai.set_subarvore_esquerda(None)                                    # [3

    if debug:
      print('>> Depois:')
      self.desenhar_noh(pai)


    # Reencarnações fazendo novos laços de família

    if debug: print('\n *** \"]\" - Reencarnações fazendo novos laços familiares ***')

    # AVO_direita -> FILHO_esquerdo
    if debug:
      print('\n#.3] - Prendendo filho_esquerdo ao avo')
      print('>> Antes:')
      self.desenhar_noh(avo)

    avo.set_subarvore_direita(filho_esquerdo)                           # 3]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(avo)

    # PAI_esquerda -> AVO
    if debug:
      print('\n#.2] - Reconecta avo ao pai')
      print('>> Antes:')
      self.desenhar_noh(pai)

    pai.set_subarvore_esquerda(avo)                                     # 2]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(pai)

    # BISAVO -> PAI
    if debug: print('\n #.1] - Reconecta a prole ao bisavo')

    if bisavo:  # se existir
      if debug:
        print('>> Antes:')
        self.desenhar_noh(bisavo)

      if mao_direita:
        bisavo.set_subarvore_direita(pai)                               # 1.b]
      elif mao_esquerda:
        bisavo.set_subarvore_esquerda(pai)                              # 1.a]

      if debug:
        print('Depois:')
        self.desenhar_noh(bisavo)


  # Rotacionar - Dupla a Direita     ---------------------------------------------------------------

  def rotacionar_dupla_direita(self, avo, bisavo, debug=False):

    avo_eh_noh_raiz = avo == self.__raiz

    pai   = avo.get_subarvore_esquerda()
    filho = pai.get_subarvore_direita()
    neto  = filho.get_subarvore_direita()          # certamente tem
    neto_esquerdo = filho.get_subarvore_esquerda() # pode ser None

    if debug:
      print('{:_<29}'.format(''))
      print('|{:_^27}|'.format('Rotação Dupla Direita'))
      print('| bisavo        {: <12}|'.format(str(bisavo)))
      print('| avo           {: <12}|'.format(str(avo)))
      print('| pai           {: <12}|'.format(str(pai)))
      print('| filho         {: <12}|'.format(str(filho)))
      print('| neto          {: <12}|'.format(str(neto)))
      print('| neto_esquerdo {: <12}|'.format(str(neto_esquerdo)))
      print('\'{:-<27}\''.format(''))


    # 1o Rotação     .............................................................

    # Quebrando laços familiares

    if debug: print('\n *** 1a Rotação, 1o Movimento: \"[\" - Quebrando laços familiares ***')


    # AVO_esquerda -> None | PAI solto
    if debug:
      print('\n [#.1 - Desprende pai do avo')
      print('>> Antes:')
      self.desenhar_noh(avo)

    avo.set_subarvore_esquerda(None)                                    # [1

    if debug:
      print('>> Depois:')
      self.desenhar_noh(avo)

    # PAI_direita -> None | FILHO solto
    if debug:
      print('\n [#.2 - Desprende filho do pai')
      print('>> Antes:')
      self.desenhar_noh(pai)

    pai.set_subarvore_direita(None)                                     # [2

    if debug:
      print('>> Depois:')
      self.desenhar_noh(pai)

    # FILHO_esquerda -> None | NETO_esquerdo solto
    if debug:
      print('\n [#.3 - Desprende neto_esquerdo')
      print('>> Antes:')
      self.desenhar_noh(filho)

    filho.set_subarvore_esquerda(None)                                  # [3

    if debug:
      print('>> Depois:')
      self.desenhar_noh(filho)


    # Criando laços temporários

    if debug: print('\n *** 1o  Rotação, 2o Movimento: \"]\" - Criando laços temporários ***')


    # PAI_direita -> NETO_esquerdo
    if debug:
      print('\n #.3] - Prendendo neto_esquerdo ao pai')
      print('>> Antes:')
      self.desenhar_noh(pai)

    pai.set_subarvore_direita(neto_esquerdo)                            # 3]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(pai)

    # FILHO_esquerda -> PAI
    if debug:
      print('\n #.2] - Pai fica a esquerda do filho')
      print('>> Antes:')
      self.desenhar_noh(filho)

    filho.set_subarvore_esquerda(pai)                                   # 2]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(filho)

    # AVO_esquerda -> FILHO
    if debug:
      print('\n #.1] - Filho no lugar do pai, segura mão esquerda do avo')
      print('>> Antes:')
      self.desenhar_noh(avo)

    avo.set_subarvore_esquerda(filho)                                   # 1]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(avo)


    # 2o Rotação     .............................................................

    # avo pode ser o noh-raiz..., e portanto bisavo = None
    if bisavo:   # se existir
      # descobrindo de que lado o avo está do bisavo
      mao_esquerda = bisavo.get_subarvore_esquerda()
      mao_direita  = bisavo.get_subarvore_direita()

      if avo == mao_esquerda:   # avo segura a mão esquerda do bisavo
        mao_direita = None
      else:                     # avo segura a mão direita  do bisavo
        mao_esquerda = None


    # Quebrando laços familiares novamente

    if debug:
      print('\n\n *** 2o Rotação, 1o Movimento: \"[\" - Quebrando laços familiares novamente ***')


    # BISAVO -> None | AVO solto
    if debug: print('\n [#.1 - Desprende avo do bisavo, se existir')

    if bisavo:  # se existir
      if debug:
        print('>> Antes:')
        self.desenhar_noh(bisavo)

      if mao_esquerda:
        bisavo.set_subarvore_esquerda(None)                             # [1.a
      elif mao_direita:
        bisavo.set_subarvore_direita(None)                              # [1.b

      if debug:
        print('Depois:')
        self.desenhar_noh(bisavo)

    # AVO_esquerda -> None | FILHO solto
    if debug:
      print('\n [#.2 - Desprende filho do avo:')
      print('>> Antes:')
      self.desenhar_noh(avo)

    avo.set_subarvore_esquerda(None)                                    # [2

    if debug:
      print('Depois:')
      self.desenhar_noh(avo)

    # FILHO_direita -> None | NETO solto
    if debug:
      print('\n [#.3 - Desprende neto do filho:')
      print('>> Antes:')
      self.desenhar_noh(filho)

    filho.set_subarvore_direita(None)                                   # [3

    if debug:
      print('Depois:')
      self.desenhar_noh(filho)


    # Recriando novos laços definitivos

    if debug: print('\n *** 2o Rotação, 2o Movimento: \"]\" - Recriando novos laços definitivos ***')


    # AVO_esquerda -> NETO
    if debug:
      print('\n #.3] - Neto fica a esquerda do avo:')
      print('>> Antes:')
      self.desenhar_noh(avo)

    avo.set_subarvore_esquerda(neto)                                    # 3]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(avo)

    # FILHO_direita -> AVO
    if debug:
      print('\n #.2] - Avo fica a direita do filho')
      print('>> Antes:')
      self.desenhar_noh(filho)

    filho.set_subarvore_direita(avo)                                    # 2]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(filho)

    # BISAVO -> FILHO
    if debug: print('\n #.1] - Reconecta bisavo a prole pelo filho:')

    if bisavo:  # se existir
      if debug:
        print('>> Antes:')
        self.desenhar_noh(bisavo)

      if mao_direita:
        bisavo.set_subarvore_direita(filho)                             # 1.b]
      elif mao_esquerda:
        bisavo.set_subarvore_esquerda(filho)                            # 1.a]

      if debug:
        print('Depois:')
        self.desenhar_noh(bisavo)

    # Se o avo, que foi reposicionado, era o noh_raiz, bisavo não existia (None).
    # Fixamos como raiz quem tomou seu lugar na reestruturação: o filho
    elif avo_eh_noh_raiz:
      self.set_raiz(filho)
      if debug:
        print('\nAvo era noh_raiz, agora o noh_raiz passa a ser o filho.\n')


  # Rotacionar - Dupla a Esquerda     --------------------------------------------------------------

  def rotacionar_dupla_esquerda(self, avo, bisavo, debug=False):

    avo_eh_noh_raiz = avo == self.__raiz

    pai   = avo.get_subarvore_direita()
    filho = pai.get_subarvore_esquerda()
    neto  = filho.get_subarvore_esquerda()          # certamente tem
    neto_direito = filho.get_subarvore_direita()    # pode ser None

    if debug:
      print('{:_<29}'.format(''))
      print('|{:_^27}|'.format('Rotação Dupla Direita'))
      print('| bisavo       {: <13}|'.format(str(bisavo)))
      print('| avo          {: <13}|'.format(str(avo)))
      print('| pai          {: <13}|'.format(str(pai)))
      print('| filho        {: <13}|'.format(str(filho)))
      print('| neto         {: <13}|'.format(str(neto)))
      print('| neto_direito {: <13}|'.format(str(neto_direito)))
      print('\'{:-<27}\''.format(''))


    # 1o Rotação     .............................................................

    # Quebrando laços familiares

    if debug: print('\n *** 1o Rotação, 1o Movimento: \"[\" - Quebrando laços familiares ***')


    # AVO_direita -> None | PAI solto
    if debug:
      print('\n [#.1 - Desprende pai do avo')
      print('>> Antes:')
      self.desenhar_noh(avo)

    avo.set_subarvore_direita(None)                                     # [1

    if debug:
      print('>> Depois:')
      self.desenhar_noh(avo)

    # PAI_esquerda -> None | FILHO solto
    if debug:
      print('\n [#.2 - Desprende filho do pai')
      print('>> Antes:')
      self.desenhar_noh(pai)

    pai.set_subarvore_esquerda(None)                                    # [2

    if debug:
      print('>> Depois:')
      self.desenhar_noh(pai)

    # FILHO_direita -> None | NETO_direito solto
    if debug:
      print('\n [#.3 - Desprende neto_direito')
      print('>> Antes:')
      self.desenhar_noh(filho)

    filho.set_subarvore_direita(None)                                   # [3

    if debug:
      print('>> Depois:')
      self.desenhar_noh(filho)


    # Criando laços temporários

    if debug: print('\n *** 1o Rotação, 2o Movimento: \"]\" - Criando laços temporários ***')


    # PAI_esquerda -> NETO_direito
    if debug:
      print('\n #.3] - Prendendo neto_direito ao pai')
      print('>> Antes:')
      self.desenhar_noh(pai)

    pai.set_subarvore_esquerda(neto_direito)                            # 3]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(pai)

    # FILHO_direita -> PAI
    if debug:
      print('\n #.2] - Pai fica a direita do filho')
      print('>> Antes:')
      self.desenhar_noh(filho)

    filho.set_subarvore_direita(pai)                                    # 2]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(filho)

    # AVO_direita -> FILHO
    if debug:
      print('\n #.1] - Filho no lugar do pai, segura mão direita do avo')
      print('>> Antes:')
      self.desenhar_noh(avo)

    avo.set_subarvore_direita(filho)                                    # 1]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(avo)


    # 2o Rotação     .............................................................

    # avo pode ser o noh-raiz..., e portanto bisavo = None
    if bisavo:   # se existir
      # descobrindo de que lado o avo está do bisavo
      mao_esquerda = bisavo.get_subarvore_esquerda()
      mao_direita  = bisavo.get_subarvore_direita()

      if avo == mao_esquerda:   # avo segura a mão esquerda do bisavo
        mao_direita = None
      else:                     # avo segura a mão direita  do bisavo
        mao_esquerda = None


    # Quebrando laços familiares novamente

    if debug:
      print('\n\n *** 2o Rotação, 1o Movimento: \"[\" - Quebrando laços familiares novamente ***')


    # BISAVO -> None | AVO solto
    if debug: print('\n[ #.1 - Desprende avo do bisavo, se existir')

    if bisavo:  # se existir
      if debug:
        print('>> Antes:')
        self.desenhar_noh(bisavo)

      if mao_esquerda:
        bisavo.set_subarvore_esquerda(None)                             # [1.a
      elif mao_direita:
        bisavo.set_subarvore_direita(None)                              # [1.b

      if debug:
        print('Depois:')
        self.desenhar_noh(bisavo)

    # AVO_direita -> None | FILHO solto
    if debug:
      print('\n [ #.2 - Desprende filho do avo:')
      print('>> Antes:')
      self.desenhar_noh(avo)

    avo.set_subarvore_direita(None)                                     # [2

    if debug:
      print('Depois:')
      self.desenhar_noh(avo)

    # FILHO_esquerda -> None | NETO solto
    if debug:
      print('\n [ #.3 - Desprende neto do filho:')
      print('>> Antes:')
      self.desenhar_noh(filho)

    filho.set_subarvore_esquerda(None)                                  # [3

    if debug:
      print('Depois:')
      self.desenhar_noh(filho)


    # Recriando novos laços definitivos

    if debug: print('\n *** 2o Rotação, 2o Movimento: \"]\" - Recriando novos laços definitivos ***')


    # AVO_esquerda -> NETO
    if debug:
      print('\n #.3] - Neto fica a direita do avo:')
      print('>> Antes:')
      self.desenhar_noh(avo)

    avo.set_subarvore_direita(neto)                                     # 3]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(avo)

    # FILHO_esquerda -> AVO
    if debug:
      print('\n #.2] - Avo fica a esquerda do filho')
      print('>> Antes:')
      self.desenhar_noh(filho)

    filho.set_subarvore_esquerda(avo)                                   # 2]

    if debug:
      print('>> Depois:')
      self.desenhar_noh(filho)


    # BISAVO -> FILHO
    if debug: print('\n#.1] - Reconecta bisavo a prole pelo filho:')

    if bisavo:  # se existir
      if debug:
        print('>> Antes:')
        self.desenhar_noh(bisavo)

      if mao_direita:
        bisavo.set_subarvore_direita(filho)                             # 1.b]
      elif mao_esquerda:
        bisavo.set_subarvore_esquerda(filho)                            # 1.a]

      if debug:
        print('Depois:')
        self.desenhar_noh(bisavo)

    # Se o avo, que foi reposicionado, era o noh_raiz, bisavo não existia (None).
    # Fixamos como raiz quem tomou seu lugar na reestruturação: o filho
    elif avo_eh_noh_raiz:
      self.set_raiz(filho)
      if debug:
        print('\nAvo era noh_raiz, agora o noh_raiz passa a ser o filho.\n')


  # ================================================================================================
  # Desenhos     -----------------------------------------------------------------------------------

  # Encaixotar - Desenha o valor do noh em uma caixinha     ----------------------------------------

  def __encaixotar(self, noh, balanceamento=None, posicao=0):

    valor = str(noh)
    numero_algarismo = len(valor)
    # 8 fica 08
    if numero_algarismo == 1:
      valor = '0' + valor
      numero_algarismo = 2
    tampa = ''
    fundo = ''
    for i in range(numero_algarismo):
      tampa += '_'
      fundo += '¨'
    empurra = ''
    for i in range(posicao):
      empurra += ' '

    linha2 = empurra + '|' + valor + '|\n'
    linha3 = empurra + ' ' + fundo

    # Montado sobrescrito do balanceamento, se fornecido
    balance = ''
    if not balanceamento == None:
      balance = str(balanceamento)
      # lado esquerdo
      if balanceamento > 0:
        balance = '+' + balance
      elif balanceamento == 0:
        balance = ' ' + balance
      # lado direito
      if balanceamento < 0:
        linha1  = empurra + ' ' + tampa + balance + ' \n'
      else:
        linha1  = empurra[:-1] + balance + tampa + ' \n'

    # se fator de balanceamento não foi passado
    else:
      linha1  = empurra + ' ' + tampa    + ' \n'

    caixa =  linha1 + linha2 + linha3

    return caixa


  # Desenhar Noh - Desenha o noh com seus ramos     ------------------------------------------------

  def desenhar_noh(self, noh, balanceamento=None, desenhar_folha=True):

    if not noh: print('Não há o que desenhar, noh =', noh)

    if self.__is_noh_folha(noh):
      if desenhar_folha:
        print(self.__encaixotar(noh, posicao=4))
      return



    CAIXA_VAZIA = '||'

    noh_esquerdo = noh.get_subarvore_esquerda()
    noh_direito  = noh.get_subarvore_direita()

    valor = str(noh)
    numero_algarismo = len(valor)
    # 3 vira 03
    if numero_algarismo == 1:
      valor = '0' + valor
      numero_algarismo = 2

    if noh_esquerdo:
      esquerdo = str(noh_esquerdo.get_conteudo())
      numero_algarismo_esquerdo = len(esquerdo)
      # 5 vira 05
      if numero_algarismo_esquerdo == 1:
        esquerdo = '0' + esquerdo
        numero_algarismo_esquerdo = 2
    else:
      numero_algarismo_esquerdo = len(CAIXA_VAZIA)
      esquerdo = '  '

    if noh_direito:
      direito = str(noh_direito.get_conteudo())
      numero_algarismo_direito  = len(direito)
      # 7 vira 07
      if numero_algarismo_direito == 1:
        direito = '0' + direito
        numero_algarismo_direito = 2
    else:
      numero_algarismo_direito  = len(CAIXA_VAZIA)
      direito = '  '


    # noh
    tampa = ''
    fundo = ''
    for i in range(numero_algarismo):
      tampa += '_'
      fundo += '¨'

    posicao = numero_algarismo_esquerdo + 1   # +1 pelo '/'
    empurra = ''
    for i in range(posicao):
      empurra += ' '

    # noh_esquerdo
    tampa_esquerda = ''
    fundo_esquerdo = ''
    for i in range(numero_algarismo_esquerdo):
      tampa_esquerda += '_'
      fundo_esquerdo += '¨'

    # noh_direito
    tampa_direita = ''
    fundo_direito = ''
    for i in range(numero_algarismo_direito):
      tampa_direita += '_'
      fundo_direito += '¨'

    posicao = numero_algarismo_esquerdo + numero_algarismo
    empurra_direita = ''
    for i in range(posicao):
      empurra_direita += ' '

    # Montado sobrescrito do balanceamento, se fornecido
    balance = '  '
    if not balanceamento == None:
      balance = str(balanceamento)
      # lado esquerdo
      if balanceamento > 0:
        balance = '+' + balance
      elif balanceamento == 0:
        balance = ' ' + balance
      # lado direito
      if balanceamento < 0:
        nivel1  = empurra + '  ' + tampa + balance + ' \n'
      else:
        nivel1  = empurra + balance + tampa + ' \n'

    # se fator de balanceamento não foi passado
    else:
      nivel1  = empurra + balance + tampa    + ' \n'

    nivel1 += empurra + ' |' + valor + '|\n'
    nivel1 += ' ' + tampa_esquerda + ' /' + fundo  + '\\ ' + tampa_direita +'\n'

    nivel2 =  '|' + esquerdo + '|' + empurra_direita + '|' + direito + '|\n'
    nivel2 += ' ' + fundo_esquerdo + empurra_direita + '  ' + fundo_direito

    desenho = nivel1 + nivel2

    print(desenho)


  # Desenhar Todos os Galhos     -------------------------------------------------------------------

  def desenhar_todos_galhos(self):
    self.__desenhar_todos_galhos_recursivo(self.get_raiz())

  def __desenhar_todos_galhos_recursivo(self, noh_atual):
    # fim da galhada
    if noh_atual == None:
      return

    #continuar descendo recursivamente
    if not noh_atual.is_inativo():
       self.desenhar_noh(noh_atual, desenhar_folha=False)

    self.__desenhar_todos_galhos_recursivo(noh_atual.get_subarvore_esquerda())
    self.__desenhar_todos_galhos_recursivo(noh_atual.get_subarvore_direita() )


  # ================================================================================================
  # Auxiliares     ---------------------------------------------------------------------------------

  # Cabecalho     ----------------------------------------------------------------------------------

  def __cabecalho(self, msg, caracter='_'):

    if caracter == '': caracter='_'
    grifo_caracter='-'
    if not caracter == ' ':
      grifo = '\n{:' + grifo_caracter + '<' + str(len(msg) + 5) + '}'
      grifo = grifo.format('    ')
      enchimento = '{:' + caracter + '<80}'
      margem = caracter + caracter + caracter
      msg = enchimento.format('\n' + margem + ' ' + msg + '    ')
    else:
      grifo = '\n{:' + grifo_caracter + '<' + str(len(msg) + 1) + '}'
      grifo = grifo.format('')
      enchimento = '{:' + caracter + '<80}'
      margem = ''
      msg = enchimento.format('\n' + margem + msg)
    return msg + grifo


  # Altura da Árvore ou Quantidade de Níveis     ---------------------------------------------------

  def get_altura(self):

    return self.__get_altura_recursivo(self.get_raiz())

  def __get_altura_recursivo(self, noh_atual):
    if not noh_atual:
      return 0
    else:
      galho_esquerdo = noh_atual.get_subarvore_esquerda()
      galho_direito = noh_atual.get_subarvore_direita()

      if not galho_esquerdo and not galho_direito:
        # estou em uma extremidade, em um noh-folha
        return 1
      else:
        nivel_profundidade_esquerda = 0
        if galho_esquerdo:
          nivel_profundidade_esquerda = self.__get_altura_recursivo(galho_esquerdo)

        nivel_profundidade_direita  = 0
        if galho_direito:
          nivel_profundidade_direita  = self.__get_altura_recursivo(galho_direito)

        nivel_mais_profundo = None

        if nivel_profundidade_esquerda > nivel_profundidade_direita:
          nivel_mais_profundo = nivel_profundidade_esquerda
        else:
          nivel_mais_profundo = nivel_profundidade_direita

        return nivel_mais_profundo + 1


  # Noh Mais Profundo Desbalanceado     ------------------------------------------------------------

  def get_noh_mais_profundo_desbalanceado(self, debug=False):

    noh_desbalanceado = self.__get_noh_mais_profundo_desbalanceado_recursivo(self.get_raiz(), debug)

    return noh_desbalanceado


  def __get_noh_mais_profundo_desbalanceado_recursivo(self, noh, debug=False):

    if self.__is_noh_folha(noh):
      return None

    noh_desbalanceado = None

    # Checando se o próprio nó está desbalanceado
    balanceamento = self.__get_balanceamento(noh, debug)    # x
    if abs(balanceamento) > 1:
      noh_desbalanceado = noh
      if debug: print('Noh Desbalanceado Corrente >>', noh_desbalanceado)

    # O balanceamento ilumina o caminho até o noh desbalanceado, basta seguir
    #  pelo lado que ele indicar; se for zero, é preciso descer pelos dois lados

    # Descer pelo galho esquerdo
    if balanceamento >= 0:
      if debug:
        if balanceamento in (0, 1):   # imprimir x se x C {0,+1}
          print(' {} >> Noh Equilibrado'.format(noh))
        else:
          print('>> Desequilíbrio encontrado do lado esquerdo !')

      noh_esquerdo = noh.get_subarvore_esquerda()

      if noh_esquerdo:
        if not self.__is_noh_folha(noh_esquerdo):     # RECURSIVIDADE
          noh_mais_profundo = self.__get_noh_mais_profundo_desbalanceado_recursivo(noh_esquerdo, debug)

          # The Cat's Jump
          if noh_mais_profundo and not noh_mais_profundo is noh_desbalanceado:
            # novo noh_problemático
            noh_desbalanceado = noh_mais_profundo

    # Descer pelo galho direito
    if balanceamento <= 0:
      if debug:
        # -2 > noh_equilibrado < 2 |=> i.e. {-1,0,+1}
        # nos casos em que for == 0, o print de "noh equilibrado" já foi feito quando
        # desceu pelo galho esquerdo: {0,+1}, portanto só imprimir x se x C {-1},
        # senão seria executado 2x para o mesmo noh
        if balanceamento == -1:
          print(' {} >> Noh Equilibrado'.format(noh))
        elif balanceamento < -1:
          print('>> Desequilíbrio encontrado do lado direito !')

      noh_direito = noh.get_subarvore_direita()

      if noh_direito:
        if not self.__is_noh_folha(noh_direito):      # RECURSIVIDADE
          noh_mais_profundo = self.__get_noh_mais_profundo_desbalanceado_recursivo(noh_direito, debug)

          # O Pulo do Gato
          if noh_mais_profundo and not noh_mais_profundo is noh_desbalanceado:
            # novo noh_problemático
            noh_desbalanceado = noh_mais_profundo

    if debug:
      if noh_desbalanceado:
        print('Retornando noh_desbalanceado: {}'.format(noh_desbalanceado))

    return noh_desbalanceado


  # Checar se é Noh Folha     ----------------------------------------------------------------------

  def __is_noh_folha(self, noh):

    # Nó folha não tem nenhum ramo, ninguém pendurado nele

    return not noh.get_subarvore_esquerda() and not noh.get_subarvore_direita()


  # Balanceamento do Noh     -----------------------------------------------------------------------

  def __get_balanceamento(self, noh, debug=False):

    noh_esquerdo = noh.get_subarvore_esquerda()
    noh_direito  = noh.get_subarvore_direita()

    profundidade_esquerda = self.__get_altura_recursivo(noh_esquerdo)
    profundidade_direita  = self.__get_altura_recursivo(noh_direito)
    balanceamento = profundidade_esquerda - profundidade_direita
    if debug:
      print('\nNOH',noh)
      print('profundidade esquerda', profundidade_esquerda)
      print('profundidade direita ', profundidade_direita)
      self.desenhar_noh(noh, balanceamento)

    return balanceamento


  # Encontrar o Noh Pai do Filho Rebelde     -------------------------------------------------------

  def get_noh_pai(self, noh_filho, debug=False):
    return self.__get_noh_pai_recursivo(self.__raiz, noh_filho, debug)

  def __get_noh_pai_recursivo(self, noh_atual, noh_filho, debug=False):

    if self.arvore_vazia():
      if debug: print('Árvore vazia. O elemento \"{}\" não está na árvore.'.format(noh_filho))
      return None

    if not noh_filho:
      if debug: print ('O noh está None. Não tem pai.')
      return None

    if noh_filho == self.__raiz:
      if debug: print ('O noh {} é o noh_raiz da árvore. Não tem pai.'.format(noh_filho))
      return None

    # O noh-pai estará segurando o filho em uma das mãos
    mao_esquerda = noh_atual.get_subarvore_esquerda()
    mao_direita  = noh_atual.get_subarvore_direita()

    # Checando se o menino segura uma das mãos
    if noh_filho in (mao_esquerda, mao_direita):
      if debug: print( ' {}  PAPAIiêêê..!!!'.format(noh_atual) )
      return noh_atual

    # Continuar procurando...
    valor = noh_filho.get_conteudo()

    if valor < noh_atual.get_conteudo():

      if debug: print('E > ', end='')       # indo para esquerda
      noh_atual = noh_atual.get_subarvore_esquerda()

      if noh_atual:
        return self.__get_noh_pai_recursivo(noh_atual, noh_filho, debug)    # RECURSÃO !!!
      else:
        if debug: print( '\nO elemento \"{}\" é filho de chocadeira.'.format(noh_filho) )
        return None

    else:
      if debug: print('D > ', end='')       # indo para direita
      noh_atual = noh_atual.get_subarvore_direita()
      if noh_atual:
        return self.__get_noh_pai_recursivo(noh_atual, noh_filho, debug)    # RECURSÃO !!!
      else:
        if debug: print( '\nO noh-filho \"{}\" não tem pai.'.format(noh_filho) )
        return None


  # Criar Árvore a Partir um Galho Pronto/Montado     ----------------------------------------------

  def criar_arvore(self, noh_raiz):

    arvore = ArvoreBinaria()
    arvore.set_raiz(noh_raiz)
    arvore.set_quantidade_noh(arvore.conta_noh())

    return arvore


  # Contar a Quantidade de Nohs     ----------------------------------------------------------------

  def conta_noh(self):

    lista = self.__get_lista_ordenada_recursivo(self.get_raiz(), list())

    return len(lista)


  # Extrair Lista Ordenada dos Conteúdos dos Nós da Árvore     -------------------------------------

  def get_lista_ordenada(self):
    return self.__get_lista_ordenada_recursivo(self.get_raiz(), list())

  def __get_lista_ordenada_recursivo(self, noh_atual, lista):
    if noh_atual == None:
      return lista

    # percorrer recursivamente adicionando os nós
    self.__get_lista_ordenada_recursivo(noh_atual.get_subarvore_esquerda(), lista)
    if not noh_atual.is_inativo():
       lista.append(noh_atual.get_conteudo())
    self.__get_lista_ordenada_recursivo(noh_atual.get_subarvore_direita(), lista)

    return lista


  # Extrair lista de Inserção Otimizada     --------------------------------------------------------

  def get_pilha_insercao_balanceada(self):
    pilha = self.__get_pilha_insercao_balanceada_recursivo( self.get_lista_ordenada() )
    # Topo a esquerda: pilha[0]
    pilha_otimizada = list()
    while pilha:
      pilha_otimizada.append(pilha.pop())

    return pilha_otimizada

  def __get_pilha_insercao_balanceada_recursivo(self, lista_ordenada):
    pilha = list()

    # galho sem folha
    n = len(lista_ordenada)
    if n == 0:
      return None

    # única folha
    if n == 1:
      return lista_ordenada


    # temos uma galhada...

    indice_mediana = int( n/2 - 1 if n%2 == 0 else n/2 )
    mediana = lista_ordenada[indice_mediana]

    galho_esquerdo = lista_ordenada[:indice_mediana]
    galho_direito  = lista_ordenada[indice_mediana + 1:]

    # Recursividade - descendo pelos galhos...
    ordem_insercao_esquerda = self.__get_pilha_insercao_balanceada_recursivo(galho_esquerdo)
    ordem_insercao_direita  = self.__get_pilha_insercao_balanceada_recursivo(galho_direito)


    # Forquilha com galhos dos dois lados - montando galhada única

    if ordem_insercao_esquerda and ordem_insercao_direita:
      # empilhar alternadamente
      for i in range(len(ordem_insercao_esquerda)):
        pilha.append(ordem_insercao_esquerda[i])
        pilha.append(ordem_insercao_direita[i])

      # Em galhos pares(n=8, i=[0-7]), após remover a mediana(i=3), teremos à direita(4,5,6,7);
      #  um elemento a mais que à esquerda(0,1,2), logo, falta adicionar esse último
      if len(ordem_insercao_esquerda) < len(ordem_insercao_direita):    # par
        pilha.append(ordem_insercao_direita.pop())


    # Acontecerá de descermos por galhos que só tem ramos em um dos lados

    elif ordem_insercao_esquerda:
      pilha.extend(ordem_insercao_esquerda)

    elif ordem_insercao_direita:
      pilha.extend(ordem_insercao_direita)


    pilha.append(mediana)


    return pilha

  def imprimir_propriedades(self):
    print(self.__cabecalho('Propriedades da Árvore', ' '))
    print('Percurso pré-ordem:', end=' ')
    self.percurso_pre_ordem()
    print('\nPercurso pós-ordem:', end=' ')
    self.percurso_pos_ordem()
    print('\nPercurso simétrico:', end=' ')
    self.percurso_simetrico()
    print( '\nTotal de elementos: {}'.format(self.get_quantidade_noh()) )
    print('Altura:', self.get_altura())

# ==================================================================================================
# ==================================================================================================
# ==================================================================================================



# ==================================================================================================
# PROGRAMA PRINCIPAL - FRONT-END_UI - Execução de Testes     ---------------------------------------
# --------------------------------------------------------------------------------------------------
def main():

  """ Método main() - Execução de Testes """

  # ================================================================================================
  # Variáveis     ----------------------------------------------------------------------------------

  # Constantes para escolha do menu de balanceamento
  ESTATICO =            1
  DINAMICO_ESTATICO =   2
  DINAMICO_ROTACIONAL = 3
  DINAMICO_RUSSO_AVL =  4
  SAIR =                9


  # Constantes para escolha das opções do método de balanceamento
  EXIBIR_INFO =            0
  INSERIR_VALOR =          1
  DESENHAR_GALHOS =        2
  CHECAR_BALANCEAMENTO =   3
  REALIZAR_BALANCEAMENTO = 4
  REINICIAR_ARVORE =       7
  MUDAR_METODO =           8

  opcoes_menu_metodos_balanceamento = {
        1 : 'ESTATICO',
        2 : 'DINAMICO_ESTATICO',
        3 : 'DINAMICO_ROTACIONAL',
        4 : 'DINAMICO_RUSSO_AVL',
    9 : 'SAIR',
    }

  opcoes_estatico = {
    0 : 'EXIBIR_INFO',
    1 : 'INSERIR_VALOR',
        2 : 'DESENHAR_GALHOS',
        3 : 'CHECAR_BALANCEAMENTO',
        4 : 'REALIZAR_BALANCEAMENTO',
    7 : 'REINICIAR_ARVORE',
    8 : 'MUDAR_METODO',
        9 : 'SAIR'
    }

  opcoes_dinamico_estatico = {      # Não tem a opção "realizar balanceamento",
    0 : 'EXIBIR_INFO',              # porque já é feito no momento de cada inserção
    1 : 'INSERIR_VALOR',
        2 : 'DESENHAR_GALHOS',
        3 : 'CHECAR_BALANCEAMENTO',
    7 : 'REINICIAR_ARVORE',
    8 : 'MUDAR_METODO',
        9 : 'SAIR'
    }

  opcoes_dinamico_rotacional = dict(opcoes_dinamico_estatico)     # cópia - outro objeto
  opcoes_dinamico_russo_avl =  dict(opcoes_dinamico_rotacional)   # distinct dict #ref

  opcoes_balanceamento = {
    ESTATICO :            opcoes_estatico,
    DINAMICO_ESTATICO :   opcoes_dinamico_estatico,
    DINAMICO_ROTACIONAL : opcoes_dinamico_rotacional,
    DINAMICO_RUSSO_AVL :  opcoes_dinamico_russo_avl,

  }

  titulos = {
    ESTATICO :            "BALANCEAMENTO ESTÁTICO",
    DINAMICO_ESTATICO :   "BALANCEAMENTO DINÂMICO-ESTÁTICO",
    DINAMICO_ROTACIONAL : "BALANCEAMENTO DINÂMICO-ROTACIONAL",
    DINAMICO_RUSSO_AVL :  "BALANCEAMENTO DINÂMICO RUSSO-AVL",
  }



  # Informações sobre os métodos de balanceamento

  rotacoes = "\n{:-<80}".format('') + (
      "\n Rotações:"
      "\n\tSIMPLES_DIREITA:  inserir noh\'s 15 ou 50"
      "\n\tSIMPLES_ESQUERDA: inserir noh 95"
      "\n\tDUPLA_DIREITA:    inserir noh 62 ou 22"
      "\n\tDUPLA_ESQUERDA_*: inserir noh 70, seguido de 73 e por fim o noh 68"
      "\n\n \'*\' - Tendo por base a árvore original de testes, não é possível obtermos "
      "\n a rotação dupla-esquerda inserindo apenas um elemento. Nesta sugestão, "
      "\n a inserção dos noh\'s 70 e 73 não desequilibram a árvore, apenas a modifica, "
      "\n para que o desequilíbrio gerado pela adição do noh 68 resulte em uma "
      "\n rotação dupla-esquerda, a fim de se restabelecer o balanceamento da árvore."
      )
  info_estatico = (
       " Único método que permite a inserção de vários valores antes de se fazer o "
       "\nbalanceamento. Todos os demais já o realizam no momento da inserção. O método "
       "\nestático remove todos os elementos da árvore e os reinsere em uma ordem ótima, "
       "\nna qual a árvore ficará balanceada."
       "\n\n"
      )
  info_dinamico_estatico = (
      " Após a inserção do elemento, avalia-se o balanceamento da árvore. "
      "\nExecuta-se uma busca, a partir do noh-raiz, se há algum noh cujo módulo "
      "\ndo fator de balanceamento seja maior ou igual a 2 (|fb| >= 2). "
      "\nSe nenhum noh desbalanceado for encontrado, a árvore está balanceada. "
      "\n\n Caso seja encontrado, a árvore está desbalanceada e a busca deve continuar, "
      "\ndescendo pelo galho desequilíbrado, indicado pelo sinal do fator de balanceamento. "
      "\nHá ocasiões em que esse primeiro noh encontrado ficou desbalanceado por "
      "\nefeito colateral de um desequilíbrio mais profundo. Portanto, deve-se continuar "
      "\nbuscando até se encontrar o noh desequilibrado de maior profundidade. "
      "\nEncontrado, procede-se o balanceamento. "
      "\n\n O balanceamento é realizado criando-se um galho clone auxiliar, correspondente "
      "\na sub-árvore(ramo) desbalanceada, no qual o noh desequilibrado será o noh-raiz. "
      "\nAplica-se o balanceamento estático ao galho desbalanceado (galho clone). "
      "\nEm seguida, remove-se o galho desbalanceado e reinsere os elementos do "
      "\ngalho amputado, conectando o novo galho balanceado. "
      "\nQualquer noh superior que estivesse desequilibrado, caso houvesse, "
      "\ntornar-se-iria equilibrado, por corolário do reequilíbrio do ramo mais profundo. "
      "\n\n A principal diferença desta abordagem em relação ao balanceamento estático "
      "\né que, no puramente estático, remove-se todos os elementos, isto é, "
      "\no balanceamento é aplicado a árvore toda, enquanto na inserção "
      "\ndinâmica-estática remove-se apenas o ramo problemático, ou seja, "
      "\naplica-se o balanceamento apenas a um galho, sem afetar o restante da árvore."
      "\n\n"
      )
  info_dinamico_rotacional = (

      " Similar a inserção dinâmica-estática, após fazer a inserção do noh, avalia-se o "
      "\nbalanceamento da árvore, buscando o noh de maior profundidade, cujo módulo do "
      "\nfator de balanceamento seja maior ou igual a 2 (|fb| >= 2). "
      "\nA diferença está na forma de fazer o balanceamento. "
      "\n\n Neste método, aplica-se a rotação ao galho desbalanceado, a mesma rotação do "
      "\nmétodo AVL desenvolvida pelos russos. Identifica-se o tipo de rotação cabível "
      "\ne aplica a rotação adequada ao galho desbalanceado. "
      "\n\n Faz-se a busca pelo noh desbalanceado de cima para baixo, como na inserção "
      "\ndinâmica-estática, porém, para o balanceamento, o método dinâmico-rotacional "
      "\nutiliza as rotações do método russo AVL."
      )
  info_dinamico_rotacional += rotacoes + "\n\n"

  info_dinamico_russo_avl = (
      " Enquanto as inserções dinâmica-estática e dinâmica-rotacional fazem a busca do "
      "\nnoh desequilibrado de cima para baixo, e precisam continuar mergulhando até "
      "\nencontrar o noh-problema mais profundo, na técnica AVL dos russos, a busca "
      "\npelo desequilíbrio é de baixo para cima, à partir do noh recém inserido. "
      "\n\n Traz a vantagem de se fazer uma busca menor e mais rápida pelo desequilíbrio, "
      "\numa vez que o primeiro noh a ser encontrado já será o noh problemático "
      "\nmais profundo. E ainda tem a característica de fazer o mesmo número de "
      "\noperações para reequilibrar a árvore - as rotações, não importando a "
      "\nprofundidade da causa do desbalanceamento."
      )
  info_dinamico_russo_avl += rotacoes + "\n\n"

  info_metodos = {
    ESTATICO :            info_estatico,
    DINAMICO_ESTATICO :   info_dinamico_estatico,
    DINAMICO_ROTACIONAL : info_dinamico_rotacional,
    DINAMICO_RUSSO_AVL :  info_dinamico_russo_avl,
  }



    # Armazenar as escolhas realizadas pelo usuário
  escolhas = {'metodo' : -1, 'acao' : -1}

  # Árvore - variável global
  arvore = None

  # ================================================================================================
  # Métodos Auxiliares para Interação com o Usuário     --------------------------------------------

  # Cabeçalho de Seção     -------------------------------------------------------------------------

  def cabecalho_secao(msg, centralizado=True):
    texto = '\n{:=<80}'.format('') + '\n'
    if centralizado:
      msg = '   ' + msg + '   '
      texto += '{:-^80}'.format(msg)
    else:
      msg = ' ' + msg + '   '
      texto += '{:-<80}'.format(msg)

    return texto


  # Cabeçalho     ----------------------------------------------------------------------------------

  def cabecalho(msg, caracter='-'):
    if caracter == '': caracter='-'
    grifo_caracter='-'
    if not caracter == ' ':
      grifo = '\n{:' + grifo_caracter + '<' + str(len(msg) + 5) + '}'
      grifo = grifo.format('    ')
      enchimento = '{:' + caracter + '<81}'
      margem = caracter + caracter + caracter
      msg = enchimento.format('\n' + margem + ' ' + msg + '    ')
    else:
      grifo = '\n{:' + grifo_caracter + '<' + str(len(msg) + 1) + '}'
      grifo = grifo.format('')
      enchimento = '{:' + caracter + '<81}'
      margem = ''
      msg = enchimento.format('\n' + margem + msg)
    return msg + grifo


    # Inicialização da Árvore Default     ------------------------------------------------------------

  def gerar_arvore_default():

    print(cabecalho('Criando uma Árvore Binária Balanceada para Testes', '-'))
    arvore = ArvoreBinaria()

    # Inserção de Elementos


                            #                 RAIZ
    arvore.insere_noh(44)   #            _____ 44 _____
                            #           /              \
    arvore.insere_noh(26)   #         26                \
    arvore.insere_noh(76)   #        /  \               76
    arvore.insere_noh(18)   #       18   \             /  \
    arvore.insere_noh(33)   #      /  \  33           /    \
    arvore.insere_noh(12)   #     12   \             /      \
    arvore.insere_noh(21)   #          21           /        \
    arvore.insere_noh(64)   #                      64         \
    arvore.insere_noh(87)   #                     /  \         87
    arvore.insere_noh(53)   #                    53   \       /  \
    arvore.insere_noh(71)   #                   /  \  71     /    \
    arvore.insere_noh(49)   #                  49   \       /      \
    arvore.insere_noh(60)   #                       60     /        \
    arvore.insere_noh(83)   #                             83         \
    arvore.insere_noh(94)   #                                        94
                            #                                       /  \
    arvore.insere_noh(91)   #                                      91   \
    arvore.insere_noh(96)   #                                           96

    desenho = (
              '\n                 RAIZ                 ' +
              '\n            _____ 44 _____            ' +
              '\n           /              \           ' +
              '\n         26                76         ' +
              '\n        /  \              /  \        ' +
              '\n       /    \            /    \       ' +
              '\n     18     33         64      87     ' +
              '\n    /  \              /  \    /  \    ' +
              '\n   12  21           53   71  83   94  ' +
              '\n                   /  \          /  \ ' +
              '\n                  49  60        91  96'
              )
    print(desenho)
    print()
    arvore.imprimir_propriedades()
    noh_problema = arvore.get_noh_mais_profundo_desbalanceado()
    if noh_problema:
      print('\n>> Árvore desbalanceada no noh {}'.format(noh_problema))
    else:
      print('\n>> A árvore está balanceada.')

    return arvore


  # Escolha do Método de Balanceamento     ---------------------------------------------------------

  def escolher_metodo():

    escolha = None

    # Exibição das opções

    print(cabecalho_secao('Escolha do Método de Balanceamento'))
    print('{:-<80}'.format(''))
    print('  1 - Estático')
    print('  2 - Dinâmico-Estático')
    print('  3 - Dinâmico-Rotacional')
    print('  4 - Dinâmico Russo-AVL')
    print('  9 - Sair do programa')

    # Obtenção, via teclado, a escolha do usuário
    escolha = int(input('\nInforme a opção desejada: '))

    return escolha


  # Escolha do Tipo de Teste de Balanceamento    ---------------------------------------------------

  def escolher_acao():

    escolha = None;

    print(cabecalho('Escolha a Ação a Ser Executada'))


    # Exibição das opções de acordo com o método de balanceamento

    metodo_escolhido = escolhas['metodo']

    if metodo_escolhido == ESTATICO:
      print('  0 - Informações sobre o método')
      print('  1 - Inserir valor')
      print('  2 - Desenhar galhos')
      print('  3 - Checar balanceamento da árvore')
      print('  4 - Balancear árvore binária')
      print('  7 - Reiniciar árvore binária original')
      print('  8 - Voltar à escolha do método de balanceamento')
      print('  9 - Sair do programa')

    elif metodo_escolhido == DINAMICO_ESTATICO:
      print('  0 - Informações sobre o método')
      print('  1 - Inserir valor')
      print('  2 - Desenhar galhos')
      print('  3 - Checar balanceamento da árvore')
      print('  7 - Reiniciar árvore binária original')
      print('  8 - Voltar à escolha do método de balanceamento')
      print('  9 - Sair do programa')

    elif ( metodo_escolhido == DINAMICO_ROTACIONAL or
           metodo_escolhido == DINAMICO_RUSSO_AVL ):
      print('  0 - Informações sobre o método')
      print('  1 - Inserir valor')
      print('  2 - Desenhar galhos')
      print('  3 - Checar balanceamento da árvore')
      print('  7 - Reiniciar árvore binária original')
      print('  8 - Voltar à escolha do método de balanceamento')
      print('  9 - Sair do programa')


    # Obtenção, via teclado, da escolha do usuário
    escolha = int(input('\nInforme a opção desejada: '))

    return escolha


  def executar_acao(escolhas):

    metodo = escolhas['metodo']
    acao  = escolhas['acao']

    if metodo == ESTATICO:

      if   acao == EXIBIR_INFO:            exibir_informacoes()
      elif acao == INSERIR_VALOR:          inserir_valor()
      elif acao == DESENHAR_GALHOS:        desenhar_galhos()
      elif acao == REINICIAR_ARVORE:       recriar_arvore()
      elif acao == CHECAR_BALANCEAMENTO:   checar_balanceamento()
      elif acao == REALIZAR_BALANCEAMENTO: realizar_balanceamento_estatico()

    elif ( metodo == DINAMICO_ESTATICO   or
           metodo == DINAMICO_ROTACIONAL or
           metodo == DINAMICO_RUSSO_AVL ):

      if   acao == EXIBIR_INFO:            exibir_informacoes()
      elif acao == INSERIR_VALOR:          inserir_valor()
      elif acao == DESENHAR_GALHOS:        desenhar_galhos()
      elif acao == REINICIAR_ARVORE:       recriar_arvore()
      elif acao == CHECAR_BALANCEAMENTO:   checar_balanceamento()




  def exibir_informacoes():
    print( cabecalho(titulos[escolhas['metodo']]) )
    print()
    print(info_metodos[escolhas['metodo']])

  def inserir_valor():

    valor = int(input('\nInforme o valor a ser inserido na árvore: '))
    if valor >= 100:
      print("\n Valores com mais de dois digitos afetarão os desenhos exibidos "
            "na interface com o usuário. \n Por gentileza, digite valores abaixo de 100."
            )
      inserir_valor()
    else:
      metodo = escolhas['metodo']
      print('Inserindo noh', valor)

      if   metodo == ESTATICO:            arvore.insere_noh(valor, True)
      elif metodo == DINAMICO_ESTATICO:   arvore.insere_noh_dinamico_estatico(valor, True)
      elif metodo == DINAMICO_ROTACIONAL: arvore.insere_noh_dinamico_rotacional(valor, True)
      elif metodo == DINAMICO_RUSSO_AVL:  arvore.insere_noh_avl(valor, True)


  def desenhar_galhos():
    arvore.desenhar_todos_galhos()


  def checar_balanceamento():

    print( cabecalho('Balanceamento da Árvore') )
    noh_problema = arvore.get_noh_mais_profundo_desbalanceado(True)
    arvore.imprimir_propriedades()
    if noh_problema:
      print('\n>> Árvore desbalanceada no noh {}'.format(noh_problema))
    else:
      print('\n>> A árvore está balanceada.')


  def realizar_balanceamento_estatico():
    arvore.balanceamento_estatico(debug=True)


  def recriar_arvore():
    nonlocal arvore
    arvore = gerar_arvore_default()

    # nonlocal/global
    # https://pt.stackoverflow.com/questions/250362/qual-a-diferen%C3%A7a-de-global-e-nonlocal-no-python


  # ================================================================================================
  # Execução do Programa - Interação com o usuário     ---------------------------------------------

  # Inicializar árvore default para os testes
  arvore = gerar_arvore_default()


  while True:
    # Escolha do método de balanceamento a ser executado
    escolhas['metodo'] = escolher_metodo()

    if escolhas['metodo'] not in opcoes_menu_metodos_balanceamento:
      print('\nOpção INVÁLIDA.!  Tente novamente...\n')

    elif not escolhas['metodo'] == SAIR:

      # Todos os demais métodos, com exceção do balanceamento estático,
      # fazem o balanceamento já no momento que se insere o noh.
      # O usuário poderia inserir vários valores através do submenu do estático,
      # depois sair sem fazer o balanceamento e então entrar no AVL, por exemplo,
      # para balancear uma árvore contendo multiplos ramos desbalanceados.
      # Estariamos fora das condições de contorno em que o método AVL foi pensado.
      # O AVL tem por premissa uma árvore equilibrada quando insere-se um novo noh.
      # Portanto, devemos reiniciar a árvore de testes.
      #
      if not escolhas['metodo'] == ESTATICO:
        recriar_arvore()

      while True:
        print( cabecalho_secao(titulos[escolhas['metodo']]) )

        # Escolha da ação a ser executada
        escolhas['acao'] = escolher_acao()

        if escolhas['acao'] == MUDAR_METODO:
          print('\nOptou por voltar à escolha do método de balanceamento !')
          break

        elif escolhas['acao'] == SAIR:
          print('\nEscolheu SAIR !')
          # informar ao loop externo da intenção do usuário
          escolhas['metodo'] = SAIR
          break

        elif escolhas['acao'] not in opcoes_balanceamento[escolhas['metodo']]:
          print('\nOpção INVÁLIDA !  Tente novamente...\n')

        else:
          executar_acao(escolhas)


    # Se pediu pra sair no loop interno, obedeça e saia da execução do programa
    if escolhas['metodo'] == SAIR:
      break


# ==================================================================================================
# ==================================================================================================


  """


  # Testes  ----------------------------------------------------------------------------------------

  # Inicialização
  print(cabecalho('Criando uma Árvore Binária Balanceada ', '-'))
  arvore = ArvoreBinaria()

  # Inserção de Elementos


                          #                 RAIZ
  arvore.insere_noh(44)   #            _____ 44 _____
                          #           /              \
  arvore.insere_noh(26)   #         26                \
  arvore.insere_noh(76)   #        /  \               76
  arvore.insere_noh(18)   #       18   \             /  \
  arvore.insere_noh(33)   #      /  \  33           /    \
  arvore.insere_noh(12)   #     12   \             /      \
  arvore.insere_noh(21)   #          21           /        \
  arvore.insere_noh(64)   #                      64         \
  arvore.insere_noh(87)   #                     /  \         87
  arvore.insere_noh(53)   #                   53   \       /  \
  arvore.insere_noh(71)   #                   /  \  71     /    \
  arvore.insere_noh(49)   #                  49   \       /      \
  arvore.insere_noh(60)   #                       60     /        \
  arvore.insere_noh(83)   #                             83         \
  arvore.insere_noh(94)   #                                        94
                          #                                       /  \
  arvore.insere_noh(91)   #                                      91   \
  arvore.insere_noh(96)   #                                           96

  desenho = (
            '\n                 RAIZ                 ' +
            '\n            _____ 44 _____            ' +
            '\n           /              \           ' +
            '\n         26                76         ' +
            '\n        /  \              /  \        ' +
            '\n       /    \            /    \       ' +
            '\n     18     33         64      87     ' +
            '\n    /  \              /  \    /  \    ' +
            '\n   12  21           53   71  83   94  ' +
            '\n                   /  \          /  \ ' +
            '\n                  49  60        91  96'
            )
  print(desenho)
  print()

  print(cabecalho('Conferindo Balanceamento da Árvore'))
  print('Percurso Simétrico')
  arvore.percurso_simetrico()
  print( '\nTotal de elementos: {}'.format(arvore.get_quantidade_noh()) )
  print('Altura: {}'.format(arvore.get_altura()))
  noh_desequilibrado = arvore.get_noh_mais_profundo_desbalanceado()
  if noh_desequilibrado:
    print('\nÁrvore desbalanceada no noh {}'.format(noh_desequilibrado))
  else:
    print('\n\tA árvore está balanceada.')


  """

  # ------------------------------------------------------------------------------------------------


  """

  # ================================================================================================
  # BALANCEAMENTO ESTÁTICO    ----------------------------------------------------------------------
  #
  # Remove todos os galhos do objeto árvore (#clear()) e os reinsere em uma ordem ótima
  # na qual a árvore ficará balanceada.
  #


  print(cabecalho_secao('BALANCEAMENTO ESTÁTICO'))

  print('\n')
  print(cabecalho('Desbalanceando a Árvore'))
  noh = 92
  print('Inserindo noh', noh)
  arvore.insere_noh(noh, debug=True)
  arvore.percurso_simetrico()
  print('\n')
  print(cabecalho('Aplicando Balanceamento'))
  arvore.balanceamento_estatico(debug=True)

  """

  # ------------------------------------------------------------------------------------------------

  """

  # ================================================================================================
  # BALANCEAMENTO DINÂMICO-ESTÁTICO - Com Busca do Noh Desbalanceado    ----------------------------
  #
  # de - Teste de desbalanceamento noh_raiz - seria caso de rotação dupla esquerda
  # print('Inserindo noh 70')       # de
  # arvore.insere_noh(70)           # de
  # print('Inserindo noh 73')       # de
  # arvore.insere_noh(73)           # de
  #
  # Depois de inserido os anteriores, a inserção do noh 68
  # causará o desequilíbrio de rotação dupla esquerda
  # print('Inserindo noh 68')       # de
  # arvore.insere_noh(68)           # de

  print(cabecalho_secao('BALANCEAMENTO DINÂMICO-ESTÁTICO'))

  #print('\n\n{:=<80}'.format(''))
  #print('{:-^80}'.format('   BALANCEAMENTO DINÂMICO-ESTÁTICO    '))



  print(cabecalho('Inserindo Noh Para Desbalancear a Árvore'))

  noh = 9
  print('Inserindo noh', noh)
  arvore.insere_noh_dinamico_estatico(noh, True)

  print(cabecalho('Balanceamento da Árvore'))
  noh_desequilibrado = arvore.get_noh_mais_profundo_desbalanceado()
  if noh_desequilibrado:
    print('\nÁrvore desbalanceada no noh {}'.format(noh_desequilibrado))
  else:
    print('\n\tA árvore está balanceada.')

  """

  # ------------------------------------------------------------------------------------------------

  """

  # ================================================================================================
  # BALANCEAMENTO DINÂMICO-ROTACIONAL - Com Busca do Noh Desbalanceado   ---------------------------
  #
  # Rotações:
  #           SIMPLES_ESQUERDA
  #           SIMPLES_DIREITA
  #           DUPLA_DIREITA
  #
  # OBS.: falta uma


  print('\n\n{:=<80}'.format(''))
  print('{:-^80}'.format('   BALANCEAMENTO DINÂMICO-ROTACIONAL    '))

  print(cabecalho('Desbalanceando a Árvore',' '))

  #noh = 15    # simples-direita
  #noh = 50    # simples-direita
  #noh = 95    # simples-esquerda
  #noh = 62    # dupla-direita
  noh = 22    # dupla-direita

  print('Inserindo noh', noh)
  arvore.insere_noh_dinamico_rotacional(noh,True)


  print( cabecalho('Balanceamento da Árvore') )
  noh_problema = arvore.get_noh_mais_profundo_desbalanceado()
  if noh_problema:
    print('\nÁrvore desbalanceada no noh {}'.format(noh_problema))
  else:
      print('\n\tA árvore está balanceada.')


  """

  # ------------------------------------------------------------------------------------------------


  """

  # ================================================================================================
  # BALANCEAMENTO DINÂMICO-ROTACIONAL - Com Busca do Noh Desbalanceado   ---------------------------
  #
  # Rotação:  DUPLA_ESQUERDA
  #
  # OBS.: É preciso inserir outros noh's para poder testar esta rotação
  #

  print('\n\n{:=<80}'.format(''))
  print('{:-^80}'.format('   BALANCEAMENTO DINÂMICO-ROTACIONAL    '))

  print( cabecalho('Modificando a árvore para poder testar a rotação dupla-esquerda') )
  print('É preciso de um pai_direita com filho_esquerdo, quando nascer um netinho.')
  print('E nós não temos essa condição na nossa árvore de estudo.')
  print('\nInserindo noh 70')

  arvore.insere_noh_dinamico_rotacional(70)

  print( '\nBalanceamento da Árvore' )
  noh_problema = arvore.get_noh_mais_profundo_desbalanceado()
  if noh_problema:
    print('Árvore desbalanceada no noh {}'.format(noh_problema))
  else:
    print('A árvore está balanceada.')

  print('\nInserindo noh 73')

  arvore.insere_noh_dinamico_rotacional(73)

  print( cabecalho('Balanceamento da Árvore') )
  noh_problema = arvore.get_noh_mais_profundo_desbalanceado()
  if noh_problema:
    print('Árvore desbalanceada no noh {}'.format(noh_problema))
  else:
    print('A árvore está balanceada.')


  print( cabecalho('Árvore Após as Inserções') )
  arvore.desenhar_todos_galhos()

  # Desequilibrando....

  print( cabecalho('Desbalanceando a Árvore') )
  print('Inserindo noh 68')
  arvore.insere_noh_dinamico_rotacional(68, True)


  print( cabecalho('Balanceamento da Árvore') )
  noh_problema = arvore.get_noh_mais_profundo_desbalanceado()
  if noh_problema:
    print('\nÁrvore desbalanceada no noh {}'.format(noh_problema))
  else:
      print('\n\tA árvore está balanceada.')


  """

  # ------------------------------------------------------------------------------------------------

  """

  # ================================================================================================
  # BALANCEAMENTO DINÂMICO AVL  --------------------------------------------------------------------
  #
  # Rotações:
  #           SIMPLES_ESQUERDA
  #           SIMPLES_DIREITA
  #           DUPLA_DIREITA
  #
  # OBS.: falta uma
  #

  print('\n\n{:=<80}'.format(''))
  print('{:-^80}'.format('   BALANCEAMENTO DINÂMICO AVL    '))

  print( cabecalho('Desbalanceando a Árvore') )

  #noh = 15    # simples-direita
  #noh = 50    # simples-direita
  #noh = 95    # simples-esquerda
  noh = 63    # dupla-direita


  print('Inserindo noh {}'.format(noh))
  arvore.insere_noh_avl(noh, True)

  print( cabecalho('Balanceamento da Árvore') )
  noh_problema = arvore.get_noh_mais_profundo_desbalanceado()
  if noh_problema:
    print('\nÁrvore desbalanceada no noh {}'.format(noh_problema))
  else:
      print('\n\tA árvore está balanceada.')


  """

  # ------------------------------------------------------------------------------------------------

  """

  # ================================================================================================
  # BALANCEAMENTO DINÂMICO AVL  --------------------------------------------------------------------
  #
  # Rotação:  DUPLA_ESQUERDA
  #
  # OBS.: É preciso inserir outros noh's para poder testar esta rotação
  #


  print('\n\n{:=<80}'.format(''))
  print('{:-^80}'.format('   BALANCEAMENTO DINÂMICO AVL    '))

  print( cabecalho('Modificando a árvore para poder testar a rotação dupla-esquerda') )
  print('É preciso de um pai_direita com filho_esquerdo, quando nascer um netinho.')
  print('E nós não temos essa condição na nossa árvore de estudo.')
  print('\nInserindo noh 70')
  arvore.insere_noh_avl(70)
  print( '\nConferindo Balanceamento da Árvore' )
  noh_problema = arvore.get_noh_mais_profundo_desbalanceado()
  if noh_problema:
    print('Árvore desbalanceada no noh {}'.format(noh_problema))
  else:
    print('A árvore está balanceada.')

  print('\nInserindo noh 73')
  arvore.insere_noh_avl(73)
  print( '\nConferindo Balanceamento da Árvore' )
  noh_problema = arvore.get_noh_mais_profundo_desbalanceado()
  if noh_problema:
    print('Árvore desbalanceada no noh {}'.format(noh_problema))
  else:
    print('A árvore está balanceada.')

  print( cabecalho('Árvore Após as Inserções') )
  arvore.desenhar_todos_galhos()

  # Desequilibrando....

  print( cabecalho('Desbalanceando a Árvore') )
  arvore.insere_noh_avl(68, True)


  print( cabecalho('Balanceamento da Árvore') )
  noh_problema = arvore.get_noh_mais_profundo_desbalanceado()
  if noh_problema:
    print('\nÁrvore desbalanceada no noh {}'.format(noh_problema))
  else:
    print('\n\tA árvore está balanceada.')

"""


# Acionamento efetivo do programa principal
if __name__ == '__main__':
    main()


