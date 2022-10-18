from rembg import remove
from PIL import Image
from easygui import fileopenbox,diropenbox,msgbox
from re import findall

class data():
    si_msg = ""
    si_title = ""
    si_default = ""
    si_filetype = ["*.png","*.jpg"]
    si_multiple = True

    simb_msg = "The format of these files is not supported\n"
    simb_title = ""

    sof_msg = ""
    sof_title = ""
    sof_default = ""





def select_image():
    file_list = fileopenbox(msg=data.si_msg,title=data.si_title,default=data.si_default,filetypes=data.si_filetype,multiple=data.si_multiple)
    image_list = []
    not_image_list = []

    for loop_check_format in file_list:
        if "*" + loop_check_format[-4:] in data.si_filetype:
            image_list.append(loop_check_format)
        else:
            not_image_list.append(loop_check_format)
    if len(not_image_list) != 0:
        msgbox(msg=data.simb_msg +("\n").join(not_image_list),title=data.simb_title)

    if len(image_list)  == 0:
        return False

    return file_list

def select_output_folder():
    output_folder = diropenbox(msg=data.sof_msg, title=data.sof_title, default=data.sof_default)
    if output_folder == None:
        return False
    return output_folder

def remove_background(list_image, output_folder_path):
    for loop_image in list_image:
        output_image_path = output_folder_path +"\\\\"+ findall(".*\\\\(.*)\..*",loop_image)[0] + "_output" + ".png"
        input_image = Image.open(loop_image)
        output_image = remove(input_image)
        output_image.save(output_image_path)
    return 0




# input_path = "test/2.jpg"
# output_path = "test/2_out.png"

# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)


def main():
    list_input_images = select_image()
    if list_input_images == False:
        return 0
    print(list_input_images)
    output_folder_path = select_output_folder()
    if output_folder_path == False:
        return 0
    print(output_folder_path)

    remove_background(list_input_images, output_folder_path)

if __name__ == "__main__":
    main()