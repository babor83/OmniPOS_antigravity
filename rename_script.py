import os

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return

    original_content = content
    content = content.replace('omnipos', 'omnipos')
    content = content.replace('omniPOS', 'omniPOS')
    content = content.replace('omniPOS', 'omniPOS')
    content = content.replace('omniPOS', 'omniPOS')
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

def main():
    directory = '.'
    exclude_dirs = {'.git', 'node_modules', '.github', 'env', '__pycache__', '.pytest_cache'}
    valid_extensions = {'.py', '.js', '.ts', '.vue', '.json', '.toml', '.txt', '.csv', '.md', '.html', '.css', '.scss', '.yaml', '.yml'}
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in valid_extensions or file in {'package.json', 'pyproject.toml', 'modules.txt', 'patches.txt'}:
                filepath = os.path.join(root, file)
                replace_in_file(filepath)

if __name__ == "__main__":
    main()
