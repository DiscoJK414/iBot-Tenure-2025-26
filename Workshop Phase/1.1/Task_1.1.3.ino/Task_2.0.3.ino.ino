const int pirPin = 2;

void setup() {
  pinMode(pirPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int Motion = digitalRead(pirPin);
  Serial.println(Motion);
  delay(200);
}
