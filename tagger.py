import json

def load_ontology(path="ontology.json"):
    with open(path, "r") as f:
        return json.load(f)

def apply_tags(fields, ontology_path="ontology.json"):
    ontology = load_ontology(ontology_path)
    
    # Jis text pe tagging karni hai
    text = " ".join([
        fields.get("program_description", ""),
        fields.get("eligibility", ""),
        fields.get("title", "")
    ]).lower()
    
    tags = {}
    
    for category, domain_dict in ontology.items():
        matched = []
        for domain, keywords in domain_dict.items():
            for keyword in keywords:
                if keyword.lower() in text:
                    matched.append(domain)
                    break  # ek domain ek baar hi add ho
        tags[category] = matched
    
    fields["tags"] = tags
    return fields