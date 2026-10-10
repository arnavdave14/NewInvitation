import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the entire loader block
old_loader_regex = r'<!-- Loading Overlay.*?<div class="w-full relative overflow-hidden" id="main-content">'
old_loader_match = re.search(old_loader_regex, content, re.DOTALL)

if old_loader_match:
    new_loader = """<!-- Loading Overlay (Image-style Envelope) -->
<style>
    .env-wrapper {
        position: relative; width: 360px; height: 240px;
        cursor: pointer; transition: transform 0.3s ease;
        margin-bottom: 2rem;
    }
    .env-wrapper:hover { transform: scale(1.02); }
    
    .env-paper {
        position: absolute; top: 10px; left: 10px;
        width: 340px; height: 210px;
        background: #fcfbf9; z-index: 2;
        display: flex; align-items: center; justify-content: center;
        transition: transform 0.9s cubic-bezier(0.4, 0, 0.2, 1) 0.3s;
        box-shadow: 0 0 15px rgba(0,0,0,0.15);
    }
    
    .env-front {
        position: absolute; inset: 0; z-index: 3;
        pointer-events: none;
    }
    
    .env-flap {
        position: absolute; top: 0; left: 0;
        width: 100%; height: 180px;
        transform-origin: top; z-index: 4;
        transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        filter: drop-shadow(0 10px 15px rgba(0,0,0,0.4));
    }
    
    .env-wax {
        position: absolute; top: 125px; left: 50%; transform: translateX(-50%);
        width: 60px; height: 60px;
        background: radial-gradient(circle, #eab308 0%, #a16207 100%);
        border-radius: 50%; z-index: 5;
        box-shadow: 0 4px 15px rgba(0,0,0,0.6), inset 0 2px 5px rgba(255,255,255,0.4);
        display: flex; align-items: center; justify-content: center;
        border: 2px solid #ca8a04;
        transition: opacity 0.3s ease;
    }
    
    .env-open .env-flap { transform: rotateX(180deg); z-index: 1; }
    .env-open .env-paper { transform: translateY(-160px); z-index: 2; }
    .env-open .env-wax { opacity: 0; }
</style>

<div id="loader" class="fixed inset-0 bg-[#f8f7f5] z-[100] flex flex-col items-center justify-center transition-opacity duration-1000">
    <div class="font-serif text-[#2d2d2d]/60 text-[9px] md:text-[11px] tracking-[0.4em] uppercase mb-4 text-center">Where love begins, forever follows</div>
    <div class="font-script text-6xl md:text-8xl text-[#2d2d2d] mb-12 drop-shadow-sm">Hritik <span class="text-[#d5cbb3] text-4xl md:text-5xl mx-2">&amp;</span> Priya</div>
    
    <div class="env-wrapper" id="envelope">
        <!-- Back -->
        <div class="absolute inset-0 bg-[#151515] rounded shadow-2xl"></div>
        
        <!-- Paper -->
        <div class="env-paper">
            <div class="w-[310px] h-[180px] border border-[#d5cbb3] flex flex-col items-center justify-center bg-white shadow-inner">
                <div class="font-serif text-[#d5cbb3] tracking-[0.4em] text-xs font-bold uppercase mb-4">You're Invited</div>
                <div class="font-script text-4xl text-[#2d2d2d]">Hritik & Priya</div>
            </div>
        </div>
        
        <!-- Front Flaps -->
        <div class="env-front">
           <svg viewBox="0 0 360 240" class="w-full h-full drop-shadow-2xl">
               <path d="M 0 0 L 180 140 L 0 240 Z" fill="#202020"/>
               <path d="M 360 0 L 180 140 L 360 240 Z" fill="#202020"/>
               <path d="M 0 240 L 180 120 L 360 240 Z" fill="#1a1a1a"/>
           </svg>
        </div>
        
        <!-- Top Flap -->
        <div class="env-flap">
           <svg viewBox="0 0 360 180" class="w-full h-full">
               <path d="M 0 0 L 360 0 L 360 20 C 270 90, 220 130, 180 150 C 140 130, 90 90, 0 20 Z" fill="#222222"/>
           </svg>
        </div>
        
        <!-- Wax Seal -->
        <div class="env-wax">
            <i class="fab fa-pagelines text-white/60 text-2xl drop-shadow-md"></i>
        </div>
    </div>
    
    <div class="font-montserrat text-[10px] text-[#2d2d2d]/50 tracking-[0.4em] uppercase animate-pulse mt-8" id="loader-text">Tap to Open</div>
</div>

<div class="w-full relative overflow-hidden" id="main-content">"""
    content = content.replace(old_loader_match.group(0), new_loader)

with open('index.html', 'w') as f:
    f.write(content)

