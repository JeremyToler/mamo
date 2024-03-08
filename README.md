## Mamo: Your Friendly Mame File Mover

This Python script simplifies updating your Mame ROM collection by automating the creation and utilization of a simple ROM list.
This script is for you if you have a merged subset of MAME ROMs for a front-end (Batocera, Emulation Station, PegasusFE, etc..) and you are hesitant to update MAME because you don't want to manually copy each ROM from a full set to your front-ends folder again.

This tool does not help you update a ROMset, or convert between merged and non-merged sets. 
This does not work on CHD's yet. I might update it later. 

**Features:**

* Generates a list of all ROMs within a specified directory.
* Copies only the listed ROMs to your desired destination, saving you time and effort when updating your ROMset.

**Installation:**

1. Save the script as `mamo.py`.
2. Ensure Python is installed on your system.

**Usage:**

**Generate a new ROM list:**

```
python mamo.py --ls /path/to/your/roms
```

**Move listed ROMs to a new location:**

```
python mamo.py --cp /path/to/source/roms /path/to/destination
```

**Arguments:**

* `--ls`: Generates a new ROM list from the specified directory.
* `--cp`: Copies ROMs listed in the existing `rom_list.txt` file from the source to the destination directory.
* `--cpchd`: Copies CHDs directories listed in the existing `rom_list.txt` file from the source to the destination directory.
* `--rm`: Deletes ROMs and scrapped art listed in `delete_list.txt` file. File must be created in this scripts root directory and needs to be a list of the rom's file names seperated by a comma. The art that is deleted matches the Emulation Station/Batocera file paths. 

**Notes:**

* The script creates a file named `rom_list.txt` in the same directory as itself. This file stores the list of ROMs.
* Ensure you have the necessary permissions to access and modify files in the specified directories.

**Example:**

1. Run `python mamo.py --ls //Batocera/Share/roms/mame` to create a list of all ROMs in your `//Batocera/Share/roms/mame` directory.
2. After updating your ROMset, run `python mamo.py --cp D:\mame\mame_0.252(merged) //Batocera/Share/roms/mame` to copy only the listed ROMs from the full set to your frontends Mame ROM folder.

This script aims to streamline your Mame ROM management process, allowing you to focus on enjoying your favorite classic games!

