import re

readme_path = 'D:/Projects/ElvanParthasarathy/README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

# 1. Update contact links
readme = readme.replace('email-svgrepo-com.svg', 'ph-email.svg')
readme = readme.replace('linkedin-svgrepo-com.svg', 'ph-linkedin.svg')
readme = readme.replace('github-142-svgrepo-com.svg', 'ph-github.svg')
readme = readme.replace('location-pin-filled-svgrepo-com.svg', 'ph-globe.svg')

# 2. Add section headers
def create_icon_html(icon_name):
    return f"""<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/{icon_name}-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/{icon_name}-light.svg">
  <img alt="icon" src="./assets/{icon_name}-light.svg" width="24" height="24" align="center">
</picture>&nbsp;"""

readme = readme.replace('## About Me', f'## {create_icon_html("ph-user")}About Me')
readme = readme.replace('## Technical Skills', f'## {create_icon_html("ph-wrench")}Technical Skills')
readme = readme.replace('## Featured Projects', f'## {create_icon_html("ph-rocket")}Featured Projects')
readme = readme.replace('## Achievements & Presentations', f'## {create_icon_html("ph-trophy")}Achievements & Presentations')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme)

print("Updated README with Phosphor icons!")
