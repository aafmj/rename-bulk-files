# Python 3 code to rename multiple files in same directory

# by default only images (.jpg, .png, .jpeg)
# that have time ((year, month, day, hour, minute, second) are required)
# in there name like (screen_shot_2020-02-02_12-25-31) will be renamed to just "date" like (2020-02-02_12-25-31)
# files that have not full date (2020-02-02_12-25-31) in there name (like 'abc32154efg') will not change
# but there is an exception. (refer to 'note' of 'is_valid_filename' method description)

# here is some examples:
# 'Annotation 2020-10-13 121750.png' => '2020-10-13_12-17-50.png'
# 'Screenshot_20151013-111412.jpg' => '2015-10-13_11-14-12.jpg'
# 'Image_14' => won't change (because a date format not found)

# here is an example of app harm: (be careful)
# 'person_with_id_20181013111412.png' => '2018-10-13_11-14-12.png'
# so just work with files that created with date included in name format like
# phone camera picturs, screen shots and ...! (if you change reqired extension to somthing like '.mp4' it works too)

# 'person_with_id_20501013111412.png' => won't change (because date format does not make sense if you are in 2020)


# Files renamed by this program could not be undo so create a back up before run :))))


# importing os module to work with operating system
import os
# importing datetime module to get current time
import datetime

# to generate random number
import random


# Function to rename multiple files
def main():
    for primitive_filename in os.listdir("."):

        filename_extension = get_filename_extension_or_none(primitive_filename)
        if filename_extension is None:
            continue
        filename = ''
        for char in primitive_filename:
            if char.isdigit():
                filename += char
        if is_valid_filename(filename):
            new_filename = format_filename(filename) + filename_extension

            # rename() function will
            # rename all the files
            try:
                os.rename(primitive_filename, new_filename)
            except OSError:
            # handle duplicate filenames
                try:
                    new_filename = new_filename.replace('.', '_' + str(random.randint(1000, 9999)) + '.')
                    os.rename(primitive_filename, new_filename)
                except OSError:
                # leave if any other error occurred
                    pass


def get_filename_extension_or_none(filename):
    """
    :param filename:
    full file name including extension.

    :return:
    return the extension of file if it exists in required extension list (see 'get_required_extension_list()') or return None.
    """
    for required_extension in get_required_extension_list():
        if filename.endswith(required_extension):
            return required_extension
    return None


def get_required_extension_list():
    """
    Only these types of file well be processed
    """
    required_extension_list = ['.jpg', '.png', '.jpeg']
    return required_extension_list


def is_valid_filename(filename):
    """
    :param filename: get just date part (and numbers after that if exists) like : '20201211201014' or '20201211201014001'
    :return: True if a real date can be generated from filename, False if can not.

    note: if filename consists of numbers that are not date (like a id or code) but
          very similar to a date like '20201211201014' could be assume valid wrongly
          so just run this file if you sure there are not such that files and
    """
    if filename:
        date = filename[:8]
        time = filename[8:14]

        # validate date and time
        if len(date) == 8 \
                and 2000 <= int(date[:4]) <= datetime.datetime.now().year \
                and 0 < int(date[4:6]) <= 12 \
                and 0 < int(date[6:8]) <= 31:
            if len(time) == 6 \
                    and 0 <= int(time[:2]) <= 23 \
                    and 0 <= int(time[2:4]) <= 59 \
                    and 0 <= int(time[4:5]) <= 59:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def format_filename(filename):
    """

    :param filename: get validated filename
    :return: return formatted form, examples:
    20201211201014 => 2020-12-11_20-10-14
    20201211201014001 => 2020-12-11_20-10-14_001
    """
    formatted_filename = filename[:4] + '-' + filename[4:6] + '-' + filename[6:8] + '_' + \
                         filename[8:10] + '-' + filename[10:12] + '-' + filename[12:14]
    if filename[14:]:
        formatted_filename += '_' + filename[14:]

    return formatted_filename


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
