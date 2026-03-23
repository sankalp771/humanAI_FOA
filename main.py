import argparse
from extractor import fetch_foa, extract_fields, parse_date
from tagger import apply_tags
from exporter import save_output

def parse_args():
    parser = argparse.ArgumentParser(description="FOA Ingestion Pipeline")
    parser.add_argument("--url", required=True, help="Grants.gov FOA URL")
    parser.add_argument("--out_dir", default="./out")
    return parser.parse_args()

def get_opp_id(url):
    # URL se oppId nikalo
    # e.g. https://grants.gov/search-results-detail/354588 → 354588
    return url.rstrip("/").split("/")[-1]

def main():
    args = parse_args()
    
    opp_id = get_opp_id(args.url)
    print(f"Fetching FOA: {opp_id}")
    
    raw = fetch_foa(opp_id)
    fields = extract_fields(raw, args.url)
    fields = apply_tags(fields)
    save_output(fields, args.out_dir)
    
    print("FOA Extraction done!")

if __name__ == "__main__":
    main()