import os
import urllib.request
import re

assets_dir = 'D:/Projects/ElvanParthasarathy/assets'

icon_list = {
    'contact-email': 'https://raw.githubusercontent.com/marella/material-design-icons/main/svg/round/mail.svg',
    'contact-linkedin': 'https://raw.githubusercontent.com/simple-icons/simple-icons/master/icons/linkedin.svg',
    'contact-github': 'https://raw.githubusercontent.com/simple-icons/simple-icons/master/icons/github.svg',
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

gradients = {
    'contact-email': ('#EA4335', '#F57C00'), # Red to Orange
    'contact-linkedin': ('#0077B5', '#00A0DC'), # LinkedIn Blue
    'contact-github': ('#24292e', '#4f565e'), # GitHub Black/Grey
    'contact-globe': ('#0F9D58', '#34A853'), # Green
    
    'header-user': ('#3F51B5', '#5C6BC0'), # Indigo
    'header-wrench': ('#00BCD4', '#26C6DA'), # Cyan
    'header-rocket': ('#FF9800', '#FFB74D'), # Orange
    'header-trophy': ('#FFC107', '#FFD54F'), # Amber
    
    'skill-code': ('#9C27B0', '#BA68C8'), # Purple
    'skill-database': ('#03A9F4', '#4FC3F7'), # Light Blue
    'skill-network': ('#4CAF50', '#81C784'), # Green
    
    'bullet-project': ('#F44336', '#EF5350'), # Red
    'bullet-stack': ('#673AB7', '#9575CD'), # Deep Purple
    'bullet-award': ('#FFEB3B', '#FFF176'), # Yellow
}

def wrap_in_samsung_circle(svg_data, icon_name):
    color1, color2 = gradients.get(icon_name, ('#000000', '#444444'))
    
    match = re.search(r'<svg[^>]*>(.*)</svg>', svg_data, re.DOTALL)
    inner_content = match.group(1) if match else ""
    
    # 48x48 canvas, circle radius 24.
    # Inner icon is 24x24 (translated 12,12 to center it).
    # This gives MASSIVE breathing room, exactly like a Samsung app icon.
    new_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
    <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{color1};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{color2};stop-opacity:1" />
        </linearGradient>
    </defs>
    <circle cx="24" cy="24" r="24" fill="url(#grad)"/>
    <g transform="translate(12, 12)" fill="#ffffff">
        {inner_content}
    </g>
</svg>"""
    return new_svg

for name, url in icon_list.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg_data = response.read().decode('utf-8')
            svg_data = re.sub(r'fill="[^"]+"', '', svg_data)
            
            # Generate Single Gradient Version
            gradient_svg = wrap_in_samsung_circle(svg_data, name)
            with open(os.path.join(assets_dir, f"{name}.svg"), 'w', encoding='utf-8') as f:
                f.write(gradient_svg)
                
        print(f"Generated Samsung Gradient for {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")

# Now update the README
readme_path = 'D:/Projects/ElvanParthasarathy/README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

def img(icon_name, size=24):
    return f'<img alt="{icon_name}" src="./assets/{icon_name}.svg" width="{size}" height="{size}" align="center">'

# 1. Update contact links
readme = re.sub(r'<a href="mailto:.*?</a>', f'<a href="mailto:Jaiprakashpartha@gmail.com">{img("contact-email", 34)}</a>', readme)
readme = re.sub(r'<a href="https://linkedin.*?</a>', f'<a href="https://linkedin.com/in/jaiprakashpartha">{img("contact-linkedin", 34)}</a>', readme)
readme = re.sub(r'<a href="https://github.*?</a>', f'<a href="https://github.com/elvanparthasarathy">{img("contact-github", 34)}</a>', readme)
readme = re.sub(r'<a href="https://jaiprakashpartha.*?</a>', f'<a href="https://jaiprakashpartha.vercel.app">{img("contact-globe", 34)}</a>', readme)

# 2. Update section headers
readme = re.sub(r'## <picture>.*?</picture>&nbsp;(.*)', r'## \1', readme)
readme = readme.replace('## About Me', f'## {img("header-user", 28)}&nbsp;About Me')
readme = readme.replace('## Technical Skills', f'## {img("header-wrench", 28)}&nbsp;Technical Skills')
readme = readme.replace('## Featured Projects', f'## {img("header-rocket", 28)}&nbsp;Featured Projects')
readme = readme.replace('## Achievements & Presentations', f'## {img("header-trophy", 28)}&nbsp;Achievements & Presentations')

# 3. Update Technical Skills
readme = re.sub(r'\*\s*<picture>.*?</picture>\s*\*\*Languages & Frameworks:\*\*', f'*   {img("skill-code", 20)} **Languages & Frameworks:**', readme)
readme = re.sub(r'\*\s*<picture>.*?</picture>\s*\*\*Databases & DevOps:\*\*', f'*   {img("skill-database", 20)} **Databases & DevOps:**', readme)
readme = re.sub(r'\*\s*<picture>.*?</picture>\s*\*\*Networking & Professional:\*\*', f'*   {img("skill-network", 20)} **Networking & Professional:**', readme)

# 4. Update Projects and Tech Stacks
readme = re.sub(r'\*\s*<picture>.*?</picture>\s*Implemented authentication', f'*   {img("bullet-project", 18)} Implemented authentication', readme)
readme = re.sub(r'\*\s*<picture>.*?</picture>\s*Developed Elvan Agazhi', f'*   {img("bullet-project", 18)} Developed Elvan Agazhi', readme)
readme = re.sub(r'\*\s*<picture>.*?</picture>\s*Deployed the web application', f'*   {img("bullet-project", 18)} Deployed the web application', readme)
readme = re.sub(r'\*\s*<picture>.*?</picture>\s*Developed a custom window', f'*   {img("bullet-project", 18)} Developed a custom window', readme)
readme = re.sub(r'\*\s*<picture>.*?</picture>\s*Integrated projects, certifications', f'*   {img("bullet-project", 18)} Integrated projects, certifications', readme)
readme = re.sub(r'\*\s*<picture>.*?</picture>\s*Built a modular content', f'*   {img("bullet-project", 18)} Built a modular content', readme)

readme = re.sub(r'\*\s*<picture>.*?</picture>\s*\*\*Tech Stack:\*\*', f'*   {img("bullet-stack", 18)} **Tech Stack:**', readme)

# 5. Update Achievements
readme = re.sub(r'\*\s*<picture>.*?</picture>\s*\*\*COULOMB 2025', f'*   {img("bullet-award", 20)} **COULOMB 2025', readme)
readme = re.sub(r'\*\s*<picture>.*?</picture>\s*\*\*KalaQuest', f'*   {img("bullet-award", 20)} **KalaQuest', readme)
readme = re.sub(r'\*\s*<picture>.*?</picture>\s*\*\*ARTC-23', f'*   {img("bullet-award", 20)} **ARTC-23', readme)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme)

print("Samsung Gradient Icons upgrade complete!")
