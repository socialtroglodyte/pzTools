import os
import shutil

dir = f"C:\\Users\\{os.getlogin()}\\Zomboid\\Mods"
cancel = "-b"

class main:

    global dir

    while True:

        def newMod():
            if 'dir' not in globals():
                path = input("Enter the path of your directory: ")
            else:
                path = dir
            folder = input("Enter the name of your mod: ")
            modID = input(str("Enter the ID for your mod: "))
            poster = input("Enter the image path for your poster: ")
            description = input(str("Provide a description for your mod: "))

            if os.path.exists(path):
                os.chdir(path)
                os.mkdir(folder)

                dest = f"{path}\\{folder}"

                os.chdir(dest)
                shutil.copy(poster, dest)
                os.rename(poster, 'poster.png')
                open("mod.info", 'w').write(f"name={folder}\nposter=poster.png\nid={modID}\ndescription={description}")

                print(f"{folder} has been created successfully in {path}.")
            else:
                print(f"Error: Could not create '{folder}'. Directory '{path}' may be incorrect or may not exist")

        def delMod():
            os.system('cls')
            for folder in os.listdir(dir):
                if os.path.exists(f'{os.path.join(dir, folder)}\\mod.info'):
                    print(f"{folder}")

            target = input(f"Enter the name of the mod you want to delete (Type {cancel} to go back): ")

            if os.path.exists(f"{dir}\\{target}"):
                shutil.rmtree(f"{dir}\\{target}")
                print(f"Mod {target} has been deleted successfully.")
            elif target == str(0):
                os.system('cls')
            else:
                print(f"Error: Could not delete '{target}'. Given folder name may be incorrect or does not exist.")

        def viewMods():
            os.system('cls')
            for folder in os.listdir(dir):
                if os.path.exists(f'{os.path.join(dir, folder)}\\mod.info'):
                    print(f"{folder}")
            user = input(f"Type {cancel} to go back: ")
            if user == str(0):
                os.system('cls')

        print(f"Target directory: {dir}")
        print("PZTOOLS 0.1.3-B4")
        print("1. Create New Mod")
        print("2. Delete Existing Mod")
        print("3. View Existing Mods")
        user = input("Select a program (integer): ")

        if user == str(1):
            newMod()
        if user == str(2):
            delMod()
        if user == str(3):
            viewMods()
        if user == "cls":
            os.system('cls')