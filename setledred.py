import wpilib
import commands2
from ledsubsystem import LEDSubsystem

class SetLEDRed(commands2.CommandBase):
   def __init__(self, led: LEDSubsystem) -> None:      
       super().__init__()

       self.led = led
       self.addRequirements(led)

   def initialize(self) -> None:
       pass       #  This function is not being used.

   def execute(self) -> None:
       self.led.setColorRed()

   def end(self, interrupted: bool) -> None:
       pass       #  This function is not being used.

   def isFinished(self) -> bool:
       return True
