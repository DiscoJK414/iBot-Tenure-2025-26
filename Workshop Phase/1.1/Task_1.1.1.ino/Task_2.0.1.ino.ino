const int irPin = A0;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int irValue = analogRead(irPin);
  Serial.println(irValue);
  delay(200);
}
