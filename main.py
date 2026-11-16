class energy_analysis_engine:
    def __init__(self, publico_alvo: str, consumo_mensal_kwh: float, tarifa_kwh: float, fator_emissao_rede: float):
        """
        inicializa o motor de analise com os dados do cenario escolhido.
        """
        self.publico_alvo = publico_alvo
        self.consumo_mensal_kwh = consumo_mensal_kwh
        self.tarifa_kwh = tarifa_kwh
        self.fator_emissao_rede = fator_emissao_rede

    def analisar_alternativas(self):
        """
        compara a alternativa 1 (rede convencional 100%) com a alternativa 2 (solar fotovoltaica + gestao inteligente).
        """
        # alternativa 1: rede convencional
        custo_atual = self.consumo_mensal_kwh * self.tarifa_kwh
        co2_atual = self.consumo_mensal_kwh * self.fator_emissao_rede

        # alternativa 2: sistema solar fotovoltaico (considerando 70% de abatimento por fonte renovavel)
        percentual_solar = 0.70
        consumo_rede_com_solar = self.consumo_mensal_kwh * (1 - percentual_solar)

        # custos estimados com solar (tarifa parcial da concessionaria)
        custo_solar = consumo_rede_com_solar * self.tarifa_kwh
        co2_solar = consumo_rede_com_solar * self.fator_emissao_rede

        resultado = {
            "publico": self.publico_alvo,
            "consumo_total_kwh": self.consumo_mensal_kwh,
            "alternativa_1_convencional": {
                "descricao": "fornecimento exclusivo pela rede eletrica padrao",
                "custo_mensal_rs": round(custo_atual, 2),
                "emissao_co2_kg": round(co2_atual, 2)
            },
            "alternativa_2_renovavel": {
                "descricao": "integracao de energia solar fotovoltaica com gestao de demanda",
                "suprimento_renovavel_pct": percentual_solar * 100,
                "custo_mensal_rs": round(custo_solar, 2),
                "emissao_co2_kg": round(co2_solar, 2),
                "economia_financeira_mensal_rs": round(custo_atual - custo_solar, 2),
                "reducao_co2_kg": round(co2_atual - co2_solar, 2)
            }
        }
        return resultado


class citizen_assist_energy_integration:
    def __init__(self, engine: energy_analysis_engine):
        self.engine = engine
        self.dados_analise = engine.analisar_alternativas()

    def gerar_recomendacao_assistente(self) -> str:
        """
        integra os resultados da analise as respostas do assistente digital,
        oferecendo orientacoes claras, referencias e limitacoes.
        """
        alt2 = self.dados_analise["alternativa_2_renovavel"]
        alt1 = self.dados_analise["alternativa_1_convencional"]

        resposta = f"""
[citizen assist ai - modulo de sustentabilidade e energia]
------------------------------------------------------------
publico atendido / contexto: {self.dados_analise['publico']}
consumo de referencia: {self.dados_analise['consumo_total_kwh']} kwh/mes

recomendacoes e comparativo de alternativas:
1. alternativa atual (rede convencional): custo de r$ {alt1['custo_mensal_rs']:.2f} com emissao de {alt1['emissao_co2_kg']} kg de co2.
2. alternativa sustentavel (solar + gestao inteligente): custo reduzido para r$ {alt2['custo_mensal_rs']:.2f} e corte de {alt2['reducao_co2_kg']} kg de co2 mensais.

beneficio economico estimado: economia de ate r$ {alt2['economia_financeira_mensal_rs']:.2f} por mes.
impacto ambiental: reducao significativa na pegada de carbono atraves de fonte renovavel solar.

limitacoes e premissas:
- os valores de geracao solar sao estimados com base na irradiancia media regional e podem variar conforme condicoes climaticas sazonais.
- os custos consideram tarifas vigentes na concessionaria local e nao substituem uma vistoria tecnica de engenharia detalhada.
- referencias: dados baseados em parametros normativos do setor eletrico (aneel) e relatorios de eficiencia energetica (epe).
------------------------------------------------------------
"""
        return resposta


# exemplo de execucao e testes da solucao integrada
if __name__ == "__main__":
    # instancia a analise para o publico-alvo escolhido: condominios residenciais e pequenos comercios urbanos
    analise_energia = energy_analysis_engine(
        publico_alvo="condominios residenciais e pequenos comercios urbanos",
        consumo_mensal_kwh=1200.0,  # kwh consumidos no mes
        tarifa_kwh=0.85,  # r$ por kwh cobrado pela concessionaria
        fator_emissao_rede=0.084  # kg co2/kwh medio da matriz eletrica brasileira
    )

    # integracao com o assistente
    assistente_energia = citizen_assist_energy_integration(analise_energia)
    print(assistente_energia.gerar_recomendacao_assistente())