import os
#links = ["about", "blog", "contact", "home", "portfolio", "pricing", "resume", "services", "sidebar", "testimonials"]
#about, blog, contact, home, portfolio, pricing, resume, services, sidebar,testimonials

# Get input names separated by commas
folder_names = input("Enter folder names (separated by commas): ").split(",")
create_output_folder = input("Do you want to create an output folder? (y/n): ").lower() == "y"

if create_output_folder:
    output_folder_name = input("Enter output folder name: ")
    os.mkdir(output_folder_name)
else:
    output_folder_name = ""

for folder_name in folder_names:
    folder_name = folder_name.strip()
    os.mkdir(os.path.join(output_folder_name, folder_name))

    jsx_file_name = os.path.join(output_folder_name, folder_name, f"{folder_name.capitalize()}.jsx")

    css_file_name = os.path.join(output_folder_name, folder_name, f"{folder_name}.css")

    with open(jsx_file_name, 'w') as jsx_file:
        jsx_file.write("import React from 'react';\n\n")
        jsx_file.write("export const " + folder_name.capitalize() + " = () => {\n")
        jsx_file.write("  return (\n")
        jsx_file.write("    <div>\n")
        jsx_file.write("      " + folder_name.capitalize() + "\n")
        jsx_file.write("    </div>\n")
        jsx_file.write("  )\n")
        jsx_file.write("}\n")
        jsx_file.write("\n")
        jsx_file.write("export default " + folder_name.capitalize() + ";\n")

    with open(css_file_name, 'w') as css_file:
        css_file.write("/* CSS code goes here */\n")