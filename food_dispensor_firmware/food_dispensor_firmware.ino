#include <Servo.h>

// assign pins
int flywheel_motor_pin_1 = 2;
int flywheel_motor_pin_2 = 3;
int servo_pin = 9;
int break_beam = 10;

// assign flywheel duration
int flywheel_motor_duration = 3000;

// initialize command
String command;

// initialize servo
Servo loading_servo;

void setup() {
  // establish serial communication and pins
  Serial.begin(9600);
  loading_servo.attach(servo_pin);
  pinMode(flywheel_motor_pin_1, OUTPUT);
  pinMode(flywheel_motor_pin_2, OUTPUT);
  pinMode(break_beam, INPUT_PULLUP);

  // ensure motor is off at start
  stop_flywheel_motor();
  // Starting servo position
  loading_servo.write(90);
}

void loop() {
  // wait for serial port to open
  while (!Serial.available()); 
  // read in command from port and trim it
  command = Serial.readString();
  command.trim();
  // if command is DISPENSE then run
  // dispense food method 
  if (command == "DISPENSE"){
    dispense_food();
  } 
}

void dispense_food(){
  // rotate servo to load food
  load_food();

  // fire food from hopper
  shoot_food();
  
  // stop flywheel motor
  stop_flywheel_motor();
}

void load_food(){
  treat_loaded = digitalRead(break_beam)
  while (treat_loaded == HIGH){
    // move servo clockwise
    loading_servo.write(0);
    delay(700);
    // Move servo counterclockwise
    loading_servo.write(180);
    delay(700);
    // check if beam is broken
    treat_loaded = digitalRead(break_beam)
  }
   // Move servo back to start
   loading_servo.write(90);
   delay(700);
}

void shoot_food(){
  // spin flywheel motor to dispense 
  // food from hopper
  digitalWrite(flywheel_motor_pin_1, LOW);
  digitalWrite(flywheel_motor_pin_2, HIGH);
  // run flywheel dispensor motor
  delay(flywheel_motor_duration);
}

void stop_flywheel_motor(){
  // stop flywheel motor
  digitalWrite(flywheel_motor_pin_1, LOW);
  digitalWrite(flywheel_motor_pin_2, LOW);
}
