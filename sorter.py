#!/usr/bin/env python
import argparse, os
from os.path import join, getsize


parser = argparse.ArgumentParser(description="Sort TV Episodes.")

group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", help="More output", action="count")
group.add_argument("-q", "--quiet", help="Less output", action="store_true")

group = parser.add_mutually_exclusive_group()
group.add_argument("-c", "--copy", help="Copy files to the destination. Leaving original files in-tact.", action="store_true")
group.add_argument("-m", "--move", help="Move files to the destination.", action="store_true")
group.add_argument("-r", "--rsync", help="Rsync files to the destination.", action="store_true")

parser.add_argument("-V", "--verify", help="Verify files after move/copy. Implied by -[-r]sync", action="store_true")

parser.add_argument("source", help="Source directory to start.")
parser.add_argument("destination", help="Destination directory for sorted files")

args = parser.parse_args()


def getFileList(path, extfilter):
	for root, dirs, files in os.walk(path, followlinks=False):
		for filename in files:
			ext = os.path.splitext(filename)[1]
			ext = ext[1:]
			if ext in extfilter:
				yield root, filename

def main():
	EPISODE_REGEXP = r'/(?P<tvname>.+)\bs?(?P<season>[0-9]+)[ex](?P<episode>[0-9]+[A-Za-z]?)\b(?P<extra>.+)/i'
	VIDEO_FORMATS = {'mkv','mp4','avi'}

	s_path = os.path.abspath(args.source)
	d_path = os.path.abspath(args.destination)

	if args.verbose:
		print "Processing..."
		print "Source {}".format(args.source)
		print "Destination {}".format(args.destination)

	for root, filename in getFileList(s_path, VIDEO_FORMATS):
		print join(root, filename)



if __name__ == "__main__": main()