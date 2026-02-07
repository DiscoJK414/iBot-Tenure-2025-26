int ledpin = 9;
int buttonpin = 2;
bool ledState = LOW;
bool buttonState = HIGH; 

void setup() {
  pinMode(ledpin, OUTPUT);
  pinMode(buttonpin, INPUT_PULLUP);
  digitalWrite(ledpin, LOW);
}

void loop() {
  int state = digitalRead(buttonpin);

  if (buttonState == HIGH && state == LOW)
  {
    ledState = !ledState;
    digitalWrite(ledpin, ledState);
    delay(100);
  }
  buttonState = state;
}