import os
import re

# Cal.com script to inject
CAL_SCRIPT = """
    <!-- Cal element-click embed code begins -->
    <script type="text/javascript">
    (function (C, A, L) { let p = function (a, ar) { a.q.push(ar); }; let d = C.document; C.Cal = C.Cal || function () { let cal = C.Cal; let ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; } if (ar[0] === L) { const api = function () { p(api, arguments); }; const namespace = ar[1]; api.q = api.q || []; if(typeof namespace === "string"){cal.ns[namespace] = cal.ns[namespace] || api;p(cal.ns[namespace], ar);p(cal, ["initNamespace", namespace]);} else p(cal, ar); return;} p(cal, ar); }; })(window, "https://app.cal.eu/embed/embed.js", "init");
    Cal("init", "30min", {origin:"https://app.cal.eu"});
    </script>
    <!-- Cal element-click embed code ends -->
"""

# Cal.com attributes for CTA buttons
CAL_ATTRS = 'data-cal-link="murix/30min" data-cal-namespace="30min" data-cal-config=\'{"layout":"month_view","useSlotsViewOnSmallScreen":"true"}\''

def update_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Update Wording: "Kein Abo-Zwang" instead of "Ohne laufende Kosten"
    content = content.replace("ohne laufende Kosten", "ohne Abo-Zwang")
    content = content.replace("keine laufenden Kosten", "kein Abo-Zwang")
    content = content.replace("Keine laufenden Kosten", "Kein Abo-Zwang")
    
    # Special fix for Static vs CMS table line if it exists
    content = content.replace("<span>0€ (nur Domain)</span>", "<span>0€ (Kein Abo-Zwang)</span>")

    # 2. Inject Cal.com Script before </body> if not present
    if "https://app.cal.eu/embed/embed.js" not in content:
        content = content.replace("</body>", f"{CAL_SCRIPT}\n</body>")

    # 3. Add Cal.com attributes to CTA buttons
    # Regex to find <a> tags with specific button text that don't have cal-link yet
    def add_cal_attrs(match):
        attrs = match.group(1)
        text = match.group(2)
        if 'data-cal-link' not in attrs:
            # Reconstruct the tag with new attributes
            return f'<a {attrs} {CAL_ATTRS}>{text}</a>'
        return match.group(0)

    # Improved regex to capture the entire <a> tag opening and content
    # Look for buttons that contain typical CTA text
    pattern = r'<a ([^>]*class="[^"]*(?:\bbtn\b|\bnav-cta\b)[^"]*"[^>]*)>(.*?)(?:Erstgespräch|Jetzt starten|Termin buchen|Termin vereinbaren)(.*?)</a>'
    content = re.sub(pattern, add_cal_attrs, content, flags=re.IGNORECASE | re.DOTALL)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {file_path}")
    else:
        print(f"⚠️  No changes for {file_path}")

def main():
    # Use actual path of the project
    directory = "/home/ubuntu/Antigravity/Murix-Backup"
    html_files = [f for f in os.listdir(directory) if f.endswith(".html")]
    
    # Files to skip
    skip_files = ["index.html", "impressum.html", "datenschutz.html"]
    
    for filename in html_files:
        if filename not in skip_files:
            file_path = os.path.join(directory, filename)
            update_html_file(file_path)

if __name__ == "__main__":
    main()
