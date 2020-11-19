def os_check():
    """
    [Check operating system]
    """
    from sys import platform

    if platform == "darwin":
        print("macOS")
    elif platform == "win32":
        print("Windows")
    elif platform == "linux" or platform == "linux2":
        print("Linux")
    else:
        print("Oops! Something went wrong.")


def path_checker(path):
    """
    [Check if path is a file or directory]

    Args:
        path ([str]): [File or folderpath]

    Returns:
        [bool]: [True/False]
    """
    from pathlib import Path
    path = Path(path)

    if path.exists():
        if path.is_dir():
            print(f"'{path}' is directory")
        else:
            if path.is_file():
                print(f"'{path}' is a file")
        return True

    else:
        print(f"'{path}' does not exist.")
        return False


def unpack_list(lst):  # Oxford comma
    """
    [Unpack list and return with Oxford comma]

    Args:
        lst ([list]): [List to unpack]

    Returns:
        [string]: [Unpacked list as a string]
    """
    if not isinstance(lst, str):
        lst = [str(item) for item in lst]
    if len(lst) == 0:
        return
    if len(lst) == 1:
        return ", ".join(lst)
    if len(lst) == 2:
        return ", and ".join(lst)
    else:
        first_part = lst[:-1]
        last_part = lst[-1]
        return ", ".join(first_part) + ", and " + last_part
