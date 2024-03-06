import argparse
import os
import shutil

def new_list(file_path):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    if file_path[-1] == '/':
        file_path = file_path[:-1]
    for dirpath, dirnames, filenames in os.walk(file_path):
        print(f'{type(filenames)} - {filenames}')
        files = ','.join(filenames)
        break
    with open(os.path.join(script_dir, 'rom_list.txt'), 'w') as rom_list:
        rom_list.write(files)
    print('rom_list.txt had been created')

def move_roms(file_paths):
    source, dest = file_paths
    script_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_dir, 'rom_list.txt'),'r') as rom_list: 
        files = rom_list.read().split(',')
    for rom in files:
        try:
            shutil.copy(os.path.join(source, rom), os.path.join(dest, rom))
            print(f'Copied {rom} to {dest}')
        except:
            print(f'Could not copy {rom}')

def remove_roms(file_path):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_dir, 'delete_list.txt'),'r') as rom_list: 
        files = rom_list.read().split(',')
    patterns = [
        ('videos/', '.mp4'),
        ('manuals/', '.pdf'),
        ('manuals/', '.jpg'),
        ('images/', '-boxback.png'),
        ('images/', '-fanart.png'),
        ('images/', '-image.png'),
        ('images/', '-marquee.png'),
        ('images/', '-thumb.png'),
        ('', '.zip')]
    for rom in files:
        for pattern in patterns:
            file = f'{pattern[0]}{rom.partition(".")[0]}{pattern[1]}'
            print (file)

def delete_file(file, file_path):
    if os.path.isfile(file):
        os.remove(file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''
    Mame file names are obtuse and going through them sucks.
    This tool makes a list of your roms so that after you update your romset,
    only the games  in the list move- meaning you only have to go through the hassle of deciphering names once.
    Run --ls on your rom folder to make a list of your roms.
    Run --cp the next time you update your romset to copy only your selected games into your rom folder.
    Run --rm to delete roms along with frontend art for emulation station/batocera. 
    First make a list formated the same way as rom_list.txt in the same folder as this script named delete_list.txt
    ''')
    parser.add_argument('--ls',
                        help='''Generate a new rom list.
                        mamo.py --ls /source/path''')
    parser.add_argument('--cp',
                        nargs='+',
                        help='''Move roms that are in the existing rom list. 
                        mamo.py --mv /source/path /destination/path''')
    parser.add_argument('--rm',
                        help='''Remove roms that are in delete_list.txt and in folder.
                        mamo.py --rm /file/path/to/mame''')

    args = parser.parse_args()

    if args.ls:
        new_list(args.ls)

    if args.cp:
        move_roms(args.cp)
    
    if args.rm:
        remove_roms(args.rm)