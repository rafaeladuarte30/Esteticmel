import re

with open('oferta-semana-do-cliente/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need a mobile footer and a desktop footer
# Currently we just have:
# <footer class="rodape desktop-rodape">
# Let's restore the mobile footer and keep the desktop one

mobile_footer = """
<footer class="rodape mobile-rodape">
  <div class="wrap">
    <img src="logo.png" alt="Esteticmel" class="hero-logo rev d1" style="display:block; margin: 0 auto 24px;">
    <div class="unidades">
      <div class="unidade rev d1">
        <svg viewBox="0 0 24 24"><path d="M12 21s7-5.7 7-11a7 7 0 1 0-14 0c0 5.3 7 11 7 11Z" stroke-linejoin="round"/><circle cx="12" cy="10" r="2.6"/></svg>
        <div><b>Stella Maris</b><span>Salvador, BA &middot; atendimento com hora marcada</span></div>
      </div>
      <div class="unidade rev d2">
        <svg viewBox="0 0 24 24"><path d="M12 21s7-5.7 7-11a7 7 0 1 0-14 0c0 5.3 7 11 7 11Z" stroke-linejoin="round"/><circle cx="12" cy="10" r="2.6"/></svg>
        <div><b>Caminho das Árvores</b><span>Salvador, BA &middot; atendimento com hora marcada</span></div>
      </div>
    </div>
    <p class="rodape-fim">Enfermagem estética &amp; saúde integrativa</p>
  </div>
</footer>
"""

# Let's see if we deleted the <div class="unidades"> when we replaced the final section.
# The final section originally ended, then there was <div class="unidades"> inside <section class="final">?
# NO, the original structure:
# <section class="final">
#   <div class="wrap">...</div>
# </section>
# <footer class="rodape">
#   <div class="wrap">
#     <img src="logo.png">
#     <div class="unidades">...</div>
#     <p class="rodape-fim">...</p>
#   </div>
# </footer>

# Let's completely replace the current footer with both mobile and desktop versions
new_footers = mobile_footer + """
<footer class="rodape desktop-rodape">
  <div class="wrap rodape-flex">
    <img src="logo.png" alt="Esteticmel" class="rodape-logo-small">
    <p class="rodape-fim">Enfermagem Estética & Saúde Integrativa - Salvador, BA</p>
    <div class="rodape-icons">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m16 5-3.5 3.5"/><path d="M8 20v-3a4 4 0 0 1 8 0v3"/><path d="M12 2v2"/><path d="m8 5 3.5 3.5"/><path d="M2 12h2"/><path d="M20 12h2"/></svg>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
    </div>
  </div>
</footer>
"""

content = re.sub(r'<footer class="rodape desktop-rodape">.*?</footer>', new_footers, content, flags=re.DOTALL)

# Add CSS for .mobile-rodape
css_add = """
.desktop-rodape { display: none; }
@media (min-width: 760px) {
  .mobile-rodape { display: none; }
  .desktop-rodape { display: block; border-top: 1px solid rgba(255,255,255,0.1); padding: 32px 0; background: #2E4A12; }
}
"""
content = content.replace('/* NEW DESKTOP STYLES (Added by agent) */', '/* NEW DESKTOP STYLES (Added by agent) */\n' + css_add)

with open('oferta-semana-do-cliente/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
