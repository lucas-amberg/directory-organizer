import os

def clean_extensions(extension_list):
    extension_list = extension_list.split(",")
    for i, item in enumerate(extension_list):
        extension_list[i] = item.lower()
        for char in extension_list[i]:
            if char not in "abcdefghijklmnopqrstuvwxyz":
                extension_list[i] = extension_list[i].replace(char, "")

def clean_directory(extension_list, current_dir):
    skipped_list = []
    os.chdir(current_dir)
    print("\nDirectory clean in progress...\n")
    print("Skipping files with extension " + extension_list+"\n")
    for file in os.listdir():
        if "." not in file:
            continue
        else:
            extension = file.split(".")[-1]
            if extension.lower() in extension_list:
                skipped_list.append(file)
                continue
            elif extension.upper() in os.listdir():
                os.rename(file, f"{current_file_path}\\{extension.upper()}\\{file}")
            elif extension.upper() not in os.listdir():
                os.mkdir(f"{current_file_path}\\{extension.upper()}")
                os.rename(file, f"{current_file_path}\\{extension.upper()}\\{file}")
    print("Clean success!\n")
    print(f"Files skipped:{skipped_list}\n")

    


current_file_path = __file__[0:-1*len((__file__.split("\\"))[-1])]

print("Hello, it seems you want to clean your files?\n")
print("Are there any filetypes you want ignored? Enter their extension below as a comma separated list")
ignored_files = input("File extensions (eg: pdf,jpg,png):")
clean_extensions(ignored_files)

clean_directory(ignored_files, current_file_path)
