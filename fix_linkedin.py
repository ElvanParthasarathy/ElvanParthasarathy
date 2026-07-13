import os
import urllib.request
import re

assets_dir = 'D:/Projects/ElvanParthasarathy/assets'

url = 'https://cdn.simpleicons.org/linkedin'

def wrap_in_ios_squircle(svg_data, mode):
    bg_color = '#ffffff' if mode == 'dark' else '#181717'
    icon_color = '#181717' if mode == 'dark' else '#ffffff'
    
    match = re.search(r'<svg[^>]*>(.*)</svg>', svg_data, re.DOTALL)
    if match:
        inner_content = match.group(1)
    else:
        inner_content = ""
    
    new_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 34 34">
    <rect x="0" y="0" width="34" height="34" rx="8" ry="8" fill="{bg_color}"/>
    <g transform="translate(5, 5)" fill="{icon_color}">
        {inner_content}
    </g>
</svg>"""
    return new_svg

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        svg_data = response.read().decode('utf-8')
        svg_data = re.sub(r'fill="[^"]+"', '', svg_data)
        
        dark_svg = wrap_in_ios_squircle(svg_data, 'dark')
        with open(os.path.join(assets_dir, f"contact-linkedin-dark.svg"), 'w', encoding='utf-8') as f:
            f.write(dark_svg)
            
        light_svg = wrap_in_ios_squircle(svg_data, 'light')
        with open(os.path.join(assets_dir, f"contact-linkedin-light.svg"), 'w', encoding='utf-8') as f:
            f.write(light_svg)
            
    print(f"Generated Material Icon squircle for linkedin")
except Exception as e:
    print(f"Failed linkedin: {e}")
