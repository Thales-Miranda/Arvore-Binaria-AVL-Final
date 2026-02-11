

from no import No

class AVL:





    def __init__(self):
        self.__raiz = None     #Raiz da árvore - Inicialização
        self.rotacoes = 0      #Contador de rotações realizadas

    def __altura(self, no):

        return no.altura if no else 0

    def __maior(self, a, b):
       
        return a if a > b else b
    
    def __fatorBalanceamento(self, no):

        return self.__altura(no.esq) - self.__altura(no.dir)
    




    #ROTAÇÕES

    def __RotacaoLL(self, A):
        B = A.esq
        A.esq = B.dir
        B.dir = A
        # Atualiza alturas
        A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.esq), A.altura) + 1
        self.rotacoes += 1
        return B
    
    def __RotacaoRR(self, A):
        B = A.dir
        A.dir = B.esq
        B.esq = A
        # Atualiza alturas
        A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.dir), A.altura) + 1
        self.rotacoes += 1
        return B

    def __RotacaoLR(self, A):
        A.esq = self.__RotacaoRR(A.esq)
        return self.__RotacaoLL(A)

    def __RotacaoRL(self, A):
        A.dir = self.__RotacaoLL(A.dir)
        return self.__RotacaoRR(A)
    




    #INSERÇÃO

    def __insereValor(self, atual, valor, linha):

        """
        Função recursiva para inserir uma palavra e a linha correspondente.
        - Se palavra já existe, adiciona a linha na lista se ainda não estiver presente
        - Balanceia a árvore automaticamente utilizando fator de balanceamento e rotações
        """

        if not atual:
            return No(valor, linha)  #Cria novo nó caso não exista a raiz

        if valor < atual.info:
            atual.esq = self.__insereValor(atual.esq, valor, linha)
            if self.__fatorBalanceamento(atual) >= 2:
                if valor < atual.esq.info:
                    atual = self.__RotacaoLL(atual)
                else:
                    atual = self.__RotacaoLR(atual)

        elif valor > atual.info:
            atual.dir = self.__insereValor(atual.dir, valor, linha)
            if self.__fatorBalanceamento(atual) <= -2:
                if valor > atual.dir.info:
                    atual = self.__RotacaoRR(atual)
                else:
                    atual = self.__RotacaoRL(atual)

        else:

            #Palavra já existe, adiciona linha na lista de linhas se não duplicada.
            if linha not in atual.linhas:
                atual.linhas.append(linha)

        #Atualiza altura do nó
        atual.altura = self.__maior(self.__altura(atual.esq), self.__altura(atual.dir)) + 1
        return atual

    def insere(self, valor, linha):

        """
        Função pública para inserir palavra e linha.
        Converte palavra para minúsculas (ignora maiúsculas/minúsculas)
        """
        self.__raiz = self.__insereValor(self.__raiz, valor.lower(), linha)





    #BUSCAS

    def busca(self, valor):

        atual = self.__raiz
        valor = valor.lower()
        while atual:
            if valor == atual.info:
                return atual
            elif valor > atual.info:
                atual = atual.dir
            else:
                atual = atual.esq
        return None
    
    def busca_prefixo(self, prefixo):

        resultado = []
        prefixo = prefixo.lower()
        def percorrer(no):
            if no:
                percorrer(no.esq)
                if no.info.startswith(prefixo):
                    resultado.append(no.info)
                percorrer(no.dir)
        percorrer(self.__raiz)
        return resultado

    def medidor_equilibrio(self, palavra):

        """
        Calcula o Medidor de Equilíbrio (ME) de uma palavra:
        ME = quantidade de nós na subárvore esquerda - quantidade na direita
        Retorna:
        -1 se palavra não existe
         0 se ME == 0
         1 se ME != 0 (imprime valor)
        """
        no = self.busca(palavra)
        if not no:
            return -1
        esq = self.__contar_nos(no.esq)
        dir = self.__contar_nos(no.dir)
        me = esq - dir
        if me == 0:
            return 0
        else:
            print(f"ME de '{palavra}': {me}")
            return 1

    def __contar_nos(self, no):

        if not no:
            return 0
        return 1 + self.__contar_nos(no.esq) + self.__contar_nos(no.dir)
    




    #REMOÇÃO

    def __procuraMenor(self, atual):
        while atual.esq:
            atual = atual.esq
        return atual

    def __removeValor(self, atual, valor, linha=None):

        """
        Remove palavra ou linha específica de um nó.
        - Se linha é fornecida, remove somente ela
        - Se não houver linhas restantes, remove o nó
        """
        if not atual:
            return None

        if valor < atual.info:
            atual.esq = self.__removeValor(atual.esq, valor, linha)

        elif valor > atual.info:
            atual.dir = self.__removeValor(atual.dir, valor, linha)

        else:
            # Palavra encontrada
            if linha and linha in atual.linhas:
                atual.linhas.remove(linha)
            if not atual.linhas or linha is None:
                if not atual.esq:
                    return atual.dir
                elif not atual.dir:
                    return atual.esq
                temp = self.__procuraMenor(atual.dir)
                atual.info = temp.info
                atual.linhas = temp.linhas
                atual.dir = self.__removeValor(atual.dir, temp.info)

        # Atualiza altura e balanceia
        atual.altura = self.__maior(self.__altura(atual.esq), self.__altura(atual.dir)) + 1
        fb = self.__fatorBalanceamento(atual)
        if fb >= 2:
            if self.__altura(atual.esq.esq) >= self.__altura(atual.esq.dir):
                return self.__RotacaoLL(atual)
            else:
                return self.__RotacaoLR(atual)
        if fb <= -2:
            if self.__altura(atual.dir.dir) >= self.__altura(atual.dir.esq):
                return self.__RotacaoRR(atual)
            else:
                return self.__RotacaoRL(atual)
        return atual

    def remove(self, valor, linha=None):
        self.__raiz = self.__removeValor(self.__raiz, valor.lower(), linha)
        




    #EM ORDEM

    def __emOrdem(self, no, resultado):

        if no:
            self.__emOrdem(no.esq, resultado)
            resultado.append((no.info, no.linhas))
            self.__emOrdem(no.dir, resultado)

    def emOrdem(self):

        resultado = []
        self.__emOrdem(self.__raiz, resultado)
        return resultado
    



    
    #PALAVRA MAIS FREQUENTE

    def palavra_mais_frequente(self):

        max_freq = 0
        palavra_max = ""
        def percorrer(no):
            nonlocal max_freq, palavra_max
            if no:
                percorrer(no.esq)
                if len(no.linhas) > max_freq:
                    max_freq = len(no.linhas)
                    palavra_max = no.info
                percorrer(no.dir)
        percorrer(self.__raiz)
        return palavra_max, max_freq
