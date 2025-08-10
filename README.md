# RPI_Webserver
Simple web server for raspberry pi. Setup instructions below.


How to set up in the rapsberry pi:
* Follow the directions on this website to set up the server: 
https://www.tomshardware.com/news/raspberry-pi-web-server,40174.html

* place index.html in the /var/www/html directory
* place gpio_control.py in the /usr/lib/cgi-bin directory
* Attach a LED to GPIO17 of the RPI. You can use this website for reference:  https://pinout.xyz/pinout/3v3_power
* To access the server: http://<hostname>. (Hostname can be found by doing Hostname -A in the rapsberry pi)
