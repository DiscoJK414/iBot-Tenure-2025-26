const int flamePin = 2;

void setup() {
  pinMode(flamePin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int state = digitalRead(flamePin);
  Serial.println(state);
  delay(200);
}
