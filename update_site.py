import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update music
content = re.sub(
    r'<source src="assets/music.mp3" type="audio/mpeg">',
    r'<source src="bg-music.mp3" type="audio/mpeg">',
    content
)

# 2. Update envelope loader
old_loader = re.search(r'<!-- Loading Overlay.*?<div class="w-full relative overflow-hidden" id="main-content">', content, re.DOTALL).group(0)

new_loader = """<!-- Loading Overlay (Image-style Envelope) -->
<style>
    .env-wrapper {
        position: relative; width: 320px; height: 220px;
        cursor: pointer; transition: transform 0.3s ease;
        margin-bottom: 2rem;
    }
    .env-wrapper:hover { transform: scale(1.02); }
    .env-back {
        position: absolute; width: 100%; height: 100%;
        background: #1a1a1a; border-radius: 8px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
    }
    .env-flap {
        position: absolute; top: 0; left: 0;
        width: 0; height: 0;
        border-left: 160px solid transparent;
        border-right: 160px solid transparent;
        border-top: 130px solid #2a2a2a;
        transform-origin: top; z-index: 4;
        transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        filter: drop-shadow(0 5px 5px rgba(0,0,0,0.2));
    }
    .env-front {
        position: absolute; bottom: 0; left: 0;
        width: 0; height: 0;
        border-left: 160px solid #222222;
        border-right: 160px solid #222222;
        border-bottom: 120px solid #1f1f1f;
        z-index: 3;
        border-radius: 0 0 8px 8px;
    }
    .env-paper {
        position: absolute; top: 15px; left: 15px;
        width: 290px; height: 190px;
        background: #fcfbf9; z-index: 2;
        display: flex; align-items: center; justify-content: center;
        transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1) 0.3s;
        border: 1px solid #e2dcd0;
    }
    .env-wax {
        position: absolute; top: 105px; left: 50%; transform: translateX(-50%);
        width: 50px; height: 50px;
        background: radial-gradient(circle, #eab308 0%, #a16207 100%);
        border-radius: 50%; z-index: 5;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5), inset 0 2px 5px rgba(255,255,255,0.3);
        display: flex; align-items: center; justify-content: center;
        border: 2px solid #ca8a04;
        transition: opacity 0.3s ease;
    }
    .env-open .env-flap { transform: rotateX(180deg); z-index: 1; }
    .env-open .env-paper { transform: translateY(-120px); z-index: 2; }
    .env-open .env-wax { opacity: 0; }
</style>

<div id="loader" class="fixed inset-0 bg-[#f8f7f5] z-[100] flex flex-col items-center justify-center transition-opacity duration-1000">
    <div class="font-serif text-[#2d2d2d]/60 text-[9px] md:text-[11px] tracking-[0.3em] uppercase mb-4 text-center">Where love begins, forever follows</div>
    <div class="font-script text-5xl md:text-7xl text-[#2d2d2d] mb-12 drop-shadow-sm">Fabiola <span class="text-[#d5cbb3]">&amp;</span> Theodore</div>
    
    <div class="env-wrapper" id="envelope">
        <div class="env-back"></div>
        <div class="env-paper">
            <div class="w-[270px] h-[170px] border border-[#d5cbb3] flex items-center justify-center bg-white shadow-inner">
                <span class="font-serif text-[#d5cbb3] tracking-widest text-sm font-bold uppercase">You're Invited</span>
            </div>
        </div>
        <div class="env-front"></div>
        <div class="env-flap"></div>
        <div class="env-wax">
            <i class="fab fa-pagelines text-white/70 text-xl"></i>
        </div>
    </div>
    
    <div class="font-montserrat text-[10px] text-[#2d2d2d]/50 tracking-[0.4em] uppercase animate-pulse mt-4" id="loader-text">Tap to Open</div>
</div>

<div class="w-full relative overflow-hidden" id="main-content">"""

content = content.replace(old_loader, new_loader)

# 3. Add Lightbox HTML right after body opens (or inside main-content)
lightbox_html = """
<!-- Lightbox -->
<div id="lightbox" class="fixed inset-0 bg-black/95 z-[200] hidden flex-col items-center justify-center opacity-0 transition-opacity duration-300">
    <button id="lightbox-close" class="absolute top-6 right-6 text-white text-4xl hover:text-[#d5cbb3] transition-colors">&times;</button>
    <img id="lightbox-img" src="" class="max-w-[90vw] max-h-[85vh] object-contain rounded shadow-2xl border-4 border-white">
</div>
"""
content = content.replace('<body class="antialiased">', f'<body class="antialiased">\n{lightbox_html}')

# Add cursor-pointer to moments images
content = content.replace('class="film-frame"><img', 'class="film-frame cursor-pointer"><img class="gallery-img"')

# 4. Wishes section form logic & likes
wishes_form = """
                <form class="flex flex-col gap-6">
                    <input type="text" id="wish-name" placeholder="Your Name" class="w-full bg-transparent border-b border-[#d5cbb3]/50 py-3 text-[#2d2d2d] focus:outline-none focus:border-[#d5cbb3] font-montserrat text-sm transition-colors placeholder:text-[#2d2d2d]/40">
                    <textarea id="wish-msg" placeholder="Your Wishes..." rows="4" class="w-full bg-transparent border-b border-[#d5cbb3]/50 py-3 text-[#2d2d2d] focus:outline-none focus:border-[#d5cbb3] font-montserrat text-sm transition-colors resize-none placeholder:text-[#2d2d2d]/40"></textarea>
                    <button type="button" id="submit-wish" class="mt-6 px-10 py-4 bg-[#1a1a1a] text-[#f4f1ea] text-[10px] tracking-[0.2em] uppercase hover:bg-[#d5cbb3] hover:text-[#1a1a1a] transition-all rounded shadow-[0_10px_20px_rgba(0,0,0,0.1)] font-bold transform hover:-translate-y-1 duration-300 self-center">
                        Send Love <i class="fas fa-heart ml-2 text-[#d5cbb3]"></i>
                    </button>
                </form>
"""
old_form = re.search(r'<form class="flex flex-col gap-6">.*?</form>', content, re.DOTALL).group(0)
content = content.replace(old_form, wishes_form)

# Add id to comments display
content = content.replace('<div class="mt-16 space-y-6 gs-reveal">', '<div class="mt-16 space-y-6 gs-reveal" id="comments-container">')

# Remove the hardcoded sample comment to let JS handle it, wait I can just let JS overwrite it.
# 5. Remove RSVP buttons and add form
rsvp_section = re.search(r'<div class="flex flex-col md:flex-row gap-5 justify-center max-w-sm mx-auto md:max-w-none">.*?</div>', content, re.DOTALL).group(0)
new_rsvp = """<form class="flex flex-col gap-4 max-w-sm mx-auto">
                <input type="text" placeholder="Guest Name(s)" class="w-full bg-transparent border-b border-[#d5cbb3]/50 py-3 text-[#2d2d2d] focus:outline-none focus:border-[#d5cbb3] font-montserrat text-sm transition-colors placeholder:text-[#2d2d2d]/50">
                <select class="w-full bg-transparent border-b border-[#d5cbb3]/50 py-3 text-[#2d2d2d] focus:outline-none focus:border-[#d5cbb3] font-montserrat text-sm transition-colors placeholder:text-[#2d2d2d]/50 appearance-none">
                    <option value="" disabled selected>Will you attend?</option>
                    <option value="yes">Joyfully Accepts</option>
                    <option value="no">Regretfully Declines</option>
                </select>
                <button type="button" class="mt-6 px-10 py-4 bg-[#1a1a1a] text-[#f4f1ea] text-[10px] tracking-[0.2em] uppercase hover:bg-[#d5cbb3] hover:text-[#1a1a1a] transition-all rounded shadow-md font-bold self-center">
                    Submit RSVP
                </button>
            </form>"""
content = content.replace(rsvp_section, new_rsvp)

# Add JavaScript for Wishes, Lightbox, etc.
js_addition = """
        // Lightbox Logic
        const lightbox = document.getElementById('lightbox');
        const lightboxImg = document.getElementById('lightbox-img');
        const lightboxClose = document.getElementById('lightbox-close');
        
        document.querySelectorAll('.gallery-img').forEach(img => {
            img.addEventListener('click', (e) => {
                lightboxImg.src = e.target.src;
                lightbox.style.display = 'flex';
                // Trigger reflow
                void lightbox.offsetWidth;
                lightbox.style.opacity = '1';
            });
        });
        
        lightboxClose.addEventListener('click', () => {
            lightbox.style.opacity = '0';
            setTimeout(() => { lightbox.style.display = 'none'; }, 300);
        });
        lightbox.addEventListener('click', (e) => {
            if(e.target === lightbox) {
                lightbox.style.opacity = '0';
                setTimeout(() => { lightbox.style.display = 'none'; }, 300);
            }
        });

        // Wishes Logic
        let wishes = [
            { name: "Rahul & Sneha", message: "Wishing you both a lifetime of immense love, joy, and happiness! Can't wait for the beautiful celebrations.", likes: 12, liked: false },
            { name: "Aman", message: "Congratulations! So happy for you two.", likes: 4, liked: false }
        ];

        window.toggleLike = function(index) {
            wishes[index].liked = !wishes[index].liked;
            wishes[index].likes += wishes[index].liked ? 1 : -1;
            renderWishes();
        };

        function renderWishes() {
            const container = document.getElementById('comments-container');
            container.innerHTML = '';
            wishes.forEach((wish, index) => {
                const div = document.createElement('div');
                div.className = "bg-white/60 p-6 rounded-lg border border-[#e2dcd0]/40 shadow-sm relative hover:shadow-md transition-shadow duration-300 text-left";
                div.innerHTML = `
                    <i class="fas fa-quote-right absolute top-6 right-6 text-[#d5cbb3]/20 text-3xl"></i>
                    <div class="flex justify-between items-start mb-2">
                        <div class="font-serif font-bold text-[#2d2d2d] text-lg">${wish.name}</div>
                        <button class="flex items-center gap-2 text-[#2d2d2d]/60 hover:text-red-500 transition-colors ${wish.liked ? 'text-red-500' : ''}" onclick="toggleLike(${index})">
                            <i class="${wish.liked ? 'fas' : 'far'} fa-heart"></i>
                            <span class="text-xs font-montserrat">${wish.likes}</span>
                        </button>
                    </div>
                    <p class="font-montserrat text-xs md:text-sm text-[#2d2d2d]/80 italic leading-relaxed">"${wish.message}"</p>
                `;
                container.appendChild(div);
            });
        }
        
        renderWishes();

        document.getElementById('submit-wish').addEventListener('click', () => {
            const name = document.getElementById('wish-name').value;
            const msg = document.getElementById('wish-msg').value;
            if(name && msg) {
                wishes.unshift({ name, message: msg, likes: 0, liked: false });
                document.getElementById('wish-name').value = '';
                document.getElementById('wish-msg').value = '';
                renderWishes();
            }
        });
"""

# Insert JS before initGSAP()
content = content.replace('function initGSAP() {', f'{js_addition}\n        function initGSAP() {{')

with open('index.html', 'w') as f:
    f.write(content)

