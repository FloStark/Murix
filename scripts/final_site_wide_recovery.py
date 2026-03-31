import os

def final_site_wide_recovery(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Restoration of Broken Tags
    content = content.replace(
        '<a href="index.html#kontakt" class="btn btn-primary btn-lg magnetic"><span></a>',
        '<a href="javascript:void(0)" class="btn btn-primary btn-lg magnetic" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'>\n                    <span>Kostenloses Erstgespräch buchen</span>\n                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n                        <path d="M5 12h14M12 5l7 7-7 7" />\n                    </svg>\n                </a>'
    )
    content = content.replace(
        'class="btn btn-primary btn-lg magnetic" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'><span></a>',
        'class="btn btn-primary btn-lg magnetic" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'>\n                    <span>Kostenloses Erstgespräch buchen</span>\n                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n                        <path d="M5 12h14M12 5l7 7-7 7" />\n                    </svg>\n                </a>'
    )

    # Specific Fix for Steiermark (had slightly different button text in hero or cta)
    if "webdesign-steiermark.html" in file_path:
         content = content.replace(
            '<a href="javascript:void(0)" class="btn btn-primary magnetic" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'><span>Jetzt Website\n                            anfragen</span>',
            '<a href="javascript:void(0)" class="btn btn-primary magnetic" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'><span>Jetzt Website anfragen</span>'
        )

    # Ensure all (inkl. MwSt.) mentions are unified
    content = content.replace('€690</strong>, Komplett-Paket ab <strong>€1.490</strong>.', '€690</strong> (inkl. MwSt.), Komplett-Paket ab <strong>€1.490</strong> (inkl. MwSt.).')
    content = content.replace('€690</strong> (inkl. MwSt.), Komplett-Paket ab <strong>€1.490</strong>.', '€690</strong> (inkl. MwSt.), Komplett-Paket ab <strong>€1.490</strong> (inkl. MwSt.).')
    
    # Ensure href="javascript:void(0)" for all data-cal-link
    content = content.replace('href="index.html#kontakt" class="btn btn-primary btn-full magnetic" data-cal-link="murix/30min"', 'href="javascript:void(0)" class="btn btn-primary btn-full magnetic" data-cal-link="murix/30min"')
    content = content.replace('href="index.html#kontakt" class="btn btn-primary magnetic" data-cal-link="murix/30min"', 'href="javascript:void(0)" class="btn btn-primary magnetic" data-cal-link="murix/30min"')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    directory = "/home/ubuntu/Antigravity/Murix-Backup"
    files = [f for f in os.listdir(directory) if f.endswith(".html")]
    for fname in files:
        final_site_wide_recovery(os.path.join(directory, fname))

if __name__ == "__main__":
    main()
