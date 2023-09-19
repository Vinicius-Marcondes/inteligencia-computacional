import random
from dataclasses import dataclass

NUMERO_GERACAO = 100
TAMANHO_POPULACAO = 50
TAMANHO_CROMOSSOMO = 8
TAXA_MUTACAO = 0.1


@dataclass
class Cromossomo:
    def __init__(self, genes: list[int]):
        self.genes = genes


populacao: list[Cromossomo] = []


def inicializacao_populacao() -> None:
    for _ in range(TAMANHO_POPULACAO):
        cromossomo: Cromossomo = Cromossomo([random.randint(0, 1) for _ in range(TAMANHO_CROMOSSOMO)])
        populacao.append(cromossomo)


def fitness(cromossomo):
    return sum(cromossomo)


def roleta_viciada(populacao: list[int], aptidoes: list[int]) -> list[int]:
    total_aptidao: int = sum(aptidoes)
    probabilidades_selecao: list[float] = [aptidao / total_aptidao for aptidao in aptidoes]
    pais_selecionados: list[int] = []
    for _ in range(len(populacao)):
        indice_pai = random.choices(range(len(populacao)), weights=probabilidades_selecao)
        pai = populacao[indice_pai[0]]
        pais_selecionados.append(pai)
    return pais_selecionados


if __name__ == '__main__':
    # Loop principal do algoritmo genético
    for geracao in range(NUMERO_GERACAO):
        # Avaliar a aptidão de cada cromossomo na população
        aptidoes = [fitness(cromossomo) for cromossomo in populacao]

        # Selecionar os melhores indivíduos para reprodução com roleta viciada
        pais_selecionados = roleta_viciada(populacao, aptidoes)

        # Realizar o cruzamento (corte em dois pontos)
        proxima_geracao = []
        for i in range(0, len(pais_selecionados), 2):
            pai1 = pais_selecionados[i]
            pai2 = pais_selecionados[i + 1]
            ponto_corte1 = random.randint(1, TAMANHO_CROMOSSOMO - 1)
            ponto_corte2 = random.randint(ponto_corte1, TAMANHO_CROMOSSOMO)
            filho1 = pai1[:ponto_corte1] + pai2[ponto_corte1:ponto_corte2] + pai1[ponto_corte2:]
            filho2 = pai2[:ponto_corte1] + pai1[ponto_corte1:ponto_corte2] + pai2[ponto_corte2:]
            proxima_geracao.extend([filho1, filho2])

        # Aplicar mutação
        for i in range(TAMANHO_CROMOSSOMO):
            if random.random() < TAXA_MUTACAO:
                indice_mutacao = random.randint(0, TAMANHO_CROMOSSOMO - 1)
                populacao[i][indice_mutacao] = 1 - populacao[i][indice_mutacao]

        # Substituir a população atual pela próxima geração
        populacao = proxima_geracao

    # Encontrar o melhor cromossomo na última geração
    melhor_cromossomo = max(populacao, key=fitness())
    melhor_aptidao = fitness(melhor_cromossomo)

    print("Melhor cromossomo:", melhor_cromossomo)
    print("Melhor aptidão:", melhor_aptidao)
