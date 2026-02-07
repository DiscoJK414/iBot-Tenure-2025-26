const int ldrPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int lightValue = analogRead(ldrPin);
  Serial.println(lightValue);
  delay(200);
}
