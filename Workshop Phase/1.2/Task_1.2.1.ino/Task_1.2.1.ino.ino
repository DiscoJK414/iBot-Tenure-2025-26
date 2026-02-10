const int buzz=8;
void setup()
{
  pinMode(buzz, OUTPUT);
}

void loop()
{
  tone(buzz, 1000);
  delay(1000);
}