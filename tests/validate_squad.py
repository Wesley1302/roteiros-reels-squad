from __future__ import annotations

import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    errors: list[str] = []
    config = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))

    for agent_id, spec in config["agents"].items():
        path = ROOT / spec["file"]
        if not path.is_file():
            errors.append(f"agent ausente: {agent_id} -> {spec['file']}")

    for task_id, rel in config["tasks"].items():
        if not (ROOT / rel).is_file():
            errors.append(f"task ausente: {task_id} -> {rel}")

    for workflow_id, rel in config["workflows"].items():
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"workflow ausente: {workflow_id} -> {rel}")
        else:
            yaml.safe_load(path.read_text(encoding="utf-8"))

    for rel in config["checklists"]:
        if not (ROOT / rel).is_file():
            errors.append(f"checklist ausente: {rel}")

    for rel in config["data"].values():
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"data ausente: {rel}")
        elif path.suffix in {".yaml", ".yml"}:
            yaml.safe_load(path.read_text(encoding="utf-8"))

    command_files = list((ROOT / ".claude" / "commands").glob("reels-*.md"))
    if len(command_files) != len(config["commands"]["map"]):
        errors.append("quantidade de comandos visíveis difere do manifesto")

    notion_text = (ROOT / "data" / "RRS-notion-50-models.md").read_text(encoding="utf-8")
    model_count = len(re.findall(r"(?m)^## MODELO \d{2}:", notion_text))
    if model_count != 50:
        errors.append(f"catálogo Notion contém {model_count}, esperado 50")

    hook_data = yaml.safe_load((ROOT / "data" / "RRS-hook-library.yaml").read_text(encoding="utf-8"))
    if len(hook_data["jeff_nippard_style"]["patterns"]) < 4:
        errors.append("banco Jeff Nippard incompleto")

    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    critical = [
        "Tema abaixo de 6/8 não vira roteiro",
        "Hook precisa ser aprovado antes do roteiro",
        "Exatamente um CTA",
        "Texto visual é somente legenda sincronizada",
    ]
    for rule in critical:
        if rule not in skill_text:
            errors.append(f"regra crítica ausente: {rule}")

    source_registry = yaml.safe_load((ROOT / "data" / "RRS-source-registry.yaml").read_text(encoding="utf-8"))
    for source in source_registry["sources"]:
        if not (ROOT / source["path"]).is_file():
            errors.append(f"fonte registrada ausente: {source['id']} -> {source['path']}")

    report = {
        "status": "PASS" if not errors else "FAIL",
        "agents": len(config["agents"]),
        "tasks": len(config["tasks"]),
        "workflows": len(config["workflows"]),
        "checklists": len(config["checklists"]),
        "commands": len(command_files),
        "notion_models": model_count,
        "errors": errors,
    }
    (ROOT / "validation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
