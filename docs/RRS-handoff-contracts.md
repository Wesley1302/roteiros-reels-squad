# Contratos de handoff

Todo handoff exige: artefatos presentes, gate PASS e atualização de state.

Formato:

```yaml
from:
to:
from_task:
to_task:
required_artifacts: []
pass:
fail_route:
```

Regras críticas:

- tema abaixo de 6/8 retorna ao estrategista;
- alegação sem suporte retorna ao pesquisador;
- ângulo ou hook sem aprovação não avança;
- roteiro reprovado volta somente ao dono do erro;
- direção de gravação só recebe roteiro aprovado;
- análise pós-publicação não infere causalidade de uma única métrica.

Mapa executável: `data/RRS-handoff-map.yaml`.
