import re

with open('oferta-semana-do-cliente/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Sintomas Desktop
# The original is: <section class="escuro"> ... </section>
sintomas_desktop = """
<section class="sintomas-desktop">
  <div class="wrap">
    <div class="sintomas-header">
      <p class="olho">VOCÊ SENTE ISSO NO CORPO?</p>
      <h2>O corpo avisa quando atinge o limite do cansaço.</h2>
    </div>
    
    <div class="sintomas-grid">
      <!-- Card 1 -->
      <div class="sintomas-card">
        <div class="sc-top">
          <div class="sc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.38 3.46 16 2a8.86 8.86 0 0 1-3.9 1.39 8.86 8.86 0 0 1-3.9-1.39L3.82 3.46A2 2 0 0 0 2 5.37V20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V5.37a2 2 0 0 0-1.62-1.91Z"/><path d="M12 2v6"/><path d="M2 13h20"/></svg></div>
          <div class="sc-num">01</div>
        </div>
        <b>Sensação de inchaço pesado</b>
        <p>Roupas apertando e abdômen estufado logo ao acordar ou ao fim do dia.</p>
      </div>
      <!-- Card 2 -->
      <div class="sintomas-card">
        <div class="sc-top">
          <div class="sc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 17c1.7 0 3-1.3 3-3s-1.3-3-3-3-3 1.3-3 3 1.3 3 3 3Z"/><path d="M9.5 14c1.7 0 3-1.3 3-3S11.2 8 9.5 8 6.5 9.3 6.5 11s1.3 3 3 3Z"/><path d="M12 2v6"/><path d="M5 22v-3"/><path d="M19 22v-3"/></svg></div>
          <div class="sc-num">02</div>
        </div>
        <b>Pernas cansadas e doloridas</b>
        <p>Retenção visível e má circulação pela rotina intensa.</p>
      </div>
      <!-- Card 3 -->
      <div class="sintomas-card">
        <div class="sc-top">
          <div class="sc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m16 8-4 4"/></svg></div>
          <div class="sc-num">03</div>
        </div>
        <b>Metabolismo travado</b>
        <p>Sensação de inflamação que água e exercícios sozinhos não aliviam rápido.</p>
      </div>
      <!-- Card 4 -->
      <div class="sintomas-card">
        <div class="sc-top">
          <div class="sc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div>
          <div class="sc-num">04</div>
        </div>
        <b>Estresse tecidual</b>
        <p>Nódulos de tensão e falta de vitalidade na pele.</p>
      </div>
    </div>
  </div>
</section>
"""
# Insert right after </section> of <section class="escuro">
escuro_end = content.find('</section>', content.find('<section class="escuro">')) + 10
content = content[:escuro_end] + "\n" + sintomas_desktop + content[escuro_end:]


# 2. Passos Desktop
# First, extract images from <div class="passos">
passos_html = re.search(r'<div class="passos">(.*?)<p class="nota rev">', content, re.DOTALL).group(1)
images = re.findall(r'<img src="(data:image/jpeg;base64,.*?)"', passos_html)

passos_desktop = f"""
<section class="passos-desktop">
  <div class="wrap">
    <div class="passos-grid">
      <!-- Passo 1 -->
      <div class="passo-card">
        <div class="pc-img">
          <img src="{images[0]}">
          <div class="pc-num">1</div>
        </div>
        <div class="pc-text">
          <b>Avaliação Clínica Integrativa</b>
          <p>Análise rápida de áreas críticas de retenção e inflamação tecidual.</p>
        </div>
      </div>
      <!-- Passo 2 -->
      <div class="passo-card">
        <div class="pc-img">
          <img src="{images[1]}">
          <div class="pc-num">2</div>
        </div>
        <div class="pc-text">
          <b>Drenagem Linfática Metabólica</b>
          <p>Desobstrução do fluxo linfático com foco em alívio e contorno corporal.</p>
        </div>
      </div>
      <!-- Passo 3 -->
      <div class="passo-card">
        <div class="pc-img">
          <img src="{images[2]}">
          <div class="pc-num">3</div>
        </div>
        <div class="pc-text">
          <b>Ativos Ortomoleculares</b>
          <p>Uso de cremes com princípios ativos potentes que penetram na pele e potencializam a desinflamação.</p>
        </div>
      </div>
      <!-- Passo 4 -->
      <div class="passo-card">
        <div class="pc-img">
          <img src="{images[3]}">
          <div class="pc-num">4</div>
        </div>
        <div class="pc-text">
          <b>Liberação de Tensões</b>
          <p>Toques estratégicos para soltar a musculatura contraída e trazer alívio imediato.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

# Insert right after the section containing "Sua sessão, passo a passo"
passos_sec_start = content.find('<p class="olho rev">Sua sessão, passo a passo</p>')
passos_sec_start = content.rfind('<section', 0, passos_sec_start)
passos_sec_end = content.find('</section>', passos_sec_start) + 10
content = content[:passos_sec_end] + "\n" + passos_desktop + content[passos_sec_end:]

# 3. Autora Desktop
autora_html = re.search(r'<div class="autora-foto">(.*?)</div>', content, re.DOTALL).group(1)
autora_img = re.search(r'<img src="(data:image/jpeg;base64,.*?)"', autora_html).group(1)

autora_desktop = f"""
<section class="autora-desktop">
  <div class="wrap ad-wrap">
    <div class="ad-left">
      <img src="{autora_img}">
      <div class="ad-tag">ESMERALDA SALES</div>
    </div>
    <div class="ad-right">
      <p class="olho">QUEM VAI TE ATENDER</p>
      <h2>Segurança, rigor técnico e saúde integrativa.</h2>
      <blockquote>
        "Sou a Esmeralda Sales, enfermeira e terapeuta ortomolecular integrativa.<br><br>
        Na Esteticmel, cada procedimento é feito com olhar individualizado. Meu compromisso não é apenas com a estética externa, mas com o equilíbrio do seu terreno biológico para que o alívio seja real e sustentável."
      </blockquote>
      <div class="ad-check">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
        Atendimento individualizado e responsável
      </div>
    </div>
  </div>
</section>
"""

painel_start = content.find('<p class="olho rev">Quem vai te atender</p>')
painel_start = content.rfind('<section', 0, painel_start)
painel_end = content.find('</section>', painel_start) + 10
content = content[:painel_end] + "\n" + autora_desktop + content[painel_end:]


# 4. Inject CSS
css_add = """
/* Desktop Exclusive Sections */
.sintomas-desktop, .passos-desktop, .autora-desktop { display: none; }

@media (min-width: 760px) {
  .sintomas-desktop, .passos-desktop, .autora-desktop { display: block; }
  
  /* Hide mobile sections */
  .escuro { display: none; }
  section:has(.passos) { display: none; } /* Mobile passos section */
  .painel:has(.autora) { display: none; } /* Mobile autora section */
  
  /* Sintomas Desktop */
  .sintomas-desktop { background: #fff; padding: 100px 0; }
  .sintomas-header { margin-bottom: 48px; }
  .sintomas-header .olho { color: #86A84F; font-weight: 700; font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px; }
  .sintomas-header h2 { color: #2E4A12; font-size: 36px; max-width: 20ch; line-height: 1.1; }
  
  .sintomas-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
  .sintomas-card { background: #E9F5D9; border-radius: 16px; padding: 32px 24px; color: #2E4A12; }
  .sc-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 32px; }
  .sc-icon { width: 48px; height: 48px; background: #3B5D1A; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #fff; }
  .sc-icon svg { width: 24px; height: 24px; }
  .sc-num { font-size: 24px; font-weight: 700; color: #86A84F; }
  .sintomas-card b { display: block; font-size: 18px; margin-bottom: 16px; line-height: 1.2; }
  .sintomas-card p { font-size: 14px; opacity: 0.8; line-height: 1.5; }
  
  /* Passos Desktop */
  .passos-desktop { background: #2E4A12; padding: 100px 0; }
  .passos-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 32px; }
  .passo-card { background: #3B5D1A; border-radius: 24px; overflow: hidden; display: flex; flex-direction: column; }
  .pc-img { position: relative; height: 320px; }
  .pc-img img { width: 100%; height: 100%; object-fit: cover; }
  .pc-num { position: absolute; top: 20px; left: 20px; width: 40px; height: 40px; background: #2E4A12; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 16px; }
  .pc-text { padding: 32px; color: #fff; }
  .pc-text b { display: block; font-size: 20px; margin-bottom: 8px; }
  .pc-text p { font-size: 14px; opacity: 0.8; line-height: 1.5; margin: 0; }
  
  /* Autora Desktop */
  .autora-desktop { background: #E9F5D9; padding: 100px 0; }
  .ad-wrap { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; }
  .ad-left { position: relative; border-radius: 24px; overflow: hidden; height: 600px; }
  .ad-left img { width: 100%; height: 100%; object-fit: cover; }
  .ad-tag { position: absolute; bottom: 20px; left: 20px; background: #2E4A12; color: #fff; padding: 8px 16px; font-size: 12px; font-weight: 700; letter-spacing: 0.1em; border-radius: 4px; }
  
  .ad-right .olho { color: #86A84F; font-weight: 700; font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 12px; }
  .ad-right h2 { color: #2E4A12; font-size: 40px; line-height: 1.1; margin-bottom: 40px; max-width: 15ch; }
  .ad-right blockquote { border-left: 4px solid #86A84F; padding-left: 24px; margin: 0 0 40px 0; color: #2E4A12; font-size: 16px; line-height: 1.6; opacity: 0.9; }
  .ad-check { display: flex; align-items: center; gap: 12px; color: #2E4A12; font-size: 14px; font-weight: 600; }
  .ad-check svg { width: 24px; height: 24px; color: #86A84F; }
}
"""
content = content.replace('/* NEW DESKTOP STYLES (Added by agent) */', '/* NEW DESKTOP STYLES (Added by agent) */\n' + css_add)

with open('oferta-semana-do-cliente/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
