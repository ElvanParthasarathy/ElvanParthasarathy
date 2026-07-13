import re

readme_path = 'D:/Projects/ElvanParthasarathy/README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

# Remove the markdown bullet '*   ' from lines that contain our custom icons
# The pattern looks for a literal '*   ' followed by '<img alt="'
# We will just replace '*   <img' with '<img'
readme = readme.replace('*   <img', '<img')

# We need to ensure that these items don't merge into a single line if they were contiguous list items.
# In markdown, contiguous list items are separated by a newline. But standard paragraphs need two newlines.
# Let's replace single newlines between these new image-paragraphs with double newlines.
# A simple way: find lines starting with <img, and ensure there's a blank line before them.
# Actually, it's safer to just split the file by lines and ensure spacing.
lines = readme.split('\n')
new_lines = []
for i, line in enumerate(lines):
    if line.startswith('<img alt='):
        # ensure previous line is blank if it's also a paragraph or image
        if i > 0 and new_lines[-1].strip() != '' and not new_lines[-1].startswith('##') and not new_lines[-1].startswith('1.') and not new_lines[-1].startswith('2.') and not new_lines[-1].startswith('3.'):
            new_lines.append('')
    new_lines.append(line)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Fixed double bullets!")
