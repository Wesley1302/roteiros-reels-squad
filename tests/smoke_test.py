from __future__ import annotations

import json


def route(message: str) -> str:
    text = message.casefold()
    if any(term in text for term in ("métrica", "publiquei", "retenção")):
        return "RRS-post-publication-learning"
    if any(term in text for term in ("rascunho", "melhorar roteiro", "revisar roteiro")):
        return "RRS-improve-draft"
    if any(term in text for term in ("lançamento", "novidade", "saiu agora", "nova função")):
        return "RRS-current-ai-update"
    if any(term in text for term in ("tema", "roteiro sobre", "quero ensinar")):
        return "RRS-topic-to-script"
    return "RRS-from-zero"


def main() -> None:
    cases = {
        "Não sei o que postar sobre IA": "RRS-from-zero",
        "Quero ensinar um tema sobre editar imagens com JSON": "RRS-topic-to-script",
        "Saiu agora uma nova função no Gemini": "RRS-current-ai-update",
        "Quero melhorar este rascunho": "RRS-improve-draft",
        "Publiquei e trouxe as métricas de retenção": "RRS-post-publication-learning",
    }
    results = {message: route(message) for message in cases}
    failures = [message for message, expected in cases.items() if results[message] != expected]
    print(json.dumps({"status": "PASS" if not failures else "FAIL", "routes": results, "failures": failures}, ensure_ascii=False, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
