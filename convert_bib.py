import re

# 1. Load the BibTeX file
input_file = 'static/ralfschmaelzle.bib'
output_file = 'content/publications_list.md'

print(f"Reading {input_file}...")

with open(input_file, 'r', encoding='utf-8') as f:
    raw_data = f.read()

# 2. Parse Entries (Simple Regex parser to avoid dependencies)
entries = []
# Split by @Article, @InBook, etc.
raw_entries = re.split(r'@\w+\{', raw_data)[1:]

for raw in raw_entries:
    entry = {}
    
    # Extract Year
    year_match = re.search(r'year\s*=\s*\{(\d+)\}', raw, re.IGNORECASE)
    entry['year'] = int(year_match.group(1)) if year_match else 9999
    
    # Extract Title
    title_match = re.search(r'title\s*=\s*\{(.*?)\}', raw, re.IGNORECASE | re.DOTALL)
    if title_match:
        entry['title'] = title_match.group(1).replace('\n', ' ').replace('  ', ' ')
    
    # Extract Author
    author_match = re.search(r'author\s*=\s*\{(.*?)\}', raw, re.IGNORECASE | re.DOTALL)
    if author_match:
        entry['author'] = author_match.group(1).replace('\n', ' ')
        entry['author'] = entry['author'].replace(' and ', ', ') # Replace 'and' with commas
    
    # Extract Journal
    journal_match = re.search(r'journal\s*=\s*\{(.*?)\}', raw, re.IGNORECASE)
    if journal_match:
        entry['journal'] = journal_match.group(1)
    
    # Extract Links
    doi_match = re.search(r'doi\s*=\s*\{(.*?)\}', raw, re.IGNORECASE)
    entry['doi'] = doi_match.group(1) if doi_match else None
    
    code_match = re.search(r'code\s*=\s*\{(.*?)\}', raw, re.IGNORECASE)
    entry['code'] = code_match.group(1) if code_match else None
    
    entries.append(entry)

# 3. Sort by Year (Descending)
entries.sort(key=lambda x: x['year'], reverse=True)

# 4. Generate Markdown
markdown_output = ""
current_year = 0

for item in entries:
    # Add Year Header if it changes
    if item['year'] != current_year:
        current_year = item['year']
        if current_year != 9999:
            markdown_output += f"\n### {current_year}\n\n"
        else:
            markdown_output += "\n### In Press / Preprints\n\n"
    
    # Format the Entry
    # Style: **Title**. Author. *Journal*. [Links]
    markdown_output += f"*   **{item.get('title', 'Untitled')}**.\n"
    markdown_output += f"    {item.get('author', 'Unknown')}.\n"
    if item.get('journal'):
        markdown_output += f"    *{item['journal']}*.\n"
    
    # Add Links
    links = []
    if item['doi']: links.append(f"[DOI]({item['doi']})")
    if item['code']: links.append(f"[CODE]({item['code']})")
    
    if links:
        markdown_output += "    " + " | ".join(links) + "\n"
    
    markdown_output += "\n"

# 5. Save to file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(markdown_output)

print(f"Success! Saved {len(entries)} papers to {output_file}")