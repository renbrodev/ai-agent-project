import os

def get_files_info(working_directory, directory="."):
    info_dump = ""

    try:
        wd_absolute = os.path.abspath(working_directory)

        target_directory = os.path.normpath(os.path.join(wd_absolute, directory))

        valid_target_directory = os.path.commonpath([wd_absolute, target_directory]) == wd_absolute

        # Better to put this first so as to not nec confirm the existence of the directory to someone via filesystem check
        # In a more secure iteration the message could be vaguer (access denied or somesuch) but since we in this case
        # want the LLM to have an idea of where it oopsied we keep the message somewhat descriptive
        if not valid_target_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'

        # REMOVE BEFORE FLIGHT
        # print(target_directory)

        td_list = os.listdir(path=target_directory)

        # REMOVE BEFORE FLIGHT
        # print(f"td_list: {td_list}")
        
        for item in td_list:

            item_path = os.path.join(target_directory, item)
            is_dir = os.path.isdir(item_path)
            # REMOVE BEFORE FLIGHT (IF UNUSED)
            # is_file = os.path.isfile(item_path)
            file_size = os.path.getsize(item_path)
            
            # REMOVE BEFORE FLIGHT
            """
                print(f"item: {item}")
                print(f"item path: {item_path}")
                print(f'isdir: {is_dir}')
                print(f'isfile: {is_file}')
                print(f'filesize: {file_size}')
            """
            
            info_dump = info_dump + "- " + item + ": file_size=" + str(file_size) + " bytes, is_dir=" + str(is_dir) + "\n"
            
            # Or, if you like yourself, you could have used the below...
            # REMOVE BEFORE FLIGHT
            # info_dump += f"- {item}: file_size={file_size} bytes, is_dir={is_dir}\n"

        # REMOVE BEFORE FLIGHT
        # print(info_dump)
    
    except Exception as e:
        return f"Error: {e}"

    return info_dump
    
    # REMOVE BEFORE FLIGHT
    # return (target_directory, valid_target_directory)

# REMOVE BEFORE FLIGHT
def main():
    print(get_files_info("calculator", "pkg"))

# REMOVE BEFORE FLIGHT
main()
