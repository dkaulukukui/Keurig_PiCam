Project to capture caffiene addicts in the act.  

- Contact closures on two keurig coffee makers triggers the pi cam to take snapshots of the guilty parties.
- Python script handles the contact closure inputs, cam interface, and file management.
- bash shell script launches python script upon system startup
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

Known issues:
- memory overflow of snapshots are not manually removed periodically
