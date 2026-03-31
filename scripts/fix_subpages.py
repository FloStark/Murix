import os

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix Wording
    content = content.replace("ohne laufende Kosten", "ohne Abo-Zwang")
    content = content.replace("keine laufenden Kosten", "kein Abo-Zwang")
    content = content.replace("Keine laufenden Kosten", "Kein Abo-Zwang")

    # 2. Fix the broken button texts from the failed regex run
    # Hero CTA in webdesign-graz
    content = content.replace(
        '<span>Kostenloses </a>',
        '<span>Kostenloses Erstgespräch</span>\n                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"\n                            stroke-width="2">\n                            <path d="M5 12h14M12 5l7 7-7 7" />\n                        </svg>\n                    </a>'
    )
    
    # Hero CTA in SEO Graz
    content = content.replace(
        '<span>Kostenloses\n                            SEO-</a>',
        '<span>Kostenloses SEO-Erstgespräch</span>\n                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"\n                            stroke-width="2">\n                            <path d="M5 12h14M12 5l7 7-7 7" />\n                        </svg>\n                    </a>'
    )
    
    # Bottom CTA in most pages
    content = content.replace(
        '<p>Kostenloses </a>',
        '<p>Lassen Sie uns in einem kostenlosen Erstgespräch besprechen, wie wir Ihnen helfen können.</p>\n                <a href="index.html#kontakt" class="btn btn-primary btn-lg magnetic" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'>\n                    <span>Kostenloses Erstgespräch buchen</span>\n                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n                        <path d="M5 12h14M12 5l7 7-7 7" />\n                    </svg>\n                </a>'
    )
    
    # Sidebar CTA
    content = content.replace(
        '<span>Jetzt analysieren\n                                lassen</span></a>',
        '<span>Jetzt analysieren lassen</span></a>'
    )
    
    # Static vs CMS specific fixes
    content = content.replace(
        '<span>0€ (nur\n                                Domain)</span>',
        '<span>0€ (Kein Abo-Zwang)</span>'
    )
    content = content.replace(
        '<span>0€ (nur Domain)</span>',
        '<span>0€ (Kein Abo-Zwang)</span>'
    )
    content = content.replace(
        'Static oder CMS – im </a>',
        'Static oder CMS – im Erstgespräch finden wir die beste Lösung für Sie.</p>\n                <a href="index.html#kontakt" class="btn btn-primary btn-lg magnetic" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'><span>Erstgespräch buchen</span><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"\n                        stroke-width="2">\n                        <path d="M5 12h14M12 5l7 7-7 7" />\n                    </svg></a>'
    )

    # Nav CTA fixes
    content = content.replace(
        'class="nav-link nav-cta" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'></a>',
        'class="nav-link nav-cta" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'>Jetzt starten</a>'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {file_path}")

def main():
    directory = "/home/ubuntu/Antigravity/Murix-Backup"
    files = [f for f in os.listdir(directory) if f.endswith(".html")]
    skip = ["index.html", "impressum.html", "datenschutz.html"]
    
    for fname in files:
        if fname not in skip:
            fix_file(os.path.join(directory, fname))

if __name__ == "__main__":
    main()
