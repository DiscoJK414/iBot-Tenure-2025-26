const int sound = A0;
const int led = 8;
bool Active = false;
unsigned long t = 0;
const int thresh = 200;

void setup() {
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW);
  Serial.begin(9600);
}

void loop() {
  int v = analogRead(sound);
  Serial.println(v);

  if (v > thresh && !Active) {
    digitalWrite(led, HIGH);
    t = millis();
    Active = true;
  }

  if (Active && millis() - t > 2000) {
    digitalWrite(led, LOW);
    Active = false;
  }
}
