from PIL import Image

img = Image.open('Headshot.png')
img.thumbnail((600, 600), Image.Resampling.LANCZOS)
img.save('Headshot.png', 'PNG', optimize=True)
print('Image compressed successfully')
