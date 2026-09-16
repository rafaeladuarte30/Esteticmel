css = """
/* NEW DESKTOP STYLES (Added by agent) */
.topbar { display: none; }
.desktop-rodape { display: none; }
.final-card-center, .final-icon-row { display: none; }
.hero-bg, .hero-wrap, .pilula-hero, .hero-price-card, .btn-hero, .hero-nota { display: none; }

@media (min-width: 760px) {
  /* Topbar */
  .topbar {
    display: block;
    position: absolute;
    top: 0; left: 0; right: 0;
    z-index: 100;
    border-bottom: 1px solid rgba(255,255,255,0.1);
  }
  .topbar-wrap {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 72px;
  }
  .topbar-logo-area { display: flex; align-items: center; gap: 20px; }
  .topbar-logo { height: 32px; filter: brightness(0) invert(1); }
  .topbar-text { color: #fff; font-size: 13px; line-height: 1.2; }
  .topbar-text b { display: block; letter-spacing: 0.1em; }
  .topbar-text span { color: rgba(255,255,255,0.7); font-size: 12px; }
  .topbar-timer { display: flex; gap: 8px; }
  .timer-box {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(4px);
    border-radius: 6px;
    padding: 6px 12px;
    color: #fff;
    text-align: center;
    line-height: 1.1;
  }
  .timer-box b { display: block; font-size: 18px; font-weight: 700; }
  .timer-box span { font-size: 9px; font-weight: 600; letter-spacing: 0.05em; }
  .btn-pequeno { padding: 10px 20px; font-size: 14px; }
  
  /* Hero */
  .hero {
    position: relative;
    min-height: 100vh;
    padding: 0;
    display: flex;
    align-items: center;
    background: #2E4A12;
    overflow: hidden;
  }
  .hero-bg { display: block; position: absolute; top: 0; left: 0; right: 0; bottom: 0; z-index: 1; }
  .hero-bg::after {
    content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(to right, #2E4A12 35%, rgba(46,74,18,0.2) 100%);
  }
  .hero-foto { height: 100%; width: 100%; border-radius: 0; margin: 0; box-shadow: none; position: absolute; right: 0; width: 60%; transform: none; }
  .hero-wrap { display: flex; position: relative; z-index: 2; width: min(1100px, 100% - 60px); }
  .hero-content { width: 55%; text-align: left; padding-top: 40px; }
  
  .pilula-hero {
    display: inline-flex; align-items: center; gap: 8px;
    border: 1px solid rgba(255,255,255,0.3); border-radius: 999px;
    padding: 6px 16px; color: #fff; font-size: 12px; font-weight: 600; letter-spacing: 0.05em;
    margin-bottom: 24px;
  }
  .hero-content h1 { font-size: clamp(2.8rem, 4.2vw, 4.5rem); margin-bottom: 20px; line-height: 1.1; max-width: 15ch; text-transform: none; }
  .hero-content .hero-sub { max-width: 46ch; font-size: 18px; color: rgba(255,255,255,0.8); margin-bottom: 40px; }
  
  .hero-price-card {
    display: inline-flex; align-items: center; gap: 24px;
    border-left: 2px solid var(--verde-claro); padding-left: 20px; margin-bottom: 32px;
  }
  .hpc-left span { display: block; color: rgba(255,255,255,0.7); font-size: 13px; margin-bottom: 4px; }
  .hpc-left b { display: block; color: #fff; font-size: 42px; font-weight: 700; line-height: 1; }
  .hpc-right span { display: block; color: rgba(255,255,255,0.6); font-size: 14px; font-weight: 600; }
  
  .btn-hero { width: auto; display: inline-flex; padding: 20px 32px; font-size: 16px; }
  .hero-nota { display: block; font-size: 13px; color: rgba(255,255,255,0.6); margin-top: 16px; }

  /* Final Section */
  .final { padding: 100px 0 60px; }
  .final-wrap-center { display: flex; flex-direction: column; align-items: center; text-align: center; }
  .final-icon {
    width: 64px; height: 64px; border-radius: 50%; background: rgba(255,255,255,0.1);
    display: flex; align-items: center; justify-content: center; color: #fff; margin-bottom: 24px;
  }
  .final-wrap-center h2 { text-align: center; max-width: 25ch; text-transform: none; }
  .final-wrap-center .final-sub { text-align: center; max-width: 48ch; margin: 20px auto 40px; font-size: 18px; }
  .final-card-center {
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    background: #3B5D1A; border-radius: 20px; padding: 32px 64px; margin-bottom: 32px;
    border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 20px 40px rgba(0,0,0,0.2);
  }
  .final-card-center p { color: rgba(255,255,255,0.8); font-size: 14px; margin-bottom: 8px; }
  .final-card-center b { color: #fff; font-size: 56px; font-weight: 700; line-height: 1; margin-bottom: 12px; }
  .final-card-center span { color: rgba(255,255,255,0.6); font-size: 12px; letter-spacing: 0.1em; font-weight: 600; text-transform: uppercase;}
  
  .btn-final-cta { font-size: 18px; padding: 20px 40px; width: auto; background: #86A84F; color: #fff; }
  .btn-final-cta:hover { background: #96BD58; }
  
  .final-icon-row { display: flex; gap: 40px; margin-top: 32px; color: rgba(255,255,255,0.7); font-size: 14px; }
  .final-icon-row div { display: flex; align-items: center; gap: 8px; }
  
  /* Footer */
  .desktop-rodape { display: block; border-top: 1px solid rgba(255,255,255,0.1); padding: 32px 0; background: #2E4A12; }
  .rodape-flex { display: flex; justify-content: space-between; align-items: center; }
  .rodape-logo-small { height: 28px; filter: brightness(0) invert(1); opacity: 0.8; }
  .rodape-fim { margin: 0; color: rgba(255,255,255,0.5); font-size: 13px; }
  .rodape-icons { display: flex; gap: 16px; color: rgba(255,255,255,0.5); }
}
</style>"""

with open('oferta-semana-do-cliente/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('</style>', css)

with open('oferta-semana-do-cliente/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
