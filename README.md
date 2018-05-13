Project to capture caffiene addicts in the act.  

- Contact closures on two keurig coffee makers triggers the pi cam to take snapshots of the guilty parties.
- Python script handles the contact closure inputs, cam interface, and file management.
- crontab runs a shell script that calls the main python script upon system startup
- Snapshots are stored into a local directory. 
- LAMP stack serves a PHP page which displays the latest snapshots on a webpage.

Major Custom Components:
- Pyhton script
- script launcher
- PHP webpage

Hardware: 

- Raspberry pi Zero W
- Raspbery pi camera
- 2 x contact closures
- 2 x resistors

software:
- Python
- LAMP
- crontab

Script Launcher Instructions:  Uses Crontab to call launcher.sh which calls python script
- At command type>> crontab -e 
   - Add the line below at the bottom of the file:
   - @reboot sh /home/pi/path_to_launcher_dir/launcher.sh >/home/pi/logs/cronlog 2>&1
   - ensure that the launcher is an executable (chmod 777 if necessary). 
   - Ensure that file path in launcher.sh to python script is correct

Known issues:
- memory overflow of snapshots are not manually removed periodically
