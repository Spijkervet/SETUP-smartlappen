import os
from mido import MidiFile
from glob import glob
if __name__ == "__main__":
    CUSTOM_DIR = "./data/custom"
    if not os.path.exists(CUSTOM_DIR):
        os.makedirs(CUSTOM_DIR)

    files = glob("./data/orders/**/*GM.MID")
    for f in files:
        fn = os.path.basename(f)
        #if "v" not in fn and "_" not in fn:
        if "_" in fn:
            mid = MidiFile(f)

            track_name = None
            for i, track in enumerate(mid.tracks):
                if len(track.name) > 12:
                    track_name = track.name
                # print('Track {}: {}'.format(i, track.name))
                if "piano" in track.name.lower():
                    piano_mid = MidiFile()
                    piano_mid.tracks.append(track)
                    piano_mid.save(os.path.join(CUSTOM_DIR, "{}_piano.mid").format(os.path.splitext(fn)[0]))
                    print("Extracting {}".format(track_name))
                    break
