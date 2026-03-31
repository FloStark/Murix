import os

def final_price_consistency(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add "inkl. MwSt." where prices are mentioned in lists or text
    content = content.replace("Ab €690 einmalig – kein Abo", "Ab €690 einmalig – inkl. MwSt., kein Abo")
    content = content.replace("Ab €690 einmalig – kein Abo-Zwang", "Ab €690 einmalig – inkl. MwSt., kein Abo-Zwang")
    content = content.replace("ab €690, Komplett-Paket ab €1.490", "ab €690, Komplett-Paket ab €1.490 (inkl. MwSt.)")
    content = content.replace("OnePager ab <strong>€690</strong>", "OnePager ab <strong>€690</strong> (inkl. MwSt.)")
    content = content.replace("Immobilien-Website ab <strong>€1.490</strong>", "Immobilien-Website ab <strong>€1.490</strong> (inkl. MwSt.)")
    content = content.replace("Ab €690 (OnePager) oder ab €1.490 (Komplett-Paket mit SEO)", "Ab €690 (OnePager) oder ab €1.490 (Komplett-Paket mit SEO) – inkl. MwSt.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    directory = "/home/ubuntu/Antigravity/Murix-Backup"
    files = ["webdesign-handwerker.html", "webdesign-gastronomie.html", "webdesign-immobilien.html", "webdesign-steiermark.html", "website-erstellen-lassen.html"]
    for fname in files:
        final_price_consistency(os.path.join(directory, fname))

if __name__ == "__main__":
    main()
