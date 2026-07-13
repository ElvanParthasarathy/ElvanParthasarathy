import re

readme_path = 'D:/Projects/ElvanParthasarathy/README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

# Replace any <img alt="skill-...> or <img alt="bullet-...> with a standard markdown bullet '*   '
# We will use regex to catch the whole image tag and any trailing spaces.
readme = re.sub(r'<img alt="(?:skill|bullet)-[^>]+>\s*', '*   ', readme)

# Note: In our previous step, we added extra newlines between some of these.
# If they are standard markdown bullets, GitHub will render them perfectly whether they have a newline or not,
# but it's cleaner to leave the formatting as is.

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme)

print("Reverted custom bullet icons back to standard markdown bullets!")
