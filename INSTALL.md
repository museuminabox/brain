# Building a Brain

## Prerequisites

1. Raspberry Pi 2
1. SL030 RFID reader
1. SL030 to Raspberry Pi interconnect cable
1. Power supply
1. Speakers
1. Micro-SD card (8GB or higher recommended)
1. HDMI screen (for video version)
1. WiFi dongle (optional)

## Assembly

1. Attractively arrange componentry on a table
1. Place micro-SD card into Raspberry Pi
1. Put WiFi dongle into one of the USB ports on the Raspberry Pi
1. Connect the short (6-way) end of the Pi-to-SL030 interconnect cable to the SL030 RFID reader.  The red wire should connect to the pin marked Vcc and the black wire should connect to the pin marked GND.
1. Connect the long end of the Pi-to-SL030 interconnect cable to the headers on the Raspberry Pi.  The wires should be in the "bottom left" of the headers if the Raspberry Pi logo printed on the Pi is the correct way round.
1. (Optional) Connect the HDMI cable if this is a video brain.
1. Connect the power to the Pi.

## Installation

### Manual Install

1. Install latest Raspbian
1. Install Node RED (if it wasn't already on the Raspbian image)
1. Install rfid-sl030 and ndef node.js modules
1. Copy contents of [miab](miab) to /home/pi
1. Copy flows_brain.json to /root/.node-red/ (you will need to rename it to flows_<hostname>.json depending on the hostname of your Pi)
1. Install [simple_sl030_rfid_reader]() and build `get_first_ndef_text_record` for it
1. Copy `bootprogress` to `/etc/init.d` to indicate progress during boot-up
1. Set `bootprogress` to run - `sudo update-rc.d bootprogress defaults`

### Ansible Install

1. Install [Ansible](https://www.ansible.com/get-started) on your computer
1. Install the latest [Raspbian lite image](https://www.raspberrypi.org/downloads/raspbian/) onto a micro-SD card
1. Boot the Raspberry Pi with the micro-SD card, while plugged into a network via Ethernet
1. Find out the IP address of the Raspberry Pi
1. Copy your SSH credentials onto the Pi
  ```ssh-copy-id pi@<ip-address-of-the-pi>```
1. Edit the ```hosts``` file so ansible knows which computer to configure.  Change the IP address in it to match the one you just found out.
1. Check you can run commands on the Pi using Ansible
   ```ansible brain -i hosts -a "hostname" -u pi```
1. Update the brain
   ```ansible-playbook brain.yml -i hosts```

Or use the pre-rolled images.

## Connecting to WiFi

To add new WiFi network credentials to the brain you will need a working network connection to the brain already.  So either add the settings before you move it from a known WiFi setup, or connect it to the network via Ethernet first.

 1. Get a command line connection to the brain ssh pi@brain-1.local
    - turn on pi, plug ethernet
    - (optional, for direct to laptop) share wifi via ethernet, set IP Add. to 10.0.0.1, make sure wifi is connected!
    - in terminal, type ssh pi@brain-1.local (or pi@brain-2..., or pi@brain-3...)
    - enter password for brain
 1. Run the WiFi config console
     sudo wicd-curses
 1. Find the network that you want to configure on the list.  Press the -> key to move to the configuration screen.  Use the down cursor key to find the "Automatically connect to this network" setting, then press the space bar to enable it "[X]" rather than "[ ]".  If the network requires encryption then cursor down to the "Key:" field and fill in the password there.
 1. Hit "F10" to save the settings.
 1. Type "Q" to quit from the WiFi config app.
 1. Next time you boot up, it should choose the newly configured WiFi.  (You'll need to unplug the Ethernet if you've used that, otherwise it'll use that in preference)

## Writing new tags

### Writing the metadata to the tags
1. Get the system up and running
1. Using an NFC-enabled phone, write a URL to the tag you want to write. (It will be overwritten, and this step will be removed when we work out how to format blank tags)
1. Place the tag onto the reader
1. In a browser, go to http://brain-1.local:1880/tag (depending on which brain you're connecting to, it might be brain-2.local instead)
1. Fill in the details
  * URL is the link to the print on the website (this is where a Phone will visit when you tap the tag on it)
  * ID is the print's ID in the database (the number at the end of the URL)
  * The filenames are the names of the media files that you'll copy onto the Brain in a minute
1. Click write

### Copying content over to the Brain
1. Open the "transmit" app (on Mac)
1. Create a new favourite, with the server of brain-1.local (or brain-2.local), username pi, password raspberry
1. Connect to it, copy the audio and video files into the respective miab/audio and miab/video folders
1. Repeat the process for all the other brains

