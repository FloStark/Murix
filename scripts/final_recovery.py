import os

def final_recovery_fix(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Restore truncated button text and icons specifically for Handwerker page
    if "webdesign-handwerker.html" in file_path:
        content = content.replace(
            '<a href="index.html#kontakt"\n                    class="btn btn-primary btn-lg magnetic"><span></a>',
            '<a href="javascript:void(0)" class="btn btn-primary btn-lg magnetic" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'>\n                    <span>Kostenloses Erstgespräch buchen</span>\n                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n                        <path d="M5 12h14M12 5l7 7-7 7" />\n                    </svg>\n                </a>'
        )
        # Fix Hero CTA as well
        content = content.replace(
            '<a href="index.html#kontakt" class="btn btn-primary magnetic" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'><span>Jetzt Website\n                            anfragen</span>',
            '<a href="javascript:void(0)" class="btn btn-primary magnetic" data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\'><span>Jetzt Website anfragen</span>'
        )

    # 2. Fix the redirect issue for ALL Cal.com buttons
    # Change href="index.html#kontakt" to href="javascript:void(0)" ONLY when data-cal-link is present
    # We do a targeted string replacement to avoid regex issues
    content = content.replace(
        'href="index.html#kontakt" class="btn btn-primary magnetic" data-cal-link="murix/30min"',
        'href="javascript:void(0)" class="btn btn-primary magnetic" data-cal-link="murix/30min"'
    )
    content = content.replace(
        'href="index.html#kontakt" class="btn btn-primary btn-full magnetic" data-cal-link="murix/30min"',
        'href="javascript:void(0)" class="btn btn-primary btn-full magnetic" data-cal-link="murix/30min"'
    )
    content = content.replace(
        'href="index.html#kontakt" class="btn btn-primary btn-lg magnetic" data-cal-link="murix/30min"',
        'href="javascript:void(0)" class="btn btn-primary btn-lg magnetic" data-cal-link="murix/30min"'
    )
    content = content.replace(
        'href="index.html#kontakt" class="nav-link nav-cta" data-cal-link="murix/30min"',
        'href="javascript:void(0)" class="nav-link nav-cta" data-cal-link="murix/30min"'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Final recovery applied to {file_path}")

def main():
    directory = "/home/ubuntu/Antigravity/Murix-Backup"
    files = [f for f in os.listdir(directory) if f.endswith(".html")]
    skip = ["index.html", "impressum.html", "datenschutz.html"]
    
    for fname in files:
        if fname not in skip:
            final_recovery_fix(os.path.join(directory, fname))

if __name__ == "__main__":
    main()
