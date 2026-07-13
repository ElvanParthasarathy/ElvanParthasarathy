import os
import urllib.request

assets_dir = 'D:/Projects/ElvanParthasarathy/assets'

# Phosphor raw URLs
icons = {
    'ph-email.svg': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/envelope-simple.svg',
    'ph-linkedin.svg': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/linkedin-logo.svg',
    'ph-github.svg': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/github-logo.svg',
    'ph-globe.svg': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/globe.svg',
    
    # Section header icons
    'ph-user.svg': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/user.svg',
    'ph-wrench.svg': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/wrench.svg',
    'ph-rocket.svg': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/rocket-launch.svg',
    'ph-trophy.svg': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/trophy.svg',
}

# Colors for Light and Dark modes
# Phosphor uses 'currentColor' or 'fill="..."' we can replace it.
brand_colors = {
    'ph-email': '#EA4335',
    'ph-linkedin': '#0A66C2',
    'ph-github': '#6e5494',
    'ph-globe': '#00C853',
    # We will make section headers dynamic light/dark
}

for filename, url in icons.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg_data = response.read().decode('utf-8')
            
            # Base name without .svg
            base = filename.replace('.svg', '')
            
            if base in brand_colors:
                # These are colored contact links. We replace "currentColor" with the brand color.
                colored_svg = svg_data.replace('currentColor', brand_colors[base])
                with open(os.path.join(assets_dir, filename), 'w', encoding='utf-8') as f:
                    f.write(colored_svg)
            else:
                # These are section headers. We need a dark mode version (white) and light mode version (black)
                dark_svg = svg_data.replace('currentColor', '#ffffff')
                with open(os.path.join(assets_dir, f"{base}-dark.svg"), 'w', encoding='utf-8') as f:
                    f.write(dark_svg)
                    
                light_svg = svg_data.replace('currentColor', '#24292e') # GitHub dark grey for light mode text
                with open(os.path.join(assets_dir, f"{base}-light.svg"), 'w', encoding='utf-8') as f:
                    f.write(light_svg)
                    
        print(f"Downloaded and processed {filename}")
    except Exception as e:
        print(f"Failed {filename}: {e}")
