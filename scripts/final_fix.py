import os

def final_fix(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hero/Section Titles
    content = content.replace(
        '<h2>Kostenloses </a>',
        '<h2>Kostenloses Erstgespräch.</h2>\n                <p>Lassen Sie uns in einem kostenlosen Erstgespräch besprechen, wie wir Ihnen helfen können.</p>\n                <a href="index.html#kontakt" class="btn btn-primary btn-lg magnetic" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'>\n                    <span>Kostenloses Erstgespräch buchen</span>\n                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n                        <path d="M5 12h14M12 5l7 7-7 7" />\n                    </svg>\n                </a>'
    )
    
    content = content.replace(
        '<span>Kostenloses </a>',
        '<span>Kostenloses Erstgespräch</span></a>'
    )
    
    content = content.replace(
        '<span>Kostenloses SEO-</a>',
        '<span>Kostenloses SEO-Erstgespräch</span></a>'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    directory = "/home/ubuntu/Antigravity/Murix-Backup"
    files = [f for f in os.listdir(directory) if f.endswith(".html")]
    for fname in files:
        final_fix(os.path.join(directory, fname))

if __name__ == "__main__":
    main()
