const int trig=9;
const int echo=10;
void setup() {
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
  }

void loop() {
  digitalWrite(trig, LOW);
  delayMicroseconds(2);

  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  long duration = pulseIn(echo, HIGH, 30000);
  float distance=(duration*0.0342)/2;

  Serial.print("\nDistance :");
  Serial.print(distance);
  
  delay(500);
}
