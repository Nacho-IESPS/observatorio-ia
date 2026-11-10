import json, pathlib, datetime
p=pathlib.Path(__file__).resolve().parents[1]/"data"/"incidentes.json"
d=json.loads(p.read_text(encoding="utf-8"))
assert isinstance(d.get("incidentes"),list)
seen=set()
for x in d["incidentes"]:
    for k in ("id","titulo","organizacion","fecha_publicacion","tipo","entorno","estado","resumen","limitaciones","fuentes"):
        assert x.get(k),f"Falta {k}"
    assert x["id"] not in seen
    seen.add(x["id"])
    assert x["entorno"] in ("producción","interno","evaluación")
    datetime.date.fromisoformat(x["fecha_publicacion"])
    if x.get("fecha_incidente"):datetime.date.fromisoformat(x["fecha_incidente"])
    assert all(s.get("url","").startswith("https://") and s.get("titulo") for s in x["fuentes"])
print(f"Validación correcta: {len(seen)} incidentes")
