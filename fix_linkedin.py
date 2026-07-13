import os
import re

assets_dir = 'D:/Projects/ElvanParthasarathy/assets'

linkedin_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>'

color1, color2 = ('#0077B5', '#00A0DC')

match = re.search(r'<svg[^>]*>(.*)</svg>', linkedin_svg, re.DOTALL)
inner_content = match.group(1) if match else ""

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

with open(os.path.join(assets_dir, f"contact-linkedin.svg"), 'w', encoding='utf-8') as f:
    f.write(new_svg)

# Also ensure it uses just contact-linkedin.svg in README
readme_path = 'D:/Projects/ElvanParthasarathy/README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

# Since generate_samsung_icons.py might have skipped the replacement if it was using the old regex, let's make sure it's updated.
readme = re.sub(r'<a href="https://linkedin.*?</a>', f'<a href="https://linkedin.com/in/jaiprakashpartha"><img alt="contact-linkedin" src="./assets/contact-linkedin.svg" width="34" height="34" align="center"></a>', readme)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme)
