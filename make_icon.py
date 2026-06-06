from PIL import Image

# 1. Open your logo and ensure it has a transparency layer
img = Image.open('pages/static/images/holychildL.png').convert("RGBA")

# 2. Make it a perfect square (Windows hates rectangles)
width, height = img.size
max_dim = max(width, height)
square_img = Image.new('RGBA', (max_dim, max_dim), (0, 0, 0, 0)) # Transparent background
square_img.paste(img, ((max_dim - width) // 2, (max_dim - height) // 2))

# 3. Force high-quality resizing (LANCZOS) to maximum Windows icon size
hq_icon = square_img.resize((256, 256), Image.Resampling.LANCZOS)

# 4. Save with all Windows sizes bundled perfectly inside
hq_icon.save(
    'hcc_icon.ico', 
    format='ICO', 
    sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
)

print("HD Icon created successfully!")