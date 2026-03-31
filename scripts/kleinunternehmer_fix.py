import os

def apply_kleinunternehmer_status(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove all "inkl. MwSt." mentions including parentheses
    content = content.replace(" (inkl. MwSt.)", "")
    content = content.replace(" inkl. MwSt.", "")
    content = content.replace(", inkl. MwSt.", "")
    content = content.replace("inkl. MwSt.", "")

    # 2. Update Pricing Disclaimer in index.html
    if "index.html" in file_path:
        content = content.replace(
            "Alle Preise verstehen sich inkl. MwSt. Gerne erstellen wir",
            "Alle Preise sind Endpreise. Aufgrund der Kleinunternehmerregelung gemäß § 6 Abs. 1 Z 27 UStG wird keine Umsatzsteuer erhoben. Gerne erstellen wir"
        )

    # 3. Update Impressum
    if "impressum.html" in file_path:
        # Check if it already has a tax section, if not add it
        if "Umsatzsteuer" not in content:
            content = content.replace(
                "</h4>", # After the first H4 usually
                "</h4>\n                    <p>Umsatzsteuerfrei aufgrund der Kleinunternehmerregelung gemäß § 6 Abs. 1 Z 27 UStG.</p>",
                1
            )
        else:
             content = content.replace(
                "Umsatzsteuer-Identifikationsnummer",
                "Umsatzsteuerbefreit aufgrund der Kleinunternehmerregelung gemäß § 6 Abs. 1 Z 27 UStG."
            )

    # 4. Standard Disclaimer for subpages if they mention prices
    disclaimer = "Umsatzsteuerbefreit gem. § 6 Abs. 1 Z 27 UStG"
    if "was-kostet-eine-website.html" in file_path:
        content = content.replace(
            "Alle Details auf unserer Preisseite",
            f"{disclaimer}. Alle Details auf unserer Preisseite"
        )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Kleinunternehmer status applied to {file_path}")

def main():
    directory = "/home/ubuntu/Antigravity/Murix-Backup"
    files = [f for f in os.listdir(directory) if f.endswith(".html")]
    for fname in files:
        apply_kleinunternehmer_status(os.path.join(directory, fname))

if __name__ == "__main__":
    main()
