import os
import urllib.request
import re

assets_dir = 'D:/Projects/ElvanParthasarathy/assets'

# Using Phosphor 'fill' weight for solid, iOS-like icons
# The filenames for fill icons end with '-fill.svg'
icon_list = {
    'contact-email': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/envelope-simple-fill.svg',
    'contact-linkedin': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/linkedin-logo-fill.svg',
    'contact-github': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/github-logo-fill.svg',
    'contact-globe': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/globe-fill.svg',
    
    'header-user': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/user-fill.svg',
    'header-wrench': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/wrench-fill.svg',
    'header-rocket': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/rocket-launch-fill.svg',
    'header-trophy': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/trophy-fill.svg',
    
    'skill-code': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/code-fill.svg',
    'skill-database': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/database-fill.svg',
    'skill-network': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/wifi-high-fill.svg',
    
    'bullet-project': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/caret-right-fill.svg',
    'bullet-stack': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/stack-fill.svg',
    'bullet-award': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/medal-fill.svg',
}

def wrap_in_ios_squircle(svg_data, mode):
    # mode: 'dark' means white squircle with black icon (for dark github theme)
    # mode: 'light' means black squircle with white icon (for light github theme)
    
    bg_color = '#ffffff' if mode == 'dark' else '#181717'
    icon_color = '#181717' if mode == 'dark' else '#ffffff'
    
    inner_content = re.search(r'<svg[^>]*>(.*)</svg>', svg_data, re.DOTALL).group(1)
    
    # Remove the transparent background rect if it exists
    inner_content = re.sub(r'<rect width="256" height="256" fill="none"\s*/>', '', inner_content)
    
    # Phosphor fill icons don't always have currentColor, some do. 
    # Let's just force fill on all paths if it's there.
    # To be safe, we'll wrap the inner content in a group with fill set.
    
    # Viewbox 350x350 gives nice padding for a 256x256 icon (47px padding on all sides)
    # rx=80 creates the perfect iOS squircle curve
    new_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 350">
    <rect x="0" y="0" width="350" height="350" rx="80" ry="80" fill="{bg_color}"/>
    <g transform="translate(47, 47)" fill="{icon_color}">
        {inner_content}
    </g>
</svg>"""
    return new_svg

for name, url in icon_list.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg_data = response.read().decode('utf-8')
            
            # Generate Dark Mode version
            dark_svg = wrap_in_ios_squircle(svg_data, 'dark')
            with open(os.path.join(assets_dir, f"{name}-dark.svg"), 'w', encoding='utf-8') as f:
                f.write(dark_svg)
                
            # Generate Light Mode version
            light_svg = wrap_in_ios_squircle(svg_data, 'light')
            with open(os.path.join(assets_dir, f"{name}-light.svg"), 'w', encoding='utf-8') as f:
                f.write(light_svg)
                
        print(f"Generated iOS squircle icons for {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")

print("Massive iOS upgrade complete!")
