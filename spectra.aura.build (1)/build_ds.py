import re
from bs4 import BeautifulSoup

# Read original html
with open('/Users/macintosh/Desktop/Esteticmel/spectra.aura.build (1)/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Get head
head = soup.head
body_classes = soup.body.get('class', [])
body_class_str = ' '.join(body_classes) if isinstance(body_classes, list) else body_classes

# Find the fixed backgrounds to preserve the look
bg_fixed = soup.find_all('div', class_=lambda c: c and 'fixed' in c and 'z-[-1]' in c)
bg_lines = soup.find_all('div', class_=lambda c: c and 'fixed' in c and 'pointer-events-none' in c and 'grid' in c)

# Find header (nav) and first section (hero)
header = soup.find('header', id='main-header')
hero_section = soup.find('section', class_=lambda c: c and 'min-h-screen' in c)

# Modify Hero text
if hero_section:
    # We will just replace strings in the str(hero_section)
    hero_str = str(hero_section)
    hero_str = hero_str.replace('VISION', 'DESIGN')
    hero_str = hero_str.replace('BEYOND', 'SYSTEM')
    hero_str = hero_str.replace('REALITY', 'V2.0')
    hero_str = hero_str.replace('Seamlessly blending digital information with your physical world.', 'Living pattern library for the Spectra AR interface.')
else:
    hero_str = ""

bg_str = ""
for b in bg_fixed:
    bg_str += str(b)
for b in bg_lines:
    bg_str += str(b)

# Construct Typography HTML
typo_html = """
<div id="typography" class="max-w-[1600px] mx-auto px-6 md:px-12 py-32 relative z-10 border-t border-white/10">
    <div class="mb-16">
        <h2 class="text-4xl md:text-5xl text-forest-50 font-dm-sans font-light tracking-tighter">Typography</h2>
    </div>
    
    <div class="flex flex-col gap-8 bg-forest-950/80 backdrop-blur-2xl border border-white/10 rounded-[2rem] p-8 shadow-2xl">
        <div class="flex flex-col md:flex-row justify-between md:items-center border-b border-white/10 pb-6 gap-4">
            <div>
                <h1 class="leading-[0.9] text-forest-50 md:text-7xl xl:text-8xl text-5xl tracking-tighter">
                    <span class="block tracking-tighter font-dm-sans font-light">HEADING 1</span>
                </h1>
            </div>
            <div class="text-right text-forest-400 font-mono text-sm">text-7xl / 8xl / font-dm-sans</div>
        </div>
        
        <div class="flex flex-col md:flex-row justify-between md:items-center border-b border-white/10 pb-6 gap-4">
            <div>
                <h2 class="text-4xl md:text-5xl text-forest-50 leading-tight tracking-tighter font-dm-sans font-light">
                    Heading 2 <span class="text-emerald-500">Accent</span>
                </h2>
            </div>
            <div class="text-right text-forest-400 font-mono text-sm">text-4xl / 5xl / font-dm-sans</div>
        </div>

        <div class="flex flex-col md:flex-row justify-between md:items-center border-b border-white/10 pb-6 gap-4">
            <div>
                <h3 class="text-xl text-forest-100 font-semibold tracking-tight font-sans">
                    Heading 3 / Card Title
                </h3>
            </div>
            <div class="text-right text-forest-400 font-mono text-sm">text-xl / font-semibold / font-sans</div>
        </div>

        <div class="flex flex-col md:flex-row justify-between md:items-center border-b border-white/10 pb-6 gap-4">
            <div>
                <p class="max-w-md text-forest-300 text-sm md:text-base leading-relaxed font-sans">
                    Paragraph (Regular). Seamlessly blending digital information with your physical world.
                </p>
            </div>
            <div class="text-right text-forest-400 font-mono text-sm">text-sm / base / text-forest-300</div>
        </div>
        
        <div class="flex flex-col md:flex-row justify-between md:items-center border-b border-white/10 pb-6 gap-4">
            <div>
                <span class="text-xs font-medium uppercase tracking-widest text-forest-400 font-sans">Sublabel / Eyebrow</span>
            </div>
            <div class="text-right text-forest-400 font-mono text-sm">text-xs / uppercase / tracking-widest</div>
        </div>
    </div>
</div>
"""

# Construct Colors HTML
colors_html = """
<div id="colors" class="max-w-[1600px] mx-auto px-6 md:px-12 py-32 relative z-10 border-t border-white/10">
    <div class="mb-16">
        <h2 class="text-4xl md:text-5xl text-forest-50 font-dm-sans font-light tracking-tighter">Colors & Surfaces</h2>
    </div>
    
    <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mb-12">
        <div class="p-6 rounded-2xl bg-forest-950 border border-white/10 shadow-lg">
            <div class="w-full h-16 bg-forest-950 rounded-lg mb-4 border border-white/10"></div>
            <div class="text-white font-mono text-sm">bg-forest-950</div>
        </div>
        <div class="p-6 rounded-2xl bg-forest-900 border border-white/10 shadow-lg">
            <div class="w-full h-16 bg-forest-900 rounded-lg mb-4 border border-white/10"></div>
            <div class="text-white font-mono text-sm">bg-forest-900</div>
        </div>
        <div class="p-6 rounded-2xl bg-forest-800 border border-white/10 shadow-lg">
            <div class="w-full h-16 bg-forest-800 rounded-lg mb-4 border border-white/10"></div>
            <div class="text-white font-mono text-sm">bg-forest-800</div>
        </div>
        <div class="p-6 rounded-2xl bg-forest-50 border border-forest-200 shadow-lg">
            <div class="w-full h-16 bg-forest-50 rounded-lg mb-4 border border-forest-200"></div>
            <div class="text-forest-950 font-mono text-sm">bg-forest-50</div>
        </div>
        <div class="p-6 rounded-2xl bg-emerald-500 border border-white/10 shadow-lg">
            <div class="w-full h-16 bg-emerald-500 rounded-lg mb-4 border border-white/10"></div>
            <div class="text-white font-mono text-sm">bg-emerald-500</div>
        </div>
        <div class="p-6 rounded-2xl bg-emerald-400 border border-white/10 shadow-lg">
            <div class="w-full h-16 bg-emerald-400 rounded-lg mb-4 border border-white/10"></div>
            <div class="text-white font-mono text-sm">bg-emerald-400</div>
        </div>
    </div>
    
    <h3 class="text-xl text-forest-100 font-semibold mb-6">Surfaces</h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="bg-forest-950/80 backdrop-blur-2xl border border-white/10 rounded-[2rem] p-8 shadow-2xl relative overflow-hidden group">
            <h4 class="text-white text-lg mb-2">Dark Glass Panel</h4>
            <p class="text-forest-300 text-sm font-mono">bg-forest-950/80 backdrop-blur-2xl border border-white/10 rounded-[2rem] shadow-2xl</p>
        </div>
        <div class="bg-forest-900/20 rounded-3xl border border-white/5 p-8 relative overflow-hidden group">
            <h4 class="text-white text-lg mb-2">Subtle Dark Card</h4>
            <p class="text-forest-300 text-sm font-mono">bg-forest-900/20 rounded-3xl border border-white/5</p>
        </div>
        <div class="bg-white/60 backdrop-blur-md rounded-[2rem] shadow-2xl shadow-forest-900/5 p-8 border border-white/40 relative">
            <h4 class="text-forest-950 text-lg mb-2">Light Glass Card</h4>
            <p class="text-forest-700 text-sm font-mono">bg-white/60 backdrop-blur-md border-white/40 shadow-2xl</p>
        </div>
    </div>
</div>
"""

# Construct Components HTML
components_html = """
<div id="components" class="max-w-[1600px] mx-auto px-6 md:px-12 py-32 relative z-10 border-t border-white/10">
    <div class="mb-16">
        <h2 class="text-4xl md:text-5xl text-forest-50 font-dm-sans font-light tracking-tighter">UI Components</h2>
    </div>
    
    <div class="grid grid-cols-1 gap-12 bg-forest-950/80 backdrop-blur-2xl border border-white/10 rounded-[2rem] p-8 shadow-2xl">
        
        <div>
            <h3 class="text-xl text-forest-100 font-semibold mb-6">Primary Action Button</h3>
            <div class="flex flex-wrap gap-8 items-center">
                <div>
                    <button class="group shadow-emerald-500/30 hover:shadow-emerald-500/50 transition-all duration-300 overflow-hidden font-medium text-emerald-950 bg-gradient-to-r from-[#d1fae5] to-[#34d399] rounded-xl pt-4 pr-8 pb-4 pl-8 relative shadow-lg" style="box-shadow:0 15px 33px -12px rgba(16, 185, 129, 0.9), inset 0 4px 6.3px rgba(209, 250, 229, 1), inset 0 -5px 6.3px rgba(5, 150, 105, 1); border-radius:9999px">
                        <div class="group-hover:translate-y-0 transition-transform duration-300 bg-white/20 absolute top-0 right-0 bottom-0 left-0 translate-y-full"></div>
                        <span class="relative flex items-center gap-2 font-sans">
                            Primary Button
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-send w-4 h-4"><path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"></path><path d="m21.854 2.147-10.94 10.939"></path></svg>
                        </span>
                    </button>
                    <p class="text-forest-400 font-mono text-xs mt-4 text-center">Default / Hover State</p>
                </div>
            </div>
        </div>

        <div>
            <h3 class="text-xl text-forest-100 font-semibold mb-6">Secondary Button (Dark BG)</h3>
            <div class="flex flex-wrap gap-8 items-center bg-forest-900 p-8 rounded-2xl border border-white/5">
                <div>
                    <button class="hover:bg-emerald-50 hover:text-emerald-700 transition-all flex text-sm font-medium text-emerald-700 bg-slate-50/50 rounded-full pt-3 pr-6 pb-3 pl-6 shadow-[0px_0px_0px_1px_rgba(0,0,0,0.06),0px_1px_1px_-0.5px_rgba(0,0,0,0.06),0px_3px_3px_-1.5px_rgba(0,0,0,0.06),_0px_6px_6px_-3px_rgba(0,0,0,0.06),0px_12px_12px_-6px_rgba(0,0,0,0.06),0px_24px_24px_-12px_rgba(0,0,0,0.06)] gap-x-2 gap-y-2 items-center" style="box-shadow: 0 18px 35px rgba(6, 78, 59, 0.25), 0 0 0 1px rgba(16, 185, 129, 0.2); color: #065f46; position: relative; --border-gradient: linear-gradient(180deg, rgba(255, 255, 255, 0.8), rgba(16, 185, 129, 0.2), rgba(255, 255, 255, 0.8)); --border-radius-before: 9999px">
                      <span class="text-sm font-medium text-emerald-900/70 tracking-tight font-sans">
                        Secondary Button
                      </span>
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="w-[16px] h-[16px]"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                    </button>
                    <p class="text-forest-400 font-mono text-xs mt-4 text-center">Default / Hover State</p>
                </div>
            </div>
        </div>

        <div>
            <h3 class="text-xl text-forest-100 font-semibold mb-6">Badges & Tags</h3>
            <div class="flex flex-wrap gap-4 items-center">
                <span class="text-xs font-mono font-bold tracking-widest text-emerald-400 bg-emerald-900/30 px-2 py-0.5 rounded font-sans">02</span>
                <span class="text-xs font-mono font-bold text-forest-400 bg-forest-50 px-2 py-1 rounded font-sans">02 // SYSTEM ACTIVE</span>
            </div>
        </div>
        
    </div>
</div>
"""

# Construct Layout HTML
layout_html = """
<div id="layout" class="max-w-[1600px] mx-auto px-6 md:px-12 py-32 relative z-10 border-t border-white/10">
    <div class="mb-16">
        <h2 class="text-4xl md:text-5xl text-forest-50 font-dm-sans font-light tracking-tighter">Layout & Spacing</h2>
    </div>
    
    <h3 class="text-xl text-forest-100 font-semibold mb-6">3-Column Grid Pattern (grid-cols-1 md:grid-cols-3 gap-8)</h3>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="p-8 bg-forest-900/20 rounded-3xl border border-white/5 flex items-center justify-center h-48">
            <span class="text-forest-400 font-mono">col-span-1</span>
        </div>
        <div class="p-8 bg-forest-900/20 rounded-3xl border border-white/5 flex items-center justify-center h-48">
            <span class="text-forest-400 font-mono">col-span-1</span>
        </div>
        <div class="p-8 bg-forest-900/20 rounded-3xl border border-white/5 flex items-center justify-center h-48">
            <span class="text-forest-400 font-mono">col-span-1</span>
        </div>
    </div>
    
    <h3 class="text-xl text-forest-100 font-semibold mb-6 mt-16">Asymmetric Split Pattern (lg:grid-cols-12)</h3>
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <div class="lg:col-span-4 p-8 bg-forest-950/80 backdrop-blur-2xl border border-white/10 rounded-[2rem] flex items-center justify-center h-64">
             <span class="text-forest-400 font-mono">lg:col-span-4</span>
        </div>
        <div class="hidden lg:block lg:col-span-2"></div>
        <div class="lg:col-span-6 p-8 bg-forest-950/80 backdrop-blur-2xl border border-white/10 rounded-[2rem] flex items-center justify-center h-64">
             <span class="text-forest-400 font-mono">lg:col-span-6</span>
        </div>
    </div>
</div>
"""

# Construct Motion HTML
motion_html = """
<div id="motion" class="max-w-[1600px] mx-auto px-6 md:px-12 py-32 relative z-10 border-t border-white/10">
    <div class="mb-16">
        <h2 class="text-4xl md:text-5xl text-forest-50 font-dm-sans font-light tracking-tighter">Motion & Interaction</h2>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="p-8 bg-forest-900/20 rounded-3xl border border-white/5 flex flex-col items-center justify-center group hover:border-emerald-500/30 hover:bg-forest-900/40 transition-all duration-500 cursor-pointer">
            <div class="w-12 h-12 bg-white/5 rounded-full flex items-center justify-center mb-4 group-hover:bg-emerald-500/20 group-hover:text-emerald-400 transition-colors duration-300 text-forest-200">
                <iconify-icon icon="lucide:arrow-right" width="24"></iconify-icon>
            </div>
            <h4 class="text-white mb-2">Group Hover Transitions</h4>
            <p class="text-forest-400 text-sm font-mono text-center">group-hover:bg-emerald-500/20 <br> group-hover:text-emerald-400</p>
        </div>
        
        <div class="p-8 bg-forest-900/20 rounded-3xl border border-white/5 flex flex-col items-center justify-center overflow-hidden group">
            <div class="w-full h-32 relative overflow-hidden rounded-xl mb-4">
                <img src="https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/936684c5-c133-46f6-b75b-466ea6d602bd_1600w.webp" class="transform group-hover:scale-105 transition-transform duration-700 w-full h-full object-cover">
            </div>
            <h4 class="text-white mb-2">Image Scale</h4>
            <p class="text-forest-400 text-sm font-mono text-center">group-hover:scale-105 <br> duration-700</p>
        </div>
        
        <div class="p-8 bg-forest-900/20 rounded-3xl border border-white/5 flex flex-col items-center justify-center relative">
            <div class="relative w-8 h-8 flex items-center justify-center mb-6">
                <div class="w-2.5 h-2.5 bg-white rounded-full shadow-lg z-10"></div>
                <div class="absolute inset-0 bg-white/30 rounded-full animate-ping"></div>
            </div>
            <h4 class="text-white mb-2">Continuous Animations</h4>
            <p class="text-forest-400 text-sm font-mono text-center">animate-ping <br> animate-pulse</p>
        </div>
    </div>
</div>
"""

# Construct Icons HTML
icons_html = """
<div id="icons" class="max-w-[1600px] mx-auto px-6 md:px-12 py-32 relative z-10 border-t border-white/10">
    <div class="mb-16">
        <h2 class="text-4xl md:text-5xl text-forest-50 font-dm-sans font-light tracking-tighter">Icons</h2>
        <p class="text-forest-300 mt-4 font-sans">Using Iconify with Lucide set</p>
    </div>
    
    <div class="flex flex-wrap gap-8">
        <div class="w-16 h-16 bg-forest-900/50 rounded-2xl flex items-center justify-center text-white border border-white/10 text-2xl">
            <iconify-icon icon="lucide:scan"></iconify-icon>
        </div>
        <div class="w-16 h-16 bg-forest-900/50 rounded-2xl flex items-center justify-center text-white border border-white/10 text-2xl">
            <iconify-icon icon="lucide:cpu"></iconify-icon>
        </div>
        <div class="w-16 h-16 bg-forest-900/50 rounded-2xl flex items-center justify-center text-white border border-white/10 text-2xl">
            <iconify-icon icon="lucide:eye"></iconify-icon>
        </div>
        <div class="w-16 h-16 bg-forest-900/50 rounded-2xl flex items-center justify-center text-white border border-white/10 text-2xl">
            <iconify-icon icon="lucide:battery-medium"></iconify-icon>
        </div>
        <div class="w-16 h-16 bg-forest-900/50 rounded-2xl flex items-center justify-center text-white border border-white/10 text-2xl">
            <iconify-icon icon="lucide:wifi"></iconify-icon>
        </div>
        <div class="w-16 h-16 bg-forest-900/50 rounded-2xl flex items-center justify-center text-white border border-white/10 text-2xl">
            <iconify-icon icon="lucide:arrow-right"></iconify-icon>
        </div>
        <div class="w-16 h-16 bg-forest-900/50 rounded-2xl flex items-center justify-center text-white border border-white/10 text-2xl">
            <iconify-icon icon="lucide:arrow-up-right"></iconify-icon>
        </div>
    </div>
</div>
"""


with open('/Users/macintosh/Desktop/Esteticmel/spectra.aura.build (1)/design-system.html', 'w', encoding='utf-8') as out:
    out.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
    out.write(''.join(str(c) for c in head.contents))
    
    # Inject Custom DS Styles for Nav
    out.write('''
<style>
    .ds-nav { position: fixed; top: 0; left: 0; right: 0; background: rgba(10, 24, 20, 0.85); backdrop-filter: blur(12px); padding: 20px; z-index: 99999; display: flex; gap: 30px; justify-content: center; border-bottom: 1px solid rgba(255,255,255,0.1); }
    .ds-nav a { color: #fff; text-decoration: none; font-size: 13px; text-transform: uppercase; letter-spacing: 2px; font-family: 'Inter', sans-serif; opacity: 0.7; transition: opacity 0.3s; }
    .ds-nav a:hover { opacity: 1; }
    #main-header { display: none !important; } /* Hide original nav if copied */
</style>
''')
    out.write('</head>\n')
    
    out.write(f'<body class="{body_class_str} bg-forest-950">\n')
    
    out.write('''
    <nav class="ds-nav">
        <a href="#hero">0. Hero</a>
        <a href="#typography">1. Typography</a>
        <a href="#colors">2. Colors</a>
        <a href="#components">3. Components</a>
        <a href="#layout">4. Layout</a>
        <a href="#motion">5. Motion</a>
        <a href="#icons">6. Icons</a>
    </nav>
    ''')
    
    # Output the background elements
    out.write(bg_str)
    
    # We will wrap the hero in a relative div with top margin
    out.write('<div id="hero" style="position:relative; margin-top: 80px;">\n')
    out.write(hero_str)
    out.write('</div>\n')
    
    out.write(typo_html)
    out.write(colors_html)
    out.write(components_html)
    out.write(layout_html)
    out.write(motion_html)
    out.write(icons_html)
    
    # Append any script tags from body end
    scripts = soup.find_all('script', src=False)
    for s in scripts:
        if 'DOMContentLoaded' in str(s) or 'requestAnimationFrame' in str(s):
             out.write(str(s))
             
    out.write('''
    <script>
    // Trigger scroll animations for DS elements
    setTimeout(() => {
        const reveals = document.querySelectorAll('.reveal-on-scroll');
        reveals.forEach(el => el.classList.add('is-visible'));
    }, 500);
    </script>
    ''')
             
    out.write('\n</body>\n</html>')

print("Created design-system.html successfully.")
