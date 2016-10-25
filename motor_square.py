import brickpi
import time
import motor_util

interface=brickpi.Interface()
interface.startLogging('logfile.txt')
interface.initialize()

motors = [0,3]
speed = 5

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

motorParams = interface.MotorAngleControllerParameters()
motor_util.set_pid(motorParams)

interface.setMotorAngleControllerParameters(motors[0],motorParams)
interface.setMotorAngleControllerParameters(motors[1],motorParams)

numSquares = 0
while (True):
	motor_util.move40cm(interface, motors)
	motor_util.rotateRight90deg(interface, motors)
	motor_util.move40cm(interface, motors)
	motor_util.rotateRight90deg(interface, motors)
	motor_util.move40cm(interface, motors)
	motor_util.rotateRight90deg(interface, motors)
	motor_util.move40cm(interface, motors)
	motor_util.rotateRight90deg(interface, motors)	
	
	numSquares += 1
	a = raw_input("~~Another one~~? ("+ str(numSquares) +" squares)")
	
print "Destination reached!"


interface.stopLogging('logfile.txt')
interface.terminate()
