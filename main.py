

import time
import re
from avl import AVL



def processar_arquivo (texto_origem):

    """
    Processa arquivo de texto e insere cada palavra na árvore AVL.
    Retorna:
    - árvore AVL
    - total de palavras processadas
    - total de palavras distintas
    - total de palavras descartadas por repetição
    """



    avl = AVL()
    total_palavras = 0
    palavras_distintas = 0
    palavras_descartadas = 0



    with open(texto_origem, 'r', encoding='utf-8') as f:

        for linha_num, linha in enumerate(f, start=1):



            # Remove pontuação e separa palavras

            palavras = re.findall(r'\b\w+\b', linha.lower())
            for palavra in palavras:
                no = avl.busca(palavra)
                total_palavras += 1
                if no:
                    if linha_num in no.linhas:
                        palavras_descartadas += 1
                else:
                    palavras_distintas += 1
                avl.insere(palavra, linha_num)
    return avl, total_palavras, palavras_distintas, palavras_descartadas



def salvar_indice(avl, nome_arquivo_saida, total_palavras, palavras_distintas, palavras_descartadas, tempo):

    """
    Salva o índice remissivo completo em arquivo texto.
    """

    with open(nome_arquivo_saida, 'w', encoding='utf-8') as f:
        for palavra, linhas in avl.emOrdem():
            linhas_str = ','.join(map(str, linhas))
            f.write(f"{palavra} {linhas_str}\n")
        f.write("\n")
        f.write(f"Número total de palavras: {total_palavras}\n")
        f.write(f"Número de palavras distintas: {palavras_distintas}\n")
        f.write(f"Total de palavras descartadas: {palavras_descartadas}\n")
        f.write(f"Total de rotações executadas: {avl.rotacoes}\n")
        f.write(f"Tempo de construção do índice usando árvore AVL: {tempo:.3f}s\n")

if __name__ == "__main__":
    inicio = time.time()
    avl, total, distintas, descartadas = processar_arquivo("texto_origem.txt")
    fim = time.time()
    tempo_execucao = fim - inicio



    salvar_indice(avl, "indice_remissivo.txt", total, distintas, descartadas, tempo_execucao)

    # Exibe palavra mais frequente

    palavra_freq, freq = avl.palavra_mais_frequente()
    print(f"Palavra mais frequente: '{palavra_freq}' ({freq} linhas)")
    print(f"Rotacoes executadas: {avl.rotacoes}")





    #Teste do Medidor de Equilíbrio

    palavra_teste = input("Digite uma palavra para calcular o Medidor de Equilíbrio (ME): ")

    resultado_me = avl.medidor_equilibrio(palavra_teste)

    if resultado_me == -1:
        print("Palavra não encontrada na árvore.")
    elif resultado_me == 0:
        print("Palavra encontrada. O nó está perfeitamente equilibrado (ME = 0).")
    else:
        print("Palavra encontrada. O nó apresenta desequilíbrio.")




