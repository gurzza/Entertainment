import os


def find_file(search_name, current_path, deep=1, current_deep=0):
    res = None
    if deep == current_deep:
        return None

    if os.path.isfile(current_path):
        last_element = current_path.split(os.sep)[-1]
        if last_element == search_name:
            return current_path
        else:
            return None

    try:
        folder_content = os.listdir(current_path)
        for folder_item in folder_content:
            current_item = os.path.join(current_path, folder_item)
            res = find_file(search_name, current_item, deep, current_deep + 1)
            if res is not None:
                break

    except PermissionError:
        pass

    return res
