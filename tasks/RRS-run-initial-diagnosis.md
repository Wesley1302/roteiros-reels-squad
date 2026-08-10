---
agent: RRS-chief
inputs: [user_message, journey_state]
outputs: [mode, current_workflow, next_task]
---

# RRS-run-initial-diagnosis

1. Classificar o pedido: `from_zero`, `find_topics`, `topic_to_script`, `current_ai_update`, `improve_draft` ou `post_publication`.
2. Ler estado e preservar respostas anteriores.
3. Se ambíguo, perguntar apenas: “Você quer encontrar um tema, criar um roteiro, melhorar um rascunho ou analisar um vídeo publicado?”
4. Selecionar workflow e gravar `journey.current_*`.

Aceite: modo e próximo passo definidos em até cinco linhas, sem pergunta repetida.

Handoff: por `data/RRS-handoff-map.yaml`.
