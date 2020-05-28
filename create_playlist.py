"""Create playlist (m3u) files for all audio files in a folder."""
import argparse
from pathlib import Path


def main(music_folders=None, music_folder_parent=None):
    if not music_folders:
        if music_folder_parent:
            music_folders = list(Path(music_folder_parent).glob('*'))
        else:
            music_folders = list(Path(__file__).parent.glob('*'))
        music_folders = [x for x in music_folders if x.is_dir()]
    else:
        music_folders = [Path(music_folders)]

    for fold in music_folders:
        if not Path.exists(fold):
            print(f'{fold} does not exist. Hint: check your back-slash "\\" and front-slash "/"')
            continue

        songs_in_folder = list(fold.glob('*.mp3'))
        if not songs_in_folder:
            songs_in_folder = list(fold.glob('*.flac'))
        if not songs_in_folder:
            songs_in_folder = list(fold.glob('*.m4a'))

        if songs_in_folder:
            songs_in_folder = [(x.name + '\n') for x in songs_in_folder]
            try:
                with open(str(fold / (str(fold.name) + '.m3u')), 'w', encoding="utf-8") as fn:
                    fn.writelines(songs_in_folder)
            except UnicodeEncodeError as err:
                print(f'{err}')
                print(f'Check that the file names do not have any special character.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create playlist (m3u) files for all audio files in a folder.')
    #parser.add_argument('--in_folder', dest="in_folder",
    #                    help='Path to folder containing audio files to add to playlist.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--in_folder', dest="in_folder",
                        help='Path to folder containing audio files to add to playlist.')
    group.add_argument('--in_folder_parent', dest="in_folder_parent",
                       help='Path to folder containing folders '
                            'with audio files to add to playlist.')

    args = parser.parse_args()
    if main(args.in_folder, args.in_folder_parent) != 0:
        exit(1)

    exit(0)
