#!python3
## Motor script

def GPIO_setup():
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BOARD)
    print('GPIO Setup...')

def Motor_setup(pwr_pin):
    GPIO.setup(pwr_pin, GPIO.OUT)
    print('Motor Setup...')

def Motor_run(time):
    GPIO.ouput(pwr_pin, GPIO.HIGH)
    print('Motor running...')
    time.sleep(time)
    GPIO.ouput(pwr_pin, GPIO.LOW)
    print('Motor Finished')
