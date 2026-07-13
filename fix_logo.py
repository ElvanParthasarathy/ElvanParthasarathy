import os
import xml.etree.ElementTree as ET
import shutil

src_logo = 'D:/Projects/Portfolio/public/img/ui/jv2tra.svg'
assets_dir = 'D:/Projects/ElvanParthasarathy/assets'

# 1. Copy the white logo for Dark Mode
dark_logo_path = os.path.join(assets_dir, 'jv2tra-dark.svg')
shutil.copy2(src_logo, dark_logo_path)

# 2. Create the black logo for Light Mode
light_logo_path = os.path.join(assets_dir, 'jv2tra-light.svg')
tree = ET.parse(src_logo)
root = tree.getroot()

for elem in root.iter():
    if 'fill' in elem.attrib and elem.attrib['fill'] == '#fff':
        elem.attrib['fill'] = '#181717' # Dark grey for light mode

tree.write(light_logo_path)

# 3. Update the README.md
readme_path = 'D:/Projects/ElvanParthasarathy/README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

# Replace the logo links
readme = readme.replace('./assets/logo-dark.svg', './assets/jv2tra-dark.svg')
readme = readme.replace('./assets/logo-light.svg', './assets/jv2tra-light.svg')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme)

print("Updated logos to jv2tra!")
