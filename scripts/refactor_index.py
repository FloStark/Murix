import sys
import re

def refactor():
    with open('/home/ubuntu/Antigravity/Murix-Backup/index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    warum_murix = """    <!-- ==================== WARUM MURIX ==================== -->
    <section class="section vorteile" id="warum">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Warum Murix wählen</span>
                <h2 class="section-title">Technik, die funktioniert.<br><span class="text-gradient-animated">Und ein Partner, der bleibt.</span></h2>
                <p class="section-subtitle">Drei Gründe, warum sich Unternehmen für uns entscheiden.</p>
            </div>
            <div class="vorteile-grid">
                <div class="vorteil-card reveal" data-delay="0">
                    <div class="vorteil-icon-wrap"><svg width="28" height="28" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="1.5">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
                            <polyline points="22 4 12 14.01 9 11.01" />
                        </svg></div>
                    <h3>1. Premium zum Festpreis</h3>
                    <p>Keine monatlichen Website-Abos, keine versteckten Kosten. Sie zahlen einen fairen Einmalpreis für Ihre fertige Website – inkl. Texte, Design und lokalem SEO. Das Ergebnis ist 100% Ihr Eigentum.</p>
                </div>
                <div class="vorteil-card reveal" data-delay="100">
                    <div class="vorteil-icon-wrap"><svg width="28" height="28" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="1.5">
                            <line x1="12" y1="1" x2="12" y2="23" />
                            <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
                        </svg></div>
                    <h3>2. Technik, die konvertiert</h3>
                    <p>Wir bauen in erster Linie blitzschnelle Static Pages. Diese laden schneller im Browser, ranken besser auf Google und bieten Hackern keine Angriffsfläche. Weniger Technik-Ballast, mehr Performance.</p>
                </div>
                <div class="vorteil-card reveal" data-delay="200">
                    <div class="vorteil-icon-wrap"><svg width="28" height="28" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="1.5">
                            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
                            <circle cx="9" cy="7" r="4" />
                            <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
                            <path d="M16 3.13a4 4 0 0 1 0 7.75" />
                        </svg></div>
                    <h3>3. Langfristiger Begleiter</h3>
                    <p>Nach dem Go-Live lassen wir Sie nicht allein. Als Ihr verlässlicher IT-Betreuer aus Graz übernehmen wir auf Wunsch die laufende Wartung (Murix Care) und Ihre gesamte Microsoft 365 Umgebung.</p>
                </div>
            </div>
        </div>
    </section>

"""
    
    # 1. Problem / Hook ersetzen
    html = re.sub(r'    <!-- ==================== PROBLEM / HOOK ==================== -->.*?    <!-- ==================== LEISTUNGEN ==================== -->', 
                  warum_murix + r'    <!-- ==================== LEISTUNGEN ==================== -->', html, flags=re.DOTALL)
    
    # 2. Alte Vorteile löschen
    html = re.sub(r'    <!-- ==================== VORTEILE ==================== -->.*?    <!-- ==================== STATIC vs CMS ==================== -->', 
                  r'    <!-- ==================== STATIC vs CMS ==================== -->', html, flags=re.DOTALL)
                  
    # 3. Static vs CMS löschen
    html = re.sub(r'    <!-- ==================== STATIC vs CMS ==================== -->.*?    <!-- ==================== PROZESS ==================== -->', 
                  r'    <!-- ==================== PROZESS ==================== -->', html, flags=re.DOTALL)
                  
    # 4. Kundenstimmen -> Wall of Love
    html = html.replace('<span class="section-tag">Kundenstimmen</span>', '<span class="section-tag">Wall of Love</span>')
    
    # Write back
    with open('/home/ubuntu/Antigravity/Murix-Backup/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Refactoring complete.")

if __name__ == '__main__':
    refactor()
