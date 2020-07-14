# DansettePi

Python scripts used in the Dansette Pi Internet Radio project

Information
===========

More details of the project can be found at:

Instructables: https://www.instructables.com/id/1964-Dansette-Pi-Internet-Radio

Hackster:

YouTube: https://youtu.be/98O8wwiskhk

Prerequisites
=============

This project uses a Pimoroni Pirate Audio board, which needs to have its software installed first. 

More info on this at: https://github.com/pimoroni/pirate-audio

The main script is dansette.py, it uses playlist files in the "stations" folder to play internet radio using VLC player. 

It also displays the corresponding station icon from the "icons" folder.

To control the volume from Python we need to create an audio mixer, in this case called "Master".

We create this by saving the "asoundrc" file into the /home/pi/ folder, changing its name to ".asoundrc"

VLC needs to be set to only allow one instance.
