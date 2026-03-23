# FOA Ingestion Pipeline

An automated pipeline to ingest Funding Opportunity Announcements (FOAs) 
from Grants.gov, extract structured fields, and apply ontology-based 
semantic tags.

## Setup
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py --url "https://grants.gov/search-results-detail/353796" --out_dir ./out
```

## Output

- `out/foa.json` — structured FOA data
```
{
  "foa_id": "AFYDE-TSCTP-CVE-WLP-GR-POLECON-2024",
  "title": "Trans-Sahara Counterterrorism Partnership/CVE Program-Women Leading Peace, POL/ECON, U.S. Embassy Yaounde",
  "agency": "Lucresse R Ngum\nGrantor",
  "open_date": "2024-04-25",
  "close_date": "2024-06-23",
  "eligibility": "The Trans-Sahara Counterterrorism Partnership/CVE Program for Women Leading Peace fund is limited to Cameroonian local registered community-based organizations, associations, non-governmental organizations (NGOs) with at least 2 years of experience working in the areas of Human Rights and Countering Violent Extremism (CVE). Organizations and entities with a prior history of poor performance of U.S. government grants are ineligible for this funding.",
  "program_description": "<p>The Political and Economic Section of the U.S. Embassy in Yaound\u00e9, Cameroon announces an open competition for organizations to submit applications under the 2024 Trans-Sahara Counterterrorism Partnership (TSCTP)/CVE <span style=\"color: rgb(36, 36, 36);\">Program</span> for <span style=\"color: rgb(36, 36, 36);\">Women Leading Peace in West Africa</span>. Proposals funded under this announcement should seek to increase the representation of women in peace and security decision-making positions and reduce the radicalization and recruitment of youths in non-state armed groups in the Northwest and Southwest regions of Cameroon by March 2026.</p>\n<p>&nbsp;</p>\n<p><u>Note</u>: The U.S. Embassy expects to receive funding for the TSCTP/CVE-WLP program before September 30, 2024.&nbsp;Grant awards are contingent on the receipt of funding. If the program is not approved, no grants will be awarded under this call.</p>",
  "award_ceiling": "200,000",
  "award_floor": "100,000",
  "source_url": "https://grants.gov/search-results-detail/353796",
  "tags": {
    "research_domains": [],
    "methods": [],
    "populations": [
      "Youth"
    ]
  }
}
```
- `out/foa.csv` — same data in CSV format
```
foa_id,title,agency,open_date,close_date,eligibility,program_description,award_ceiling,award_floor,source_url,tags
AFYDE-TSCTP-CVE-WLP-GR-POLECON-2024,"Trans-Sahara Counterterrorism Partnership/CVE Program-Women Leading Peace, POL/ECON, U.S. Embassy Yaounde","Lucresse R Ngum
Grantor",2024-04-25,2024-06-23,"The Trans-Sahara Counterterrorism Partnership/CVE Program for Women Leading Peace fund is limited to Cameroonian local registered community-based organizations, associations, non-governmental organizations (NGOs) with at least 2 years of experience working in the areas of Human Rights and Countering Violent Extremism (CVE). Organizations and entities with a prior history of poor performance of U.S. government grants are ineligible for this funding.","<p>The Political and Economic Section of the U.S. Embassy in Yaoundé, Cameroon announces an open competition for organizations to submit applications under the 2024 Trans-Sahara Counterterrorism Partnership (TSCTP)/CVE <span style=""color: rgb(36, 36, 36);"">Program</span> for <span style=""color: rgb(36, 36, 36);"">Women Leading Peace in West Africa</span>. Proposals funded under this announcement should seek to increase the representation of women in peace and security decision-making positions and reduce the radicalization and recruitment of youths in non-state armed groups in the Northwest and Southwest regions of Cameroon by March 2026.</p>
<p>&nbsp;</p>
<p><u>Note</u>: The U.S. Embassy expects to receive funding for the TSCTP/CVE-WLP program before September 30, 2024.&nbsp;Grant awards are contingent on the receipt of funding. If the program is not approved, no grants will be awarded under this call.</p>","200,000","100,000",https://grants.gov/search-results-detail/353796,"{""research_domains"": [], ""methods"": [], ""populations"": [""Youth""]}"
```

## Project Structure
```
├── main.py          # CLI entry point
├── extractor.py     # API fetch + field extraction
├── tagger.py        # Ontology-based semantic tagging
├── exporter.py      # JSON + CSV export
├── ontology.json    # Controlled vocabulary for tagging
└── out/             # Output directory
```

## Design Decisions

- **API over scraping:** Grants.gov public REST API used instead of HTML 
  scraping for reliability and structured data access
- **Modular structure:** Each concern separated into its own module
- **Ontology-driven tagging:** Tags derived from a controlled vocabulary 
  (ontology.json) — easily extensible for new domains
- **Graceful error handling:** Network failures return empty dict, 
  pipeline continues without crashing

## Tagging Approach

Rule-based tagging using keyword matching across three categories:
- `research_domains` — subject area of the FOA
- `methods` — approaches mentioned
- `populations` — target groups identified

Ontology can be extended without changing pipeline code.