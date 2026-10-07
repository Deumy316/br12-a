import json, hashlib
from pathlib import Path

BASE = Path(__file__).resolve().parent
src = BASE / "input" / "records.json"
out = BASE / "output" / "summary.json"

data = json.loads(src.read_text(encoding="utf-8"))
summary = {
    "owner": data["owner"],
    "period": data["period"],
    "morning_records": int(data["ritual"]["morning"]),
    "closing_records": int(data["ritual"]["closing"]),
    "strength_count": len(data["strengths"]),
    "completed_projects": sum(1 for p in data["projects"] if p.get("completed")),
    "reserved_projects": [p["title"] for p in data["projects"] if not p.get("completed")],
    "strengths": [{"name":s["name"], "alias":s["alias"]} for s in data["strengths"]],
    "dated_scenes": sorted(data.get("events", []), key=lambda x: (x["date"], x["text"]))
}
payload = json.dumps(summary, ensure_ascii=False, sort_keys=True, separators=(",",":"))
summary["deterministic_hash"] = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
print("갱신 완료:", out)
print("아침 기록:", summary["morning_records"])
print("마무리 기록:", summary["closing_records"])
print("완료 프로젝트:", summary["completed_projects"])
print("동일 입력 확인용 해시:", summary["deterministic_hash"])
