import re

with open('oferta-semana-do-cliente/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Topbar and Hero Start
new_hero_start = """
<nav class="topbar">
  <div class="wrap topbar-wrap">
    <div class="topbar-logo-area">
      <img src="logo.png" alt="Esteticmel" class="topbar-logo">
      <div class="topbar-text">
        <b>SEMANA DO CLIENTE</b>
        <span>15 a 25 de setembro &bull; de R$ 220 por R$ 120</span>
      </div>
    </div>
    <div class="topbar-timer" id="topbar-timer">
      <div class="timer-box"><b data-d>00</b><span>DIAS</span></div>
      <div class="timer-box"><b data-h>00</b><span>HORAS</span></div>
      <div class="timer-box"><b data-m>00</b><span>MIN</span></div>
      <div class="timer-box"><b data-s>00</b><span>SEG</span></div>
    </div>
    <a class="btn btn-claro btn-pequeno" href="https://wa.me/5571997110471?text=Ol%C3%A1%21%20Quero%20aproveitar%20a%20Semana%20do%20Cliente%20%2815%20a%2025/09%29%20e%20garantir%20minha%20sess%C3%A3o%20de%20Detox%20Corporal%20por%20R%24%20120.%20Vim%20pelo%20site." target="_blank" rel="noopener">Garantir vaga &rarr;</a>
  </div>
</nav>

<header class="hero">
  <div class="hero-bg">
    <div class="hero-foto rev rev-zoom d3">
"""
content = re.sub(r'<header class="hero">.*?<div class="hero-foto rev rev-zoom d3">', new_hero_start, content, flags=re.DOTALL)

# 2. Hero End
new_hero_end = """
    </div>
  </div>
  <div class="wrap hero-wrap">
    <div class="hero-content">
      <div class="pilula-hero rev d1">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 4 13V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v7a7 7 0 0 1-7 7Z"/><path d="M8 12h8"/></svg>
        <span>OFERTA VÁLIDA DE 15 A 25 DE SETEMBRO &bull; APENAS 20 VAGAS</span>
      </div>
      <h1 class="rev d1">Desinchar, desinflamar e recuperar sua disposição.</h1>
      <p class="hero-sub rev d2">O Detox Corporal da Esteticmel une drenagem metabólica integrativa e ativos ortomoleculares para devolver leveza ao seu corpo em uma única sessão.</p>
      
      <div class="hero-price-card rev d3">
        <div class="hpc-left">
           <span>De R$ 220 por apenas</span>
           <b>R$ 120</b>
        </div>
        <div class="hpc-right">
           <span>Economia imediata de R$ 100</span>
        </div>
      </div>
      
      <a class="btn btn-hero rev d4" href="https://wa.me/5571997110471?text=Ol%C3%A1%21%20Quero%20aproveitar%20a%20Semana%20do%20Cliente%20%2815%20a%2025/09%29%20e%20garantir%20minha%20sess%C3%A3o%20de%20Detox%20Corporal%20por%20R%24%20120.%20Vim%20pelo%20site." target="_blank" rel="noopener">GARANTIR MEU DETOX POR R$ 120 NO WHATSAPP &rarr;</a>
      <p class="hero-nota rev d4">Garanto o valor promocional agora e escolha a melhor data para o atendimento.</p>
    </div>
  </div>
</header>
"""
content = re.sub(r'    </div>\n    <div class="pilula rev d3">.*?</header>', new_hero_end, content, flags=re.DOTALL)

# 3. Final Section
final_start = content.find('<section class="final">')
final_end = content.find('</section>', final_start) + 10
new_final = """
<section class="final">
  <div class="wrap final-wrap-center">
    <div class="final-icon rev">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>
    </div>
    <h2 class="rev">Não deixe para cuidar de você quando o corpo travar.</h2>
    <p class="final-sub rev d1">Uma hora de cuidado clínico agora vale mais do que semanas de cansaço acumulado.</p>
    
    <div class="final-card-center rev d2">
      <p>De R$ 220 por apenas</p>
      <b>R$ 120</b>
      <span>ATÉ 25 DE SETEMBRO</span>
    </div>
    
    <a class="btn btn-final-cta rev d3" href="https://wa.me/5571997110471?text=Ol%C3%A1%21%20Quero%20aproveitar%20a%20Semana%20do%20Cliente%20%2815%20a%2025/09%29%20e%20garantir%20minha%20sess%C3%A3o%20de%20Detox%20Corporal%20por%20R%24%20120.%20Vim%20pelo%20site." target="_blank" rel="noopener">QUERO MEU DETOX CORPORAL POR R$ 120 &rarr;</a>
    
    <div class="final-icon-row rev d3">
      <div><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg> Apenas 20 vagas</div>
      <div><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Salvador, BA</div>
      <div><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> Sessão de 1 Hora</div>
    </div>
  </div>
</section>
"""
content = content[:final_start] + new_final + content[final_end:]

# 4. Footer Section
footer_start = content.find('<footer class="rodape">')
footer_end = content.find('</footer>', footer_start) + 9
new_footer = """
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
content = content[:footer_start] + new_footer + content[footer_end:]

# 5. Fix Javascript countdown targeting
# We need to target #topbar-timer instead of .cartao .caixa-tempo
content = content.replace('var cels = document.getElementById("r2")', 'var cels = document.getElementById("r2") || document.getElementById("topbar-timer")')

with open('oferta-semana-do-cliente/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
