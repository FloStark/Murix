import sys
import re

def refactor():
    with open('/home/ubuntu/Antigravity/Murix-Backup/index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    combined_section = """    <!-- ==================== PROBLEM & LÖSUNG (VORTEILE) ==================== -->
    <section class="section hook-section" id="problem">
        <div class="container">
            <div class="hook-grid">
                <div class="hook-text reveal">
                    <span class="section-tag">Ihre Herausforderung</span>
                    <h2 class="section-title">Schluss mit teuren Agenturen und IT-Chaos.</h2>
                    <p>Ihre Konkurrenz gewinnt Kunden über Google und arbeitet mit modernen Cloud-Tools. Und Sie ärgern sich über langsame Websites, Abo-Fallen oder unzuverlässige IT. Wir beenden das.</p>
                </div>
                <div class="hook-cards reveal" data-delay="200">
                    <div class="pain-card">
                        <div class="pain-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="1.5">
                                <line x1="12" y1="1" x2="12" y2="23" />
                                <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
                            </svg></div>
                        <h4>Faire Festpreise</h4>
                        <p>Keine teuren Knebelverträge oder Agentur-Abos. Sie zahlen einen fairen Einmalpreis für Ihre fertige Website – 100% Ihr Eigentum.</p>
                    </div>
                    <div class="pain-card">
                        <div class="pain-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="1.5">
                                <circle cx="11" cy="11" r="8" />
                                <line x1="21" y1="21" x2="16.65" y2="16.65" />
                            </svg></div>
                        <h4>Sichtbar bei Google</h4>
                        <p>Wir bauen SEO-optimierte, blitzschnelle Websites, die Kunden anziehen, während alte Websites in den Suchergebnissen verschwinden.</p>
                    </div>
                    <div class="pain-card">
                        <div class="pain-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="1.5">
                                <path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z" />
                            </svg></div>
                        <h4>IT, die funktioniert</h4>
                        <p>Schluss mit lokalen Servern. Wir modernisieren Ihr Unternehmen mit Microsoft 365, sicherer Cloud und professionellen E-Mails.</p>
                    </div>
                    <div class="pain-card solution">
                        <div class="pain-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="1.5">
                                <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
                            </svg></div>
                        <h4>Der Murix-Vorteil</h4>
                        <p>Ihr persönlicher IT-Betreuer aus Graz. Webdesign, SEO und Microsoft 365 Betreuung – alles zuverlässig aus einer Hand.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

"""
    
    # 1. Replace PROBLEM / HOOK 
    html = re.sub(r'    <!-- ==================== PROBLEM / HOOK ==================== -->.*?    <!-- ==================== LEISTUNGEN ==================== -->', 
                  combined_section + r'    <!-- ==================== LEISTUNGEN ==================== -->', html, flags=re.DOTALL)
    
    # 2. Delete VORTEILE section completely
    html = re.sub(r'    <!-- ==================== VORTEILE ==================== -->.*?    <!-- ==================== STATIC vs CMS ==================== -->', 
                  r'    <!-- ==================== STATIC vs CMS ==================== -->', html, flags=re.DOTALL)
                  
    # Write back
    with open('/home/ubuntu/Antigravity/Murix-Backup/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Refactoring complete.")

if __name__ == '__main__':
    refactor()
