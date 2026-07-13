import os

assets_dir = 'D:/Projects/ElvanParthasarathy/assets'

linkedin_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>'

def wrap_in_ios_squircle(svg_data, mode):
    bg_color = '#ffffff' if mode == 'dark' else '#181717'
    icon_color = '#181717' if mode == 'dark' else '#ffffff'
    
    import re
    match = re.search(r'<svg[^>]*>(.*)</svg>', svg_data, re.DOTALL)
    inner_content = match.group(1) if match else ""
    
    new_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 34 34">
    <rect x="0" y="0" width="34" height="34" rx="8" ry="8" fill="{bg_color}"/>
    <g transform="translate(5, 5)" fill="{icon_color}">
        {inner_content}
    </g>
</svg>"""
    return new_svg

dark_svg = wrap_in_ios_squircle(linkedin_svg, 'dark')
with open(os.path.join(assets_dir, f"contact-linkedin-dark.svg"), 'w', encoding='utf-8') as f:
    f.write(dark_svg)
    
light_svg = wrap_in_ios_squircle(linkedin_svg, 'light')
with open(os.path.join(assets_dir, f"contact-linkedin-light.svg"), 'w', encoding='utf-8') as f:
    f.write(light_svg)

print("Fixed LinkedIn icon!")
