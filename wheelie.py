from gpiozero import Motor


devices = {
        'front': (2, 3),
        'back': (17, 27),
        'turn': (9, 10), }


class Car:

    def __init__(self, devices=devices):
        self._speed = .5
        self._turn = .5
        if devices:
            self.devices = devices
            self.connect(devices)

    def connect(self, devices):
        self.front = Motor(*devices['front'])
        self.back = Motor(*devices['back'])
        self.steer = Motor(*devices['turn'])

    def forward(self):
        self.front.forward(self.speed)
        self.back.forward(self.speed)

    def stop(self):
        self.front.stop()
        self.back.stop()
        self.steer.stop()

    def turn_right(self):
        self.steer.forward(self.turn)

    def turn_left(self):
        self.steer.reverse(self.turn)

    def straight(self):
        self.steer.stop()

    def speed(self, value):
        if 0 <= value and value <= 1:
            self._speed = value

    def turn_speed(self, value):
        if 0 <= value and value <= 1:
            self._turn = value
