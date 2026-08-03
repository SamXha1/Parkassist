// Define IR sensor pins
#define IR1 2
#define IR2 3
#define IR3 4
#define IR4 5
#define IR5 6

// Define LED pins
#define RED1 7
#define GREEN1 8
#define RED2 9
#define GREEN2 10
#define RED3 11
#define GREEN3 12
#define RED4 13
#define GREEN4 A0
#define RED5 A1
#define GREEN5 A2

void setup() {
    // Initialize IR sensors as input
    pinMode(IR1, INPUT);
    pinMode(IR2, INPUT);
    pinMode(IR3, INPUT);
    pinMode(IR4, INPUT);
    pinMode(IR5, INPUT);

    // Initialize LEDs as output
    pinMode(RED1, OUTPUT);
    pinMode(GREEN1, OUTPUT);
    pinMode(RED2, OUTPUT);
    pinMode(GREEN2, OUTPUT);
    pinMode(RED3, OUTPUT);
    pinMode(GREEN3, OUTPUT);
    pinMode(RED4, OUTPUT);
    pinMode(GREEN4, OUTPUT);
    pinMode(RED5, OUTPUT);
    pinMode(GREEN5, OUTPUT);

    // Start with all Green LEDs ON (No Object)
    turnOnGreenLEDs();
    Serial.begin(9600);
}

// Function to turn on all green LEDs and turn off all red LEDs initially
void turnOnGreenLEDs() {
    digitalWrite(RED1, LOW);  digitalWrite(GREEN1, HIGH);
    digitalWrite(RED2, LOW);  digitalWrite(GREEN2, HIGH);
    digitalWrite(RED3, LOW);  digitalWrite(GREEN3, HIGH);
    digitalWrite(RED4, LOW);  digitalWrite(GREEN4, HIGH);
    digitalWrite(RED5, LOW);  digitalWrite(GREEN5, HIGH);
}

void loop() {
    // Read sensor states
    int sensor1 = digitalRead(IR1);
    int sensor2 = digitalRead(IR2);
    int sensor3 = digitalRead(IR3);
    int sensor4 = digitalRead(IR4);
    int sensor5 = digitalRead(IR5);

    // Update LEDs based on sensor readings
    updateLED(sensor1, RED1, GREEN1, "Sensor 1");
    updateLED(sensor2, RED2, GREEN2, "Sensor 2");
    updateLED(sensor3, RED3, GREEN3, "Sensor 3");
    updateLED(sensor4, RED4, GREEN4, "Sensor 4");
    updateLED(sensor5, RED5, GREEN5, "Sensor 5");

    delay(100); // Small delay for stability
}

// Function to update LEDs based on sensor input
void updateLED(int sensorState, int redLED, int greenLED, String sensorName) {
    if (sensorState == LOW) { // Object detected
        digitalWrite(redLED, HIGH);
        digitalWrite(greenLED, LOW);
        Serial.println(sensorName + " - Object Detected: Red ON");
    } else { // No object detected
        digitalWrite(redLED, LOW);
        digitalWrite(greenLED, HIGH);
        Serial.println(sensorName + " - No Object: Green ON");
    }
}