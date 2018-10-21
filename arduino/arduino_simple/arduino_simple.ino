
void setup()
{
  Serial.begin( 115200 );
}

void loop()
{
  Serial.print( F( "MILLIS: " ) );
  Serial.println( millis() );
  _delay_ms( 1000 );
}
