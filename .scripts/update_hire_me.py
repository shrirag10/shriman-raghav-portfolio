import glob
import re

files = glob.glob("*.html")
for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # Replace href="index.html#contact" with href="assets/resumes/General_Manufacturing.pdf" target="_blank" if followed by ... >Hire Me
    new_content = re.sub(r'href="index\.html#contact"([^>]*>Hire Me)', r'href="assets/resumes/General_Manufacturing.pdf" target="_blank"\1', content)
    
    # Also if the href is just "#contact" for files like index.html (if they exist)
    new_content = re.sub(r'href="#contact"([^>]*>Hire Me)', r'href="assets/resumes/General_Manufacturing.pdf" target="_blank"\1', new_content)
    
    if new_content != content:
        with open(f, "w") as file:
            file.write(new_content)
        print(f"Updated {f}")
