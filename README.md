================================================================================

citizen assist ai - modulo de energia e sustentabilidade

================================================================================
--------------------------------------------------------------------------------

1. integrantes do grupo

--------------------------------------------------------------------------------

- Felipe Mello Ramalho - rm: 569237

- Gabriel Beu Volpato - rm: 563008

--------------------------------------------------------------------------------

2. contexto e publico-alvo

--------------------------------------------------------------------------------

- publico escolhido: condominios residenciais e pequenos comercios urbanos.

- necessidade energetica: alto custo mensal com eletricidade convencional 

  (iluminacao de areas comuns, elevadores, bombas, refrigeracao e equipamentos) 

  aliado a falta de orientacao tecnica sobre a viabilidade financeira e 

  ambiental da transicao para fontes renovaveis.

- contribuicao do assistente: o modulo integrado ao citizen assist ai traduz 

  dados tecnicos de consumo em recomendacoes praticas, comparando o cenario 

  atual com uma alternativa renovavel, detalhando economias estimadas, impacto 

  de carbono e limitacoes reais.



--------------------------------------------------------------------------------

3. funcionalidades de energia

--------------------------------------------------------------------------------

1) motor de calculo energetico (energy_analysis_engine):

   processa o consumo mensal (kwh), tarifa local (r$/kwh) e fator de emissao 

   da rede (kg co2/kwh).



2) comparativo de alternativas:

   contrasta o fornecimento 100% convencional da concessionaria com um sistema 

   hibrido (70% suprido por energia solar fotovoltaica com gestao de demanda).



3) integracao conversacional (citizen_assist_energy_integration):

   formata os resultados em linguagem acessivel, apresentando beneficios 

   economicos, reducao de emissoes, fontes de dados e avisos sobre limitacoes 

   das estimativas.



--------------------------------------------------------------------------------

4. dados utilizados, premissas e calculos

--------------------------------------------------------------------------------

os parametros padrao configurados no codigo baseiam-se em medias publicas do 

setor eletrico brasileiro:



- consumo de referencia (estimado): 1.200 kwh/mes (periodo de 30 dias), 

  representativo do consumo mensal tipico de areas comuns de um condominio 

  residencial de pequeno/medio porte ou de um pequeno comercio urbano.

- tarifa media convencional: r$ 0,85/kwh (baseado em tarifas residenciais e 

  comerciais medias da aneel, incluindo impostos).

- fator de emissao da rede: 0,084 kg co2/kwh (fator medio anual do sistema 

  interligado nacional - sin / mcti).

- premissa da alternativa renovavel: sistema solar fotovoltaico dimensionado 

  para abater 70% do consumo mensal da rede, mantendo os 30% restantes 

  conectados a concessionaria para suprimento noturno ou em dias nublados.



resumo da comparacao (base mensal):



* alternativa 1 - rede convencional (100% concessionaria):

  - consumo da rede: 1.200 kwh

  - custo mensal estimado: r$ 1.020,00

  - emissoes de carbono: 100,80 kg co2



* alternativa 2 - solar + gestao inteligente (70% solar / 30% rede):

  - consumo da rede: 360 kwh

  - custo mensal estimado: r$ 306,00

  - emissoes de carbono: 30,24 kg co2



* impacto / diferenca direta:

  - reducao no consumo da rede: -840 kwh (-70%)

  - economia financeira mensal: r$ 714,00

  - reducao de emissoes: 70,56 kg co2 evitados por mes



--------------------------------------------------------------------------------

5. justificativas e limitacoes

--------------------------------------------------------------------------------

- custos e viabilidade: a alternativa solar apresenta alta viabilidade a medio e 

  longo prazo devido a reducao imediata de 70% na fatura mensal, embora exija 

  investimento inicial (capex) de instalacao e area de telhado/cobertura 

  disponivel sem sombreamento.

- impactos ambientais: evita a emissao de aproximadamente 846,7 kg de co2 ao 

  ano, reduzindo a pressao sobre termeletricas em horarios de pico.

- limitacoes explicitas: as estimativas nao garantem retorno financeiro fixo, 

  pois dependem da irradiancia solar regional, inclinacao dos paineis, perdas 

  eletricas do inversor, variacoes tarifarias (bandeiras) e disponibilidade 

  fisica do imovel.



--------------------------------------------------------------------------------

6. testes com usuarios e ajustes realizados

--------------------------------------------------------------------------------

foram realizados testes de compreensao com 3 usuarios potenciais (sindico e 

comerciantes locais) para avaliar a clareza das respostas geradas pelo 

assistente:



- situacao testada 1: consulta sobre reducao de custos em um condominio com 

  consumo de 1.200 kwh/mes.

  * feedback: o usuario achou o termo "fator de emissao" pouco claro no 

    primeiro prototipo.

  * ajuste: a saida textual do assistente foi simplificada para exibir 

    diretamente o total de kg de co2 evitados no mes.



- situacao testada 2: duvida sobre a garantia do valor economizado em um 

  pequeno comercio.

  * feedback: o usuario questionou se a economia de r$ 714,00 era garantida em 

    todos os meses do ano.

  * ajuste: adicionada a secao explicita de "limitacoes e premissas" alertando 

    sobre variacoes climaticas sazonais e necessidade de vistoria tecnica.


--------------------------------------------------------------------------------

7. referencias utilizadas

--------------------------------------------------------------------------------

- aneel (agencia nacional de energia eletrica): ranking de tarifas e dados de 

  geracao distribuida.

- mcti (ministerio da ciencia, tecnologia e inovacao): fatores de emissao de 

  co2 pela geracao de energia eletrica no sistema interligado nacional (sin).

- epe (empresa de pesquisa energetica): anuario estatistico de energia eletrica 

  e parametros de eficiencia energetica.

================================================================================
