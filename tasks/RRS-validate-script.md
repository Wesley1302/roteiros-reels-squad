---
agent: RRS-evidence-editor
inputs: [script_draft, approved_hook, evidence_ledger, objective]
outputs: [validation_report, approved_script]
---

# RRS-validate-script

Rodar os checklists de evidência, hook, roteiro e TDAH.

Classificar problemas:

- `fact`: alegação sem suporte;
- `promise`: hook não entregue;
- `clarity`: leigo não entende;
- `retention`: bloco não adiciona valor;
- `scope`: tema amplo demais;
- `production`: depende de recurso não disponível.

PASS envia ao diretor. FAIL devolve correções cirúrgicas ao dono da etapa.

Aceite: zero dados inventados, um CTA e legenda como único texto visual.
