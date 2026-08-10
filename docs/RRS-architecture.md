# Arquitetura do Roteiros Reels Squad

## Camadas

| Camada | Componentes | Responsabilidade |
|---|---|---|
| Orquestração | RRS-chief | diagnosticar, preservar state, rotear e bloquear atalhos |
| Estratégia | creator, topic, angle, hook | decidir o que vale dizer e por qual mecanismo |
| Produção | scriptwriter, evidence editor, recording director | transformar decisão em roteiro verdadeiro e gravável |
| Aprendizado | iteration analyst | converter publicação em hipótese e próximo teste |

## Unidade executável

A Task é a unidade reutilizável. Agentes são donos de tarefas; workflows ordenam tarefas; handoffs exigem artefatos e gates; state preserva decisões.

## Ordem bloqueante

`Mapa → Tema ≥6/8 → Pesquisa quando necessária → Ângulo aprovado → Hook aprovado → Estrutura → Roteiro → QA → Direção → Métricas`

## Decisões incorporadas

- TDAH-first: uma decisão por vez e até três opções.
- Objetivo atual conhecido: seguidores; o sistema continua adaptável.
- Público inicial: usuários leigos ou intermediários de IA no navegador.
- Produção: rosto na câmera, celular, microfone, dois Reels por semana.
- Texto na tela: somente legenda sincronizada.
- AIOX é referência de organização; a identidade e os comandos são RRS/reels-*.
