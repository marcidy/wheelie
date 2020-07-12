# Wheelie
The wheelie chassis has 5 connectors.
- Power from battery
- Power switch (short to turn on)
- Front Axel fwd/rev motor
- Front Axel turn motor
- Rear Axel fwd/rev motor

The power and switch connectors have red/black wires in the model used.  The motor connectors have white/green wires.

Each motor connector (white/green) requires a separate motor controller.  The power switch connector can be shorted.  The battery connector can be used to distribute power, or not.


## Motor Controllers

![Motor controllers]!(img/motor_controller_module.png)

Aideepen 5pcs 1.5A 2 Way DC Motor Driver Module Speed Dual H-Bridge Replace Stepper L298N 

[Amazon listing](https://www.amazon.com/gp/product/B075S368Y2/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)

- Power: 5V, GND
- 2 separate motor controllers on each module
- each controller has 2 inputs, and 2 outputs

## Wheelie
The wheelie has 3 motors total:
- a forward/reverse motor on each axel
- a "turn" motor on he front axel

This requires 3 seperate controllers, which is 2 modules

# Raspberry Pi
Well, we're using an rpi, but any GPIO from an MCU or whatever will work.   RPI is 3.3V and that works fine to drive the motor controller modules, as the work down to 1.8V inputs.

## GPIO
The GPIO used is determeined in wheelie.py.

```python
devices = {                                                                     
        'front': (2, 3),                                                        
        'back': (17, 27),                                                       
        'turn': (9, 10), }
```
This is done with GPIO numbering, also knows as BCM.  The GPIO numbering requirement is determined via the use of `gpiozero` python module.

While it's technically possible to swap the `front` and `back` definitions, the order of the pins must be consistent with the wiring.  If pins are swaps, the controller motors will not spin in the proper direction.

As long as the `devices` is updated to reflect the wiring, the api will function.

## Controller

`wheelie.py` is the controller for the motors.  They are logically grouped so that both 'fwd/rev' motors are synchronized.

## systemd
An example systemd service file is included which will launch a flask server to serve the API.

# API
The api is simplistic.  There's one endpoint '/drive' which takes two parameters `speed` and `turn`.  These inputs are both limited to the interval [-1, 1].

## speed
The `speed` parameter controls the velocity and fwd/rev of the wheelie.
- negative values are reverse
- positive values are forward
- `-1` is full reverse
- `0` is stop
- `1` is full forward

## turn
The `turn` parameter controls the front axle angle of deflection.
- negative values are left
- positive values are right

I haven't determined the angles, and they would be determined by the load on the chassis, so you'd have to experiement.

# Connection Diagram

![Connections]!(img/wiring.png)

