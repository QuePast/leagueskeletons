import os
import subprocess

# Specify the path to the base directory where the champion folders are located
base_path = r'C:\Users\Admin\Desktop\bone\proc\assets\characters'

# Path to lol2gltf.CLI.exe
lol2gltf_path = r'lol2gltf.CLI.exe'

# Loop through champion folders
for champion_folder in os.listdir(base_path):
    champion_path = os.path.join(base_path, champion_folder)
    if os.path.isdir(champion_path):
        base_skin_path = os.path.join(champion_path, 'skins', 'base')
        
        if os.path.exists(base_skin_path):
            for file in os.listdir(base_skin_path):
                if file.lower().endswith('.skn'):
                    skn_file_path = os.path.join(base_skin_path, file)
                    skl_file_path = skn_file_path.replace('.skn', '.skl')
                    if os.path.exists(skl_file_path):
                        champion_name = champion_folder.lower()  # Adjust the champion name if needed
                        print(champion_name)
                        output_path = f"C:\\Users\\Admin\\Desktop\\bone\\proc\\output\\{champion_name}"
                        
                        cmd_args = [
                            lol2gltf_path,
                            'skn2gltf',
                            '--skn', skn_file_path,
                            '--skl', skl_file_path,
                            '--gltf', output_path
                        ]
                        
                        subprocess.run(cmd_args, shell=True, check=True)
                        print("Conversion complete.")
