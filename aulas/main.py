import random


class Cromossomo:
    dados: list[int] = []
    fitness: int = 0


class Config:
    tamanho_populacao = 50
    geracoes = 100

    max_iteracoes = 1000
    max_congelamento = 10;
    taxa_mutacao = 0.1
    tamanho_cromossomo = 8

    def fitness(self, cromossomo: Cromossomo) -> int:
        return sum(cromossomo.dados)


c = Config()

# Inicialização da população
populacao = []
for _ in range(c.tamanho_populacao):
    cromossomo = [random.randint(0, 1) for _ in range(c.tamanho_cromossomo)]
    populacao.append(cromossomo)

# Loop principal do algoritmo genético
for geracao in range(c.geracoes):
    # Avaliar a aptidão de cada cromossomo na população
    aptidoes = [funcao_aptidao(cromossomo) for cromossomo in populacao]

    # Selecionar os melhores indivíduos para reprodução
    pais_selecionados = []
    for _ in range(c.tamanho_populacao // 2):
        indice_pai1 = random.choices(range(c.tamanho_populacao), weights=aptidoes)
        indice_pai2 = random.choices(range(c.tamanho_populacao), weights=aptidoes)
        pai1 = populacao[indice_pai1[0]]
        pai2 = populacao[indice_pai2[0]]
        pais_selecionados.extend([pai1, pai2])

    # Realizar o cruzamento (corte em dois pontos)
    proxima_geracao = []
    for i in range(0, len(pais_selecionados), 2):
        pai1 = pais_selecionados[i]
        pai2 = pais_selecionados[i + 1]
        ponto_corte1 = random.randint(1, c.tamanho_cromossomo - 1)
        ponto_corte2 = random.randint(ponto_corte1, c.tamanho_cromossomo)
        filho1 = pai1[:ponto_corte1] + pai2[ponto_corte1:ponto_corte2] + pai1[ponto_corte2:]
        filho2 = pai2[:ponto_corte1] + pai1[ponto_corte1:ponto_corte2] + pai2[ponto_corte2:]
        proxima_geracao.extend([filho1, filho2])

    # Aplicar mutação
    for i in range(c.tamanho_populacao):
        if random.random() < c.taxa_mutacao:
            indice_mutacao = random.randint(0, c.tamanho_cromossomo - 1)
            populacao[i][indice_mutacao] = 1 - populacao[i][indice_mutacao]

    # Substituir a população atual pela próxima geração
    populacao = proxima_geracao

# Encontrar o melhor cromossomo na última geração
melhor_cromossomo = max(populacao, key=funcao_aptidao)
melhor_aptidao = funcao_aptidao(melhor_cromossomo)

print("Melhor cromossomo:", melhor_cromossomo)
print("Melhor aptidão:", melhor_aptidao)
