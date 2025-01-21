import os
import shutil
from markdown import markdown_to_hmtl_node

def main():
    recursive_copy("static", "public")

    generate_pages_recursive("content", "template.html", "public")
    return

def recursive_copy(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.makedirs(destination)

    for item in os.listdir(source):
        if os.path.isfile(f"{source}/{item}"):
            shutil.copy2(f"{source}/{item}", f"{destination}/{item}")
        else:
            recursive_copy(f"{source}/{item}", f"{destination}/{item}")

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith('# '):
            return line[1:].strip()
    raise Exception('No title')

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r', encoding="utf-8") as f:
        content = f.read()
    with open(template_path, 'r', encoding="utf-8") as f:
        template = f.read()

    node = markdown_to_hmtl_node(content)
    string = node.to_html()

    title = extract_title(content)

    new_template = template.replace("{{ Title }}", title).replace("{{ Content }}", string)

    with open(dest_path, 'w',  encoding="utf-8") as f:
        f.write(new_template)
    

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        if os.path.isfile(f"{dir_path_content}/{item}"):
            generate_page(f"{dir_path_content}/{item}", template_path, f"{dest_dir_path}/{item.replace('md', 'html')}")
        else:
            os.makedirs(f"{dest_dir_path}/{item}")
            generate_pages_recursive(f"{dir_path_content}/{item}", template_path, f"{dest_dir_path}/{item}")
main()