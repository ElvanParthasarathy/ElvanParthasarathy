import os
import re

assets_dir = 'D:/Projects/ElvanParthasarathy/assets'

# The exact, solid original brand colors
solid_colors = {
    'contact-email': '#EA4335',     # Original Gmail Red
    'contact-linkedin': '#0077B5',  # Original LinkedIn Blue
    'contact-github': '#181717',    # Original GitHub Black
    'contact-globe': '#0F9D58',     # Original Vibrant Green
    
    'header-user': '#3F51B5',       # Deep Indigo
    'header-wrench': '#0097A7',     # Deep Cyan
    'header-rocket': '#F57C00',     # Deep Orange
    'header-trophy': '#FFA000',     # Deep Amber
}

def convert_to_solid(filepath, color):
    with open(filepath, 'r', encoding='utf-8') as f:
        svg_data = f.read()
    
    # We want to replace the <defs> and gradient fill with a solid fill
    # The current structure has:
    # <defs> ... </defs>
    # <circle cx="24" cy="24" r="24" fill="url(#grad)"/>
    
    # Remove defs entirely
    svg_data = re.sub(r'<defs>.*?</defs>', '', svg_data, flags=re.DOTALL)
    
    # Replace the circle fill with the solid color
    svg_data = re.sub(r'<circle cx="24" cy="24" r="24" fill="url\(#grad\)"/>', f'<circle cx="24" cy="24" r="24" fill="{color}"/>', svg_data)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_data)

for name, color in solid_colors.items():
    filepath = os.path.join(assets_dir, f"{name}.svg")
    if os.path.exists(filepath):
        try:
            convert_to_solid(filepath, color)
            print(f"Converted {name} to solid brand color.")
        except Exception as e:
            print(f"Failed {name}: {e}")
