import os
import urllib.request
import re

assets_dir = 'D:/Projects/ElvanParthasarathy/assets'

icon_list = {
    'contact-email': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/mail.svg',
    'contact-linkedin': 'https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/linkedin.svg',
    'contact-github': 'https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/github.svg',
    'contact-globe': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/public.svg',
    
    'header-user': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/person.svg',
    'header-wrench': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/build.svg',
    'header-rocket': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/rocket_launch.svg',
    'header-trophy': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/emoji_events.svg',
    
    'skill-code': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/code.svg',
    'skill-database': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/storage.svg',
    'skill-network': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/wifi.svg',
    
    'bullet-project': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/play_arrow.svg',
    'bullet-stack': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/layers.svg',
    'bullet-award': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/workspace_premium.svg',
}

def wrap_in_ios_squircle(svg_data, mode):
    bg_color = '#ffffff' if mode == 'dark' else '#181717'
    icon_color = '#181717' if mode == 'dark' else '#ffffff'
    
    match = re.search(r'<svg[^>]*>(.*)</svg>', svg_data, re.DOTALL)
    if match:
        inner_content = match.group(1)
    else:
        inner_content = ""
    
    # Material Icons and Simple Icons use a 24x24 viewBox.
    # We will use a 34x34 squircle, translating 5px on x and y.
    new_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 34 34">
    <rect x="0" y="0" width="34" height="34" rx="8" ry="8" fill="{bg_color}"/>
    <g transform="translate(5, 5)" fill="{icon_color}">
        {inner_content}
    </g>
</svg>"""
    return new_svg

for name, url in icon_list.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg_data = response.read().decode('utf-8')
            
            # SimpleIcons explicitly have `<path d="..." />` without fill, but some might. 
            # We strip any hardcoded fills so our group `<g fill="...">` applies.
            svg_data = re.sub(r'fill="[^"]+"', '', svg_data)
            
            # Generate Dark Mode version
            dark_svg = wrap_in_ios_squircle(svg_data, 'dark')
            with open(os.path.join(assets_dir, f"{name}-dark.svg"), 'w', encoding='utf-8') as f:
                f.write(dark_svg)
                
            # Generate Light Mode version
            light_svg = wrap_in_ios_squircle(svg_data, 'light')
            with open(os.path.join(assets_dir, f"{name}-light.svg"), 'w', encoding='utf-8') as f:
                f.write(light_svg)
                
        print(f"Generated Material Icon squircle for {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")

print("Material Icons upgrade complete!")
