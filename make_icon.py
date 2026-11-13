from PIL import Image, ImageDraw, ImageFilter
import os
os.makedirs("assets", exist_ok=True)
S = 1024
src = Image.open("icon-source.png").convert("RGB")
full = src.resize((S, S), Image.LANCZOS)
full.save("assets/icon-only.png")
m = Image.radial_gradient("L").resize((S, S))
Image.composite(Image.new("RGB", (S, S), (14, 18, 46)), Image.new("RGB", (S, S), (40, 42, 90)), m).save("assets/icon-background.png")
size = int(S * 0.60)
art = src.resize((size, size), Image.LANCZOS).convert("RGBA")
mask = Image.new("L", (size, size), 0)
pad = int(size * 0.10)
ImageDraw.Draw(mask).rectangle([pad, pad, size - pad, size - pad], fill=255)
art.putalpha(mask.filter(ImageFilter.GaussianBlur(size * 0.05)))
fg = Image.new("RGBA", (S, S), (0, 0, 0, 0))
fg.paste(art, ((S - size) // 2, (S - size) // 2))
fg.save("assets/icon-foreground.png")
print("done")
