import os
import xml.etree.ElementTree as ET

# 1. Colorize the icons
icon_colors = {
    'email-svgrepo-com.svg': '#EA4335',       # Gmail Red
    'linkedin-svgrepo-com.svg': '#0A66C2',    # LinkedIn Blue
    'github-142-svgrepo-com.svg': '#6e5494',  # GitHub Purple (looks good on both themes)
    'location-pin-filled-svgrepo-com.svg': '#00C853' # Vibrant Green
}

assets_dir = 'd:/Projects/ElvanParthasarathy/assets'

for filename, color in icon_colors.items():
    filepath = os.path.join(assets_dir, filename)
    if os.path.exists(filepath):
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            # Remove any existing fill attributes and add our color to the root svg
            if 'fill' in root.attrib:
                del root.attrib['fill']
            
            # Force all paths to use the new color
            for elem in root.iter():
                if elem.tag.endswith('path') or elem.tag.endswith('circle') or elem.tag.endswith('rect') or elem.tag.endswith('polygon'):
                    elem.attrib['fill'] = color
                    
            tree.write(filepath)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# 2. Generate Light and Dark mode logos from the portfolio logo
logo_src = 'd:/Projects/Portfolio/public/img/ui/logo.svg'
if os.path.exists(logo_src):
    tree = ET.parse(logo_src)
    root = tree.getroot()
    
    # Generate logo-light.svg (White circle, Black shapes)
    for elem in root.iter():
        if elem.tag.endswith('circle') and 'fill' in elem.attrib and elem.attrib['fill'] == '#fff':
            pass # Keep it white
        elif elem.tag.endswith('circle') or elem.tag.endswith('polygon') or elem.tag.endswith('rect'):
            elem.attrib['fill'] = '#181717' # Dark grey/black for the JAI shapes
            
    tree.write(os.path.join(assets_dir, 'logo-light.svg'))
    
    # Generate logo-dark.svg (Dark/Transparent circle, White shapes)
    for elem in root.iter():
        if elem.tag.endswith('circle') and 'fill' in elem.attrib and elem.attrib['fill'] == '#fff':
            elem.attrib['fill'] = 'transparent' # Make background transparent for dark mode
        elif elem.tag.endswith('circle') or elem.tag.endswith('polygon') or elem.tag.endswith('rect'):
            elem.attrib['fill'] = '#ffffff' # White for the JAI shapes
            
    tree.write(os.path.join(assets_dir, 'logo-dark.svg'))


# 3. Fix the README.md HTML structure to prevent blue underlines and use the new dynamic logo
readme_path = 'd:/Projects/ElvanParthasarathy/README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

# The new header HTML
new_header = """<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/logo-light.svg">
    <img alt="Jai Logo" src="./assets/logo-light.svg" width="120" height="120">
  </picture>
  
  <h1>Elvan Parthasarathy (Jaiprakash P)</h1>
  <p>Final-year ECE student with full-stack development experience across React, TypeScript, and native Android (Kotlin).</p>
  
  <p>
    <a href="mailto:Jaiprakashpartha@gmail.com"><img src="./assets/email-svgrepo-com.svg" width="30" alt="Email" /></a>
    <a href="https://linkedin.com/in/jaiprakashpartha"><img src="./assets/linkedin-svgrepo-com.svg" width="30" alt="LinkedIn" /></a>
    <a href="https://github.com/elvanparthasarathy"><img src="./assets/github-142-svgrepo-com.svg" width="30" alt="GitHub" /></a>
    <a href="https://jaiprakashpartha.vercel.app"><img src="./assets/location-pin-filled-svgrepo-com.svg" width="30" alt="Portfolio" /></a>
  </p>
</div>"""

# Replace everything from <div align="center"> to </div> with the new header
import re
readme = re.sub(r'<div align="center">.*?</div>', new_header, readme, flags=re.DOTALL, count=1)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme)

print("Colorized SVGs, generated dark/light logos, and fixed README!")
