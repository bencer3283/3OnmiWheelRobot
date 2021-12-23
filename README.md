# 3OnmiWheelRobot

## Files
- The `bluetooth.sh` file is used to run the bluetooth serial port on raspberry pi.
- The `rPi.py` file is the main app to run the robot.
- `pid.py` is used to test the motor control codes.

## Procedures to run the robot
0. Pair your phone with rpi by bluetooth.
1. copy `bluetooth.sh` and `rPi.py` to the desired location on Rpi. (Currently in Desktop)
2. Open a terminal window, run `cd /Desktop`. (Or the desired location)
3. Then run `bash bluetooth.sh`, the terminal will then wait for your next command, now type in `power on`, after the execution type in `discoverable on`, than `quit`.
4. Now the rpi is waiting for a bluetooth connection. Keep this terminal window opened.
4. Click the connect button on the phone app utill the terminal indicate that the connection is established.
5. Open another terminal window, run `cd Desktop`, then `python3 rPi.py`, the program will be running without anything in the terminal. If it prints out error it's usually either the bluetooth connection isn't succesful or the Arduino is not connectted.
6. If things all go well, when you press a button on the app, the terminal shoud prints out the command it recieves.