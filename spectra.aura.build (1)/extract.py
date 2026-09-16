import re
from bs4 import BeautifulSoup

with open('/Users/macintosh/Desktop/Esteticmel/spectra.aura.build (1)/index.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

head = soup.head
# We want to extract the Hero section. It seems to be the first <section> inside the main content.
# Also the <header> for the nav.

nav = soup.find('header')
hero = soup.find('section')

# We can print out the string representation
with open('/Users/macintosh/Desktop/Esteticmel/spectra.aura.build (1)/design-system.html', 'w') as out:
    out.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
    out.write(''.join(str(c) for c in head.contents))
    out.write('\n<style>\n')
    out.write('.ds-nav { position: fixed; top: 0; left: 0; right: 0; background: rgba(10,24,20,0.9); backdrop-filter: blur(10px); padding: 15px; z-index: 9999; display: flex; gap: 20px; justify-content: center; border-bottom: 1px solid rgba(255,255,255,0.1); }\n')
    out.write('.ds-nav a { color: #fff; text-decoration: none; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }\n')
    out.write('.ds-section { padding: 100px 20px; border-bottom: 1px solid rgba(255,255,255,0.05); }\n')
    out.write('.ds-header { margin-bottom: 40px; text-align: center; color: #fff; }\n')
    out.write('.ds-preview { padding: 40px; background: rgba(255,255,255,0.02); border-radius: 16px; border: 1px dashed rgba(255,255,255,0.1); margin-bottom: 20px; }\n')
    out.write('</style>\n</head>\n')
    out.write('<body class="antialiased text-forest-950 selection:bg-emerald-200 selection:text-emerald-900 bg-forest-50 overflow-x-hidden">\n')
    
    # Nav
    out.write('<nav class="ds-nav">\n')
    out.write('<a href="#hero">0. Hero</a>\n')
    out.write('<a href="#typography">1. Typography</a>\n')
    out.write('<a href="#colors">2. Colors & Surfaces</a>\n')
    out.write('<a href="#components">3. Components</a>\n')
    out.write('<a href="#layout">4. Layout & Spacing</a>\n')
    out.write('<a href="#motion">5. Motion</a>\n')
    out.write('<a href="#icons">6. Icons</a>\n')
    out.write('</nav>\n')
    
    # Hero Clone
    out.write('<div id="hero" style="position:relative; margin-top: 60px;">\n')
    # Change text in hero
    hero_str = str(hero)
    hero_str = hero_str.replace('VISION</span>', 'DESIGN</span>')
    hero_str = hero_str.replace('BEYOND</span>', 'SYSTEM</span>')
    hero_str = hero_str.replace('REALITY</span>', 'V2.0</span>')
    hero_str = hero_str.replace('Seamlessly blending digital information', 'A living pattern library for the Spectra AR')
    
    # Include background elements that were outside the section
    bg_elements = soup.find_all('div', class_=re.compile(r'fixed top-0 right-0'))
    for bg in bg_elements:
        out.write(str(bg))
    
    out.write(hero_str)
    out.write('</div>\n')

    # Add other sections (typography, etc.) - we can append this via another tool call or string replacement
    out.write('</body></html>')

