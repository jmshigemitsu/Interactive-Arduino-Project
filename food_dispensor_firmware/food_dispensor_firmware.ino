// assign pins
int loader_motor_pin_1 = 2;
int loader_motor_pin_2 = 3;
int flywheel_motor_pin_1 = 4;
int flywheel_motor_pin_2 = 5;

// assign durations
int loader_motor_duration = 5000;
int flywheel_motor_duration = 3000;

// initialize command
String command;

void setup() {
  // establish serial communication and set pins
  Serial.begin(9600);
  pinMode(loader_motor_pin_1, OUTPUT);
  pinMode(loader_motor_pin_2, OUTPUT);
  pinMode(flywheel_motor_pin_1, OUTPUT);
  pinMode(flywheel_motor_pin_2, OUTPUT);

  // ensure all motors off at start
  stop_motors();
}

void loop() {
  while (!Serial.available()); 
  command = Serial.readString();
  command.trim(); 
  if (command == "DISPENSE"){
    // dispense food
    dispense_food();
  } 
}

void dispense_food(){
  // motor used to load food into hopper
  // rotation loader motor clockwise
  digitalWrite(loader_motor_pin_1, HIGH);
  digitalWrite(loader_motor_pin_2, LOW);
  delay(loader_motor_duration);
  
  // rotation loader counter clockwise
  digitalWrite(loader_motor_pin_1, LOW);
  digitalWrite(loader_motor_pin_2, HIGH);
  delay(loader_motor_duration);

  // stop loader motor
  stop_loader_motor();

  // spin flywheel motor to dispense 
  // food from hopper
  digitalWrite(flywheel_motor_pin_1, LOW);
  digitalWrite(flywheel_motor_pin_2, HIGH);

  // run flywheel dispensor motor
  delay(flywheel_motor_duration);

  // stop all motors
  stop_motors();
}

void stop_loader_motor(){
  // stop loader motors
  digitalWrite(loader_motor_pin_1, LOW);
  digitalWrite(loader_motor_pin_2, LOW);
}

void stop_motors(){
  // stop all motors
  stop_loader_motor();
  digitalWrite(flywheel_motor_pin_1, LOW);
  digitalWrite(flywheel_motor_pin_2, LOW);
}
