import os
import urllib.request
import re

assets_dir = 'D:/Projects/ElvanParthasarathy/assets'

# Phosphor icons to fetch
icon_list = {
    'contact-email': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/envelope-simple.svg',
    'contact-linkedin': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/linkedin-logo.svg',
    'contact-github': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/github-logo.svg',
    'contact-globe': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/globe.svg',
    
    'header-user': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/user.svg',
    'header-wrench': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/wrench.svg',
    'header-rocket': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/rocket-launch.svg',
    'header-trophy': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/trophy.svg',
    
    'skill-code': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/code.svg',
    'skill-database': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/database.svg',
    'skill-network': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/wifi-high.svg',
    
    'bullet-project': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/caret-right.svg',
    'bullet-stack': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/stack.svg',
    'bullet-award': 'https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/medal.svg',
}

def wrap_in_circle(svg_data, mode):
    # mode: 'dark' means white circle with black icon (for dark github theme)
    # mode: 'light' means black circle with white icon (for light github theme)
    
    circle_color = '#ffffff' if mode == 'dark' else '#181717'
    icon_color = '#181717' if mode == 'dark' else '#ffffff'
    
    # Extract just the inner paths of the Phosphor SVG
    # Phosphor SVGs look like: <svg ...><rect width="256" height="256" fill="none"/><path .../></svg>
    inner_content = re.search(r'<svg[^>]*>(.*)</svg>', svg_data, re.DOTALL).group(1)
    
    # We remove the transparent background rect if it exists so it doesn't block the circle
    inner_content = re.sub(r'<rect width="256" height="256" fill="none"/>', '', inner_content)
    
    # We replace currentColor with the icon_color
    inner_content = inner_content.replace('currentColor', icon_color)
    
    new_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
    <circle cx="128" cy="128" r="128" fill="{circle_color}"/>
    {inner_content}
</svg>"""
    return new_svg

for name, url in icon_list.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg_data = response.read().decode('utf-8')
            
            # Generate Dark Mode version
            dark_svg = wrap_in_circle(svg_data, 'dark')
            with open(os.path.join(assets_dir, f"{name}-dark.svg"), 'w', encoding='utf-8') as f:
                f.write(dark_svg)
                
            # Generate Light Mode version
            light_svg = wrap_in_circle(svg_data, 'light')
            with open(os.path.join(assets_dir, f"{name}-light.svg"), 'w', encoding='utf-8') as f:
                f.write(light_svg)
                
        print(f"Generated circle icons for {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")

# Now update the README
readme_path = 'D:/Projects/ElvanParthasarathy/README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

def pic(icon_name, size=24):
    return f"""<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/{icon_name}-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/{icon_name}-light.svg"><img alt="icon" src="./assets/{icon_name}-light.svg" width="{size}" height="{size}" align="center"></picture>"""

# 1. Update contact links
readme = re.sub(r'<a href="mailto:.*?</a>', f'<a href="mailto:Jaiprakashpartha@gmail.com">{pic("contact-email", 30)}</a>', readme)
readme = re.sub(r'<a href="https://linkedin.*?</a>', f'<a href="https://linkedin.com/in/jaiprakashpartha">{pic("contact-linkedin", 30)}</a>', readme)
readme = re.sub(r'<a href="https://github.*?</a>', f'<a href="https://github.com/elvanparthasarathy">{pic("contact-github", 30)}</a>', readme)
readme = re.sub(r'<a href="https://jaiprakashpartha.*?</a>', f'<a href="https://jaiprakashpartha.vercel.app">{pic("contact-globe", 30)}</a>', readme)

# 2. Update section headers (re-replace since we changed the names to header-*)
# Clean out old pictures first
readme = re.sub(r'## <picture>.*?</picture>&nbsp;(.*)', r'## \1', readme)
readme = readme.replace('## About Me', f'## {pic("header-user")}&nbsp;About Me')
readme = readme.replace('## Technical Skills', f'## {pic("header-wrench")}&nbsp;Technical Skills')
readme = readme.replace('## Featured Projects', f'## {pic("header-rocket")}&nbsp;Featured Projects')
readme = readme.replace('## Achievements & Presentations', f'## {pic("header-trophy")}&nbsp;Achievements & Presentations')

# 3. Add icons to Technical Skills
readme = readme.replace('*   **Languages & Frameworks:**', f'*   {pic("skill-code", 18)} **Languages & Frameworks:**')
readme = readme.replace('*   **Databases & DevOps:**', f'*   {pic("skill-database", 18)} **Databases & DevOps:**')
readme = readme.replace('*   **Networking & Professional:**', f'*   {pic("skill-network", 18)} **Networking & Professional:**')

# 4. Add icons to Project Bullets and Tech Stacks
# Just replace standard markdown bullets '*' that are at the start of a line inside the Projects section
# Actually, the bullets in projects are "*   "
# It's safer to just string replace the specific lines
readme = readme.replace('*   Implemented authentication', f'*   {pic("bullet-project", 16)} Implemented authentication')
readme = readme.replace('*   Developed Elvan Agazhi', f'*   {pic("bullet-project", 16)} Developed Elvan Agazhi')
readme = readme.replace('*   Deployed the web application', f'*   {pic("bullet-project", 16)} Deployed the web application')

readme = readme.replace('*   Developed a custom window', f'*   {pic("bullet-project", 16)} Developed a custom window')
readme = readme.replace('*   Integrated projects, certifications', f'*   {pic("bullet-project", 16)} Integrated projects, certifications')

readme = readme.replace('*   Built a modular content', f'*   {pic("bullet-project", 16)} Built a modular content')

readme = readme.replace('*   **Tech Stack:**', f'*   {pic("bullet-stack", 16)} **Tech Stack:**')

# 5. Add icons to Achievements
readme = readme.replace('*   **COULOMB 2025', f'*   {pic("bullet-award", 18)} **COULOMB 2025')
readme = readme.replace('*   **KalaQuest', f'*   {pic("bullet-award", 18)} **KalaQuest')
readme = readme.replace('*   **ARTC-23', f'*   {pic("bullet-award", 18)} **ARTC-23')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme)

print("Massive monochrome upgrade complete!")
