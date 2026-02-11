

# ArvoreBinariaAVL
Projeto de estruturação e criação de uma árvore binária de busca devidamente balanceada em resposta ao trabalho solicitado na disciplina de estrutura de dados 2 na faculdade de computação UFU.

## Introdução - Como Foi resolvido o problema?

O problema foi resolvido utilizando linguagem Python. O desenvolvimento do índice remissivo foi estrurado para processar um arquivo de texto longo listando todas as palavras encontradas em ordem alfabética assim como uma lista para cada palavra contendo todas as linhas em que essa palavra aparece durante o texto.

A solução se encontra em uma estrutura de dados da Árvore Binária de Busca Balanceada (AVL). O projeto foi dividido em pontos chaves, iniciando com no.py, há o código de construção da classe nó, possuindo informação como a palavra (info) a ser armazenada, altura, ponteiros de esquerda e direita assim como a função de frequência da palavra que é obtido ao percorrer a lista de linhas que essa palavra aparece. No arquivo avl.py encontra-se toda as funções para inicialização da árvore assim como funções de inserção, busca e remoção, todas devidamente corrigidas a cada alteração pelas rotações necessárias ao calcular o fator de balanceamento com informação da altura. 

Uma AVL é considerado um tipo especial de grafo que permite que um extenso volume de dados seja devidamente armazenado de forma eficiente de acordo com a lógica de alocação por um novo nó à esquerda (caso o valor seja menor que o no anterior e esse atual esteja vazio) e à direita (caso o valor seja maior que o anterior e esse atual esteja vazio). O fator de balanceamento garante que a árvore esteja devidamente equilibrada ao calcular a diferença de altura do no à esquerda pela altura do no à direita, considera-se aceitável para o fator de balanceamento <= |2|. 

A ordenação alfabética entrega a extração de todos os dados ao percorrer a árvore sem que seja necessário uma ordenação prévia. Uma estrutura como a AVL permite eficiência de busca de alta velociade ao bidirecionar utilizando a lógica <> fazendo com que o pior caso seja o caminho de percorrer a altura da árvore.


## Exemplo de uso



```python
from avl import AVL

arvore = new AVL();

# Aqui inserimos o numero 10 na arvore.

# Ele irá fazer X Y Z, buscanod tal, fazendo tal
arvore.inserir("sol");
arvore.buscar("sol")

```

Aqui o programa utiliza-se da classe ABC
```python
from avl import AVL

arvore = new AVL();

# Aqui inserimos o numero 10 na arvore.

# Ele irá fazer X Y Z, buscanod tal, fazendo tal
arvore.inserir("nuvem");
arvore.buscar("nuvem")

```

```python
from avl import AVL

arvore = new AVL();

# Aqui inserimos o numero 10 na arvore.

# Ele irá fazer X Y Z, buscanod tal, fazendo tal
arvore.inserir(10);
arvore.buscar(10)

```