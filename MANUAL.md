# Museum in a Box User Manual

## Configuring Wifi

Although your Museum in a Box will work just fine, to receive automatic updates to the content; check for updates; or let us discover which objects are the most popular requires a connection to the Internet.

The Box connects to the Internet over wifi, so you will need to tell the Box the details for your wifi network:

  1. Boop the `Configure Wifi` tag onto the box
  1. That will create a `MuseumInABox` wifi network.  Connect to  that with your phone or laptop
  1. Usually that will automatically open this page which will let you enter the details for the network that the Box should use to connect to the Internet.  If this page fails to open, then visit [http://box.local/](http://box.local) (or if that fails to load, then [http://192.168.42.1](http://192.168.42.1)) in a web browser

  [!configure-wifi.jpg]

You will then be disconnected from the `MuseumInABox` network while the Box tries to connect using its new settings.  It will then tell you whether or not it succeeded.

### Advanced Wifi Options

We now have initial support for hidden and WPA Enterprise (also known as 802.1x) wifi networks.  To configure your Box to use one of these networks then follow these steps rather than those above.

  1. Boop the `Configure Wifi` tag onto the box
  1. That will create a `MuseumInABox` wifi network.  Connect to  that with your phone or laptop
  1. Ignore the standard configure wifi screen.  Instead, open a web browser and go to [http://box.local:1880/wifi](http://box.local:1880/wifi) (or if that doesn't load, then [http://192.168.42.1:1880/wifi](http://192.168.42.1:1880/wifi))
  1. That will present you with the following screen.  Enter the details for the particular type of network that the Box should use to connect to the Internet and then hit `Save`

  [!advanced-wifi-settings.jpg]

You will then be disconnected from the `MuseumInABox` network while the Box tries to connect using its new settings.  It will then tell you whether or not it succeeded.

## Checking for upgrades

Occasionally there will be software updates available for your Museum in a Box.  Generally, the team at Museum in a Box HQ will let you know if there's something available.

When you want to check for, or apply, an update the process is quite simple:

  1. Make sure your box is connected to the Internet.  Follow the steps to [Configure Wifi](#configuring-wifi)  if you haven't already done so
  1. Boop the `Check for Updates` tag onto the box
  1. The box will then tell you that it is checking for updates.  Once any updates have been applied, it will tell you that everything is up-to-date

