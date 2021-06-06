#!/bin/sh

#./videotogif.sh input.mov output.gif 720 10
# will output 720p wide 10fps GIF from the movie you gave it

palette="/tmp/palette.png"

filters="fps=$4,scale=$3:-1:flags=lanczos"

ffmpeg -v warning -i "$1" -vf "$filters,palettegen" -y "$palette"
ffmpeg -v warning -i "$1" -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y "$2"