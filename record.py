#!/usr/bin/env python

import subprocess
import datetime
import os

ROOT_PATH = "/home/pi/recordings"
DATE_FMT = "%Y_%m_%d_%H_%M_%S"
SEGMENT_TIME = 30
ENCODING = "copy"

new_dir = datetime.datetime.now().strftime(DATE_FMT)

recording_path = os.path.join(ROOT_PATH, new_dir)
os.mkdir(recording_path)

segments_path = os.path.join(recording_path, "%03d.avi")

command = "ffmpeg -i /dev/video0 -c:v {} -an -sn -dn -segment_time {} -f segment -reset_timestamps 1 {}".format(ENCODING, SEGMENT_TIME, segments_path)

subprocess.call(command, shell=True)
