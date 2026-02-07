int ledpin=3;
void setup() {
  pinMode(ledpin, OUTPUT);
}

void loop() {
  for(int b=0;b<=255;b++)
  {
    analogWrite(ledpin, b);
    delay(12);
  }
  for(int b=255;b>=0;b++)
  {
    analogWrite(ledpin,b);
    delay(12);
  }
}
