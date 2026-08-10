# Arquitetura da futura skill de roteiros para Reels

## 1. Proposta da skill

**Nome de trabalho:** `roteirista-reels`.

**Resultado que ela entrega:** transformar conhecimento real do usuário em um roteiro de Reel gravável, com tema útil, ângulo escolhido, abertura adequada ao objetivo, falas, texto na tela, apoio visual simples e CTA coerente.

Ela não será uma geradora de textos genéricos. Será uma condutora de decisão: ajuda a escolher **sobre o que vale a pena falar**, por que vale para aquela audiência e como transformar isso em um vídeo curto.

## 2. Problema que resolve

Quem está começando costuma travar em quatro pontos:

1. não sabe qual tema escolher;
2. escolhe um tema amplo demais ou sem utilidade prática;
3. tenta escrever um gancho antes de saber o objetivo e a entrega;
4. recebe um roteiro longo, confuso e difícil de gravar.

A skill resolve nessa ordem: `pessoa -> público -> objetivo -> tema -> ângulo -> gancho -> estrutura -> roteiro -> aprendizado pós-publicação`.

## 3. Experiência de uso: TDAH-first

A habilidade deve reduzir decisões simultâneas, não produzir uma aula longa.

### Regras de interação

- Conduzir **uma decisão por vez** e mostrar `Etapa 1 de 6`.
- Fazer uma pergunta curta; quando útil, sugerir até três caminhos, com um recomendado e o motivo.
- Mostrar um resumo de uma linha ao concluir cada etapa: `Definido: objetivo = salvamentos`.
- Nunca gerar mais de três temas, três ângulos ou três ganchos por rodada sem o usuário pedir.
- Permitir comandos naturais: `pular`, `voltar`, `simplificar`, `me dê exemplos`, `decida comigo` e `salvar para depois`.
- Repetir o contexto que já foi confirmado; não obrigar a pessoa a lembrar decisões anteriores.
- Encerrar cada interação com **um próximo passo concreto**, não com uma lista de possibilidades.

### Regra de formato

Por padrão, responder com:

1. decisão atual;
2. por que ela importa em uma frase;
3. uma única pergunta ou ação seguinte.

Detalhes, variações e explicações só aparecem quando o usuário pedir ou quando forem indispensáveis para não criar uma promessa enganosa.

## 4. Modos de trabalho

| Modo | Quando usar | Saída |
|---|---|---|
| `começar meu perfil` | Usuário ainda não tem contexto de criação organizado | Mapa pessoal mínimo: conhecimento, público, objetivo, disponibilidade e limites. |
| `encontrar temas` | Usuário não sabe o que postar | Três temas pontuados, cada um com utilidade e ângulo sugerido. |
| `explorar um tema` | Já existe tema, mas falta profundidade | Seis ângulos e recomendação do mais útil ao objetivo. |
| `criar roteiro` | Tema e objetivo estão claros | Roteiro gravável com fala, visual e CTA. |
| `melhorar rascunho` | Usuário tem uma ideia ou texto | Diagnóstico curto e versão mais clara, preservando a voz. |
| `analisar referência` | Usuário fornece Reel, perfil ou transcrição | Mapa de mecanismo reutilizável, sem copiar fala ou história. |
| `aprender com publicação` | Usuário traz métricas e comentários | Hipótese do que funcionou e um único teste para o próximo Reel. |

## 5. Fluxo principal

### Etapa 0 — Recuperar ou montar o mapa do criador

Perguntar somente o que falta, nesta ordem:

1. `Qual conhecimento ou experiência você realmente consegue demonstrar?`
2. `Quem você quer ajudar primeiro?`
3. `O que esse perfil precisa gerar agora: alcance, confiança, salvamentos, conversa ou clientes?`
4. `Quanto tempo e qual formato você consegue manter?`

Salvar em uma ficha de contexto. A skill não deve inventar nicho, oferta, resultado ou autoridade.

### Etapa 1 — Escolher ou validar o tema

Um tema passa se atender a quatro critérios:

| Critério | Pergunta |
|---|---|
| Relevância | Essa pessoa reconhece o problema, desejo ou decisão? |
| Utilidade | Ela sai com uma ação, critério, checklist, comparação ou template? |
| Verdade/prova | O criador consegue demonstrar, explicar ou citar fonte confiável? |
| Adequação ao objetivo | Esse tema favorece descoberta, salvamento, conexão ou conversão? |

Pontuar cada critério em `0, 1 ou 2`. Tema abaixo de 6/8 não vira roteiro: a skill reenquadra ou sugere outro.

### Etapa 2 — Pesquisar quando o tema exigir

Se a pauta depende de conhecimento específico, atual ou controverso, pesquisar antes de roteirizar. Priorizar fonte primária, documentação oficial, estudo ou especialista identificável.

Registrar separadamente:

- fato verificável;
- inferência do criador;
- exemplo próprio;
- o que ainda é incerto.

Não pesquisar para encher o roteiro de curiosidades. Pesquisar para encontrar uma informação que mude a decisão ou torne a entrega mais útil.

### Etapa 3 — Abrir seis ângulos

Aplicar os Seis Chapéus como máquina de pauta, adaptada para Reels:

| Ângulo | Pergunta | Tipo de Reel provável |
|---|---|---|
| Fato | O que precisa ser entendido objetivamente? | explicação, teste, comparação. |
| Sentimento | Que frustração, desejo ou alívio existe? | conexão, história, identificação. |
| Risco | O que dá errado e como evitar? | diagnóstico, checklist, mito. |
| Benefício | O que melhora se a pessoa fizer direito? | antes/depois, caso, processo. |
| Criativo | Que comparação, metáfora ou demonstração torna isso visível? | contraste, experimento, visual. |
| Processo | Qual ordem reduz a dificuldade? | tutorial, template, lista. |

Gerar os seis ângulos em frases curtas. Depois recomendar somente um, baseado no objetivo atual.

### Etapa 4 — Escolher a estratégia de gancho

| Objetivo | Gancho recomendado | Condição |
|---|---|---|
| Descoberta/seguidores | Amplo ou híbrido | A abertura deve continuar conectada ao tema real. |
| Salvamentos | Específico ou híbrido | Prometer uma utilidade reutilizável e entregá-la. |
| Conexão | Específico | Usar experiência, bastidor ou pergunta reconhecível. |
| Conversão | Específico | Nomear situação, mecanismo, prova e próximo passo verdadeiro. |

Para o objetivo de **salvamento**, a skill precisa identificar pelo menos um ativo que a pessoa queira rever:

- checklist;
- processo em etapas;
- comparação com critério;
- matriz de decisão;
- template;
- regra prática com condição.

Sem ativo reutilizável, a sugestão deve mudar de objetivo ou de tema — não usar um CTA de "salve" por hábito.

### Etapa 5 — Selecionar estrutura

Escolher uma estrutura da biblioteca conforme o tema: tutorial de três passos, comparação, diagnóstico, correção de crença, pergunta de escolha, teste, pesquisa traduzida, bastidor, ranking, dor-virada-solução-ação ou seis ângulos.

A skill deve explicar em uma linha por que aquela estrutura foi escolhida e listar seus blocos antes de escrever a fala.

### Etapa 6 — Escrever o roteiro gravável

Entregar em cinco blocos:

1. **Gancho falado e texto na tela** — 0 a 3 segundos.
2. **Qualificador e contexto** — quem se beneficia e por quê.
3. **Desenvolvimento em blocos curtos** — uma ideia por bloco.
4. **Payoff** — resposta que quita a promessa.
5. **CTA** — uma ação possível e alinhada ao objetivo.

Para cada bloco, incluir apenas o necessário:

- fala exata ou bullets graváveis;
- texto na tela de até duas linhas;
- um apoio visual simples (tela, papel, checklist, comparativo ou gesto);
- transição de edição, se indispensável.

O padrão inicial deve ser Reel de 25 a 40 segundos e produção possível com celular e microfone. Se a ideia precisar de mais, dividir em série antes de esticar o roteiro.

### Etapa 7 — Checagem antes de gravar

Validar em formato curto:

- uma ideia principal;
- promessa cumprida;
- informação verdadeira ou fonte citada;
- visual que ajuda a entender;
- linguagem natural do usuário;
- CTA possível;
- uma hipótese de métrica para aprender depois.

## 6. Arquitetura de arquivos da futura skill

```text
roteirista-reels/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── workflow.md
│   ├── descoberta-do-criador.md
│   ├── avaliacao-de-temas.md
│   ├── angulos-seis-chapeus.md
│   ├── ganchos-por-objetivo.md
│   ├── estruturas-de-roteiro.md
│   ├── producao-simples.md
│   └── guardrails-e-validacao.md
└── assets/
    ├── ficha-de-contexto.md
    ├── scorecard-de-tema.md
    ├── ficha-de-roteiro.md
    ├── cartao-de-referencia.md
    └── registro-pos-publicacao.md
```

### SKILL.md: conteúdo mínimo

Deve conter apenas: gatilhos de uso, regras TDAH-first, ordem do fluxo, quando pesquisar, quando usar cada tipo de gancho e a regra de abrir as referências sob demanda. Fica curto para não carregar conteúdo repetido a cada uso.

### Referências: bases de conhecimento

| Arquivo | Conteúdo |
|---|---|
| `workflow.md` | Decisão do modo e sequência etapa a etapa. |
| `descoberta-do-criador.md` | Perguntas mínimas para conhecer conhecimento, público, objetivo e recursos. |
| `avaliacao-de-temas.md` | Scorecard de relevância, utilidade, prova e objetivo; critérios para pesquisar ou descartar. |
| `angulos-seis-chapeus.md` | Perguntas e saídas curtas para os seis ângulos. |
| `ganchos-por-objetivo.md` | Amplo, específico e híbrido; famílias de gancho e riscos. |
| `estruturas-de-roteiro.md` | Estruturas e blocos de cada uma; sem exemplos copiados de terceiros. |
| `producao-simples.md` | Texto na tela, apoio visual, gravação com celular e edição mínima. |
| `guardrails-e-validacao.md` | Verdade, fontes, claims, CTA, adequação e redução de sobrecarga. |

### Assets: artefatos que a skill preenche

| Asset | Função |
|---|---|
| `ficha-de-contexto.md` | Mantém o mapa do criador e evita perguntar tudo de novo. |
| `scorecard-de-tema.md` | Torna a escolha de pauta visual e objetiva. |
| `ficha-de-roteiro.md` | Entrega roteiro falado, visual, CTA e hipótese de teste. |
| `cartao-de-referencia.md` | Analisa mecanismo de referência sem incentivar cópia. |
| `registro-pos-publicacao.md` | Aprende com métricas e comentários para guiar a próxima pauta. |

## 7. O que não entra na primeira versão

- calendário editorial completo e automatizado;
- integração de postagem, agendamento ou DM;
- edição de vídeo automática;
- banco infinito de ganchos;
- pesquisa profunda em toda solicitação;
- promessa de alcance, viralização ou venda.

Esses itens aumentariam a complexidade antes de provar que o fluxo central ajuda alguém a escolher bom tema e gravar um bom Reel.

## 8. Critério de sucesso da skill

Após uma conversa curta, o usuário deve sair com:

1. um tema aprovado e explicado;
2. um ângulo escolhido entre seis possibilidades;
3. uma decisão explícita de gancho amplo, específico ou híbrido;
4. uma estrutura escolhida;
5. um roteiro que consiga gravar com os recursos disponíveis;
6. uma única hipótese para observar depois da postagem.

Se a skill gerar texto bonito, mas não conseguir responder por que aquele tema é útil para aquele público, ela falhou.

## 9. Próximo marco antes de implementar

Validar esta arquitetura com três cenários reais:

1. iniciante sem tema;
2. criador que quer Reel salvável;
3. especialista com uma ideia técnica que precisa de prova e simplificação.

Só depois, criar a pasta da skill, os assets e o `SKILL.md` definitivo.
