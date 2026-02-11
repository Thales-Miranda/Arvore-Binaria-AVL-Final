# Árvore Binaria de Busca Balanceada (AVL)

Projeto de estruturação e criação de uma árvore binária de busca devidamente balanceada em resposta ao trabalho solicitado na disciplina de estrutura de dados 2 na faculdade de computação-UFU.

## Introdução - Como Foi resolvido o problema?

O problema foi resolvido utilizando linguagem Python. O desenvolvimento do índice remissivo foi estrurado para processar um arquivo de texto longo listando todas as palavras encontradas em ordem alfabética assim como uma lista para cada palavra contendo todas as linhas em que essa palavra aparece durante o texto.

Uma AVL é considerado um tipo especial de grafo que permite que um extenso volume de dados seja devidamente armazenado de forma eficiente de acordo com a lógica de alocação por um novo nó à esquerda (caso o valor seja menor que o no anterior e esse atual esteja vazio) e à direita (caso o valor seja maior que o anterior e esse atual esteja vazio). O fator de balanceamento garante que a árvore esteja devidamente equilibrada ao calcular a diferença de altura do no à esquerda pela altura do no à direita para cada nó, considera-se aceitável para o fator de balanceamento <= |2|. Uma árvore perfeitamente balanceada, todos os nós possuem o fator de balanceamento = 0. Caso o limite de |2| são realizadas rotações (simples ou duplas) para reestruturar o equilíbrio garantindo performace de alta velocidade e precisão para consultas, busca, inserção e remoção.  

## Desenvolvimento dos Arquivos Principais

A solução se encontra em uma estrutura de dados da Árvore Binária de Busca Balanceada (AVL). O projeto foi dividido em pontos chaves (módulos principais). No arquivo no.py, há o código de construção da classe nó, possuindo informação como a palavra (info) a ser armazenada, altura, ponteiros de esquerda (filho à esquerda) e direita (filho à direita) assim como a função de frequência da palavra que é obtido ao percorrer a lista de linhas que essa palavra aparece. No arquivo avl.py encontra-se toda as funções para inicialização da árvore assim como funções de inserção, busca e remoção, todas devidamente corrigidas a cada alteração pelas rotações necessárias ao calcular o fator de balanceamento com informação da altura, encontra-se tmabém todas as funcionalidades relacionadas à estrutura da árvore e requisitos solicitados no enunciado. O arquivo main.py encontra-se o código de coordenação e execução do programa, realizando a leitura de arquivo texto_origem, processando e filtrando os dados para identificação das palavras e linhas, desconsiderando pontuações e letras maiúsculas e minúsculas, ele utiliza do arquivo avl.py, no.py para processar o texto e gerar as estaísticas finais além do arquivo índice remissivo contendo todas as palavras do texto e suas respectivas listas. 

A ordenação alfabética entrega a extração de todos os dados ao percorrer a árvore sem que seja necessário uma ordenação prévia, os dados já vem ordenados por se tratar de um percurso de inorder traversal. Uma estrutura como a AVL permite eficiência de busca de alta velociade ao bidirecionar utilizando a lógica de comparação <> (maior ou menor) fazendo com que o pior caso seja o caminho de percorrer a altura da árvore, garantindo assim o desempenho O(log n) e custo mínimo.

Além disso, a utilização de uma Árvore AVL assegura que as operações fundamentais — inserção, busca e eventual remoção — mantenham complexidade assintótica O(log n), mesmo no pior caso, devido ao mecanismo de balanceamento automático por meio de rotações simples e duplas (LL, RR, LR e RL). O controle da altura dos nós e o cálculo do fator de balanceamento garantem que a diferença entre as subárvores esquerda e direita permaneça dentro do limite estrutural permitido (|FB| ≤ 1), evitando degradação para uma estrutura linear. Dessa forma, a solução apresenta não apenas organização ordenada dos dados, mas também eficiência computacional adequada para o processamento de grandes volumes de dados.


# Documentação do Código

## no.py

Responsável por definir a classe No, que representa cada elemento da árvore.

Atributos:

info: palavra armazenada.
linhas: lista de linhas onde a palavra aparece.
altura: altura do nó na árvore.
esq e dir: ponteiros para filhos esquerdo e direito.

Métodos:

frequencia(): retorna o número de linhas associadas à palavra.

## avl.py

Implementa a estrutura AVL e suas operações principais.

Principais métodos:

insere(valor, linha)
Insere uma palavra na árvore.
Atualiza altura.
Verifica fator de balanceamento.
Executa rotações quando necessário.

busca(valor)
Retorna o nó correspondente à palavra.

busca_prefixo(prefixo)
Retorna lista de palavras que iniciam com o prefixo informado.

remove(valor, linha=None)
Remove uma palavra inteira ou apenas uma linha específica.
Realiza rebalanceamento após remoção.

emOrdem()
Retorna as palavras em ordem alfabética.

palavra_mais_frequente()
Percorre a árvore e identifica o termo com maior frequência.

medidor_equilibrio(palavra)
Calcula a diferença entre o número de nós da subárvore esquerda e direita.

Observação: 

A árvore mantém-se balanceada utilizando o fator de balanceamento:
FB = altura(esquerda) − altura(direita)
Valores aceitáveis: -1, 0 ou 1.
Quando |FB| ≥ 2, rotações são aplicadas.

## main.py

Processar o arquivo texto_origem.txt.
Construir a árvore AVL.

Controlar estatísticas como:
Total de palavras processadas.
Total de palavras distintas.
Palavras descartadas por repetição.
Executar testes e medições de desempenho.
Gerar a saída do índice remissivo.



## Exemplo de uso

from avl import AVL

Criação da árvore
arvore = AVL()

Inserindo palavras com número da linha
arvore.insere("coracao", 1)
arvore.insere("delator", 1)
arvore.insere("coracao", 3)  # mesma palavra em outra linha

Buscando uma palavra
no = arvore.busca("coracao")

if no:
    print("Palavra encontrada!")
    print("Linhas:", no.linhas)
    print("Frequência:", no.frequencia())
else:
    print("Palavra não encontrada.")





Processamento de Arquivo

from main import processar_arquivo
avl, total, distintas, descartadas = processar_arquivo("texto_origem.txt")
print("Total de palavras:", total)
print("Palavras distintas:", distintas)
print("Descartadas:", descartadas)



Busca de Palavra

no = avl.busca("coração")
if no:
    print("Linhas:", no.linhas)
Saída esperada:
Linhas: [1, 120, 240]



Impressão em Ordem Alfabética

indice = avl.emOrdem()
for palavra, linhas in indice:
    print(palavra, "->", linhas)



Palavra Mais Frequente

palavra, freq = avl.palavra_mais_frequente()
print(f"{palavra} aparece em {freq} linhas.")
