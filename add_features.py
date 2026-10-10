import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add Confetti JS to head
if 'canvas-confetti' not in content:
    content = content.replace('</head>', '    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>\n</head>')

# 2. Make comments scrollable and stylize scrollbar
old_comments = '<div class="mt-16 space-y-6 gs-reveal" id="comments-container">'
new_comments = """<style>
#comments-container::-webkit-scrollbar { width: 6px; }
#comments-container::-webkit-scrollbar-track { background: transparent; }
#comments-container::-webkit-scrollbar-thumb { background: #d5cbb3; border-radius: 10px; }
</style>
<div class="mt-16 space-y-6 gs-reveal max-h-[400px] overflow-y-auto pr-2" id="comments-container">"""
content = content.replace(old_comments, new_comments)

# 3. Add Scratch Card HTML
scratch_html = """
    <!-- Scratch Card Section -->
    <div class="relative w-full bg-[#f8f7f5] py-24 flex flex-col items-center justify-center border-t border-b border-[#e2dcd0]/50" id="scratch-section">
        <div class="text-center mb-10 gs-reveal">
            <h3 class="font-serif text-3xl md:text-5xl text-[#d5cbb3] mb-4">The Big Day</h3>
            <p class="font-montserrat text-[10px] md:text-xs tracking-[0.4em] uppercase text-[#2d2d2d]/60">Scratch to reveal</p>
        </div>
        
        <div class="relative w-[300px] h-[150px] md:w-[450px] md:h-[220px] rounded-xl overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.15)] select-none gs-reveal">
            <!-- The revealed content -->
            <div class="absolute inset-0 bg-[#151515] flex flex-col items-center justify-center pointer-events-none">
                 <div class="font-serif text-5xl md:text-6xl text-[#d5cbb3] mb-4">14 . 02 . 2026</div>
                 <div class="font-montserrat text-[10px] md:text-xs tracking-[0.3em] text-[#f4f1ea] uppercase">Udaipur, Rajasthan</div>
            </div>
            <!-- The scratchable canvas -->
            <canvas id="scratch-canvas" class="absolute inset-0 w-full h-full cursor-crosshair touch-none"></canvas>
        </div>
    </div>
"""
# Insert scratch card right after Hero section
content = content.replace('<!-- Our Story Section -->', f'{scratch_html}\n    <!-- Our Story Section -->')

# 4. Add Confetti and Scratch Card JS
# Add confetti trigger to envelope click
content = content.replace("envelope.classList.add('env-open');", "envelope.classList.add('env-open');\n            confetti({ particleCount: 150, spread: 80, origin: { y: 0.6 }, colors: ['#d5cbb3', '#ffffff', '#eab308'] });")

# Add confetti trigger to submit wish
content = content.replace("renderWishes();\n            }", "renderWishes();\n                confetti({ particleCount: 100, spread: 70, origin: { y: 0.8 }, colors: ['#ff0000', '#d5cbb3'] });\n            }")


scratch_js = """
        // Scratch Card Logic
        const canvas = document.getElementById('scratch-canvas');
        if (canvas) {
            const ctx = canvas.getContext('2d', { willReadFrequently: true });
            let isDragging = false;
            
            function initScratchCard() {
                canvas.width = canvas.offsetWidth;
                canvas.height = canvas.offsetHeight;
                
                // Gold foil gradient
                const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
                gradient.addColorStop(0, '#c8bc9f');
                gradient.addColorStop(0.5, '#e2dcd0');
                gradient.addColorStop(1, '#a89973');
                ctx.fillStyle = gradient;
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                // Overlay text
                ctx.fillStyle = '#2d2d2d';
                ctx.font = 'italic 20px serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.globalAlpha = 0.6;
                ctx.fillText('Scratch here with your finger', canvas.width/2, canvas.height/2);
                ctx.globalAlpha = 1.0;
            }
            
            // We need to wait for layout
            setTimeout(initScratchCard, 500);
            window.addEventListener('resize', initScratchCard);
            
            const scratch = (x, y) => {
                ctx.globalCompositeOperation = 'destination-out';
                ctx.beginPath();
                ctx.arc(x, y, 25, 0, Math.PI * 2);
                ctx.fill();
            };
            
            const getMousePos = (e) => {
                const rect = canvas.getBoundingClientRect();
                const clientX = e.touches ? e.touches[0].clientX : e.clientX;
                const clientY = e.touches ? e.touches[0].clientY : e.clientY;
                return {
                    x: clientX - rect.left,
                    y: clientY - rect.top
                };
            };

            canvas.addEventListener('mousedown', () => isDragging = true);
            canvas.addEventListener('touchstart', (e) => { isDragging = true; });
            
            window.addEventListener('mouseup', () => isDragging = false);
            window.addEventListener('touchend', () => isDragging = false);
            
            canvas.addEventListener('mousemove', (e) => {
                if (!isDragging) return;
                const pos = getMousePos(e);
                scratch(pos.x, pos.y);
            });
            
            canvas.addEventListener('touchmove', (e) => {
                if (!isDragging) return;
                const pos = getMousePos(e);
                scratch(pos.x, pos.y);
            });
        }
"""
content = content.replace('// Wishes Logic', f'{scratch_js}\n        // Wishes Logic')

with open('index.html', 'w') as f:
    f.write(content)

