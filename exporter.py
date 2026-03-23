import json
import csv
import os

def save_output(fields, out_dir="./out"):
    os.makedirs(out_dir, exist_ok=True)
    
    # JSON save
    json_path = os.path.join(out_dir, "foa.json")
    with open(json_path, "w") as f:
        json.dump(fields, f, indent=2)
    
    # CSV save — tags ko string mein convert karo
    csv_path = os.path.join(out_dir, "foa.csv")
    flat = fields.copy()
    flat["tags"] = json.dumps(fields.get("tags", {}))
    
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=flat.keys())
        writer.writeheader()
        writer.writerow(flat)
    
    print(f"✅ Saved: {json_path}")
    print(f"✅ Saved: {csv_path}")