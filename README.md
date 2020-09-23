# Lab 3 and 4 (AWSlog.py)
 For this project, you will be working individually or in pairs (at your discretion). If you work in a pair group, you will each receive the same grade for the project.

The goal of this project is to familiarize yourself with Python syntax, and some basic tasks that are common in systems programming and administration. The program will be invoked from the command line on a fresh Linux machine, so if you introduce any library dependencies beyond the Python Standard Library (not recommended), you must provide very clear instructions to recreate your environment. I would suggest using Vagrant (Links to an external site.) or a GCP (Links to an external site.) VM to develop in Linux if you are on a Windows machine. Another option is to install the Windows Subsystem for Linux (Links to an external site.) and setup a Python environment (Links to an external site.). It is your responsibility to ensure the program runs as expected in the operational environment described.

Here’s the scenario: you work for a medium sized company that sells widgets directly to consumers through brick-and-mortar retail stores. The marketing department wants to try a new promotional campaign to ramp up direct internet sales, but needs better data about current traffic to your website. Your boss has asked you to take the HTTP server logs from the webserver and provide some analytics to Marketing.

STEPS

Your program will be parsing and analyzing log files from an Apache web server. The first thing your program must do is retrieve the log file across the network. It is available here: https://s3.amazonaws.com/tcmg476/http_access_log (Links to an external site.)

Once you download the file, you need to save a local copy to disk (a cached copy) so the next time you run your script, you don't have to wait for the download.

Marketing wants to know two things: 
How many total requests have been made in the last year?
How many total requests were made in the time period represented by the log?

You will need to output this data to the screen. The format you choose to do this is up to you, but your decisions and your implementation should be logical and consistent.

Your program should be created and developed using GitHub (I will be examining the commit logs to see your work). When the project is due, submit your repository URL so I can clone the repo and test your program.

If you are working in a pair group, each student should submit the same repo URL.
