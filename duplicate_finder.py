import pyperclip


def find_rem_duplicates(prowided_text, separator) -> str:
    """Simple duplicate finding function"""
    work_list = prowided_text.split(separator)
    work_list = [elem.strip() for elem in work_list ]
    work_list = list(dict.fromkeys(work_list))
    print(work_list)
    final_str = f"{separator} ".join(work_list)
    pyperclip.copy(final_str)
    print("This is your final text with no duplicates it should be copied to the clipboard " + final_str + " ")
    return final_str
    

text_w_dup =  input("Provide text to find duplicates: ")
separator = input("Provide separator sign: ")
find_rem_duplicates(prowided_text=text_w_dup, separator=separator)
input("press any key to close")