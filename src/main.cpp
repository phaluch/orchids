#include <Arduino.h>
#include <stdio.h>

// Define variables for file name and interval
unsigned long interval = 60000; // 60 seconds

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0; i < 20; i++) {
    int sensorValue = analogRead(i); // Read analog value from pin i
    
    // Print the value to the serial monitor
    Serial.print(i);
    Serial.print(":");
    Serial.println(sensorValue);
    
    delay(100); // Wait for a short time before reading the next pin
  }
}