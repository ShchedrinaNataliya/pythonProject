from time import sleep
class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
            print("Trafficlight is red")
            sleep(7)
            print("Trafficlight is yellow")
            sleep(2)
            print("Trafficlight is green")
            sleep(7)
            print("Trafficlight is yellow")
            sleep(2)
trafficlight = TrafficLight()
trafficlight.running()