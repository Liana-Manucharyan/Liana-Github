import os   


def delete_files(file_names):
    try:
        for file_name in file_names:
            if os.path.exists(os.path.join(os.path.dirname(__file__), file_name)):
                confirm = input(f"Do you want to remove '{file_name}' file? (yes/no): ")
                if confirm.lower() == "yes":             
                    os.remove(os.path.join(os.path.dirname(__file__), file_name)) 
                    print(f"'{file_name}' file has been deleted.")
                elif confirm.lower() == "no":
                    print(f"'{file_name}' file hasn't been deleted.")

                else: 
                    print(f"'{file_name}' file hasn't been deleted, because of incorrect input.")

            else:
                print(f"'{file_name}' file doesn't exist.")
    except Exception as e:
        print(f"Error occured while deleting file. Exception: {e}")
        