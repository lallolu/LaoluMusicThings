"""Create playlist (m3u) files for all audio files in a folder."""
import argparse
from pathlib import Path


def main(music_folders=None):
    if not music_folders:
        #music_folders = list(Path(__file__).parent.glob('*'))
        music_folders = list(Path(__file__).parent.glob('Naija_2019'))
        music_folders = [x for x in music_folders if x.is_dir()]

    songs_in_folder = []
    for fold in music_folders:
        songs_in_folder = list(fold.glob('*.mp3'))
        if not songs_in_folder:
            songs_in_folder = list(fold.glob('*.flac'))
        songs_in_folder = [(x.name + '\n') for x in songs_in_folder]

        with open(str(fold / (str(fold.name) + '.m3u')), 'w') as fn:
            fn.writelines(songs_in_folder)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create playlist (m3u) files for all audio files in a folder.')
    parser.add_argument('--in_folder', dest="in_folder",
                        help='Path to folder containing audio files to add to playlist.')
    args = parser.parse_args()
    main(args.in_folder)

    #if main(args.in) != 0:
    #    sys.exit(1)

    sys.exit(0)


