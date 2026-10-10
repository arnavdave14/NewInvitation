import re

file_path = "/Users/apple/Desktop/Invitation_2/index.html"
with open(file_path, "r") as f:
    content = f.read()

# Container padding and margin
content = content.replace(
    'bg-[#fcfbf9] rounded-xl p-8 relative z-10 -mt-24 mx-4',
    'bg-[#fcfbf9] rounded-xl px-5 py-5 pb-5 relative z-10 -mt-16 mx-4'
)

# Icon margin
content = content.replace(
    'class="fab fa-pagelines text-[#d5cbb3] text-xl mb-4',
    'class="fab fa-pagelines text-[#d5cbb3] text-lg mb-2'
)

# Title margin
content = content.replace(
    'tracking-[0.2em] mb-3 text-[#2d2d2d]',
    'tracking-[0.2em] mb-1 text-[#2d2d2d]'
)

# Divider margin
content = content.replace(
    'w-12 h-[2px] bg-[#d5cbb3] mb-6',
    'w-8 h-[2px] bg-[#d5cbb3] mb-4'
)

# Date container
content = content.replace(
    'gap-4 mb-6"',
    'gap-4 mb-4"'
)
content = content.replace(
    'text-[54px]',
    'text-[46px]'
)

# Details box
content = content.replace(
    'py-4 px-2 mb-4',
    'py-3 px-2 mb-3'
)
content = content.replace(
    'flex flex-col gap-3',
    'flex flex-col gap-2'
)
content = content.replace(
    'justify-center gap-3',
    'justify-center gap-2'
)

# Attire tag
content = content.replace(
    'attire-badge p-3',
    'attire-badge py-2 px-3'
)
content = content.replace(
    'text-[8px] uppercase tracking-[0.3em] font-bold text-[#d5cbb3] mb-1',
    'text-[8px] uppercase tracking-[0.3em] font-bold text-[#d5cbb3] mb-0'
)

with open(file_path, "w") as f:
    f.write(content)

