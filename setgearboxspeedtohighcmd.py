import wpilib
from commands2 import Command
from pneumaticsubsystem import PneumaticSubsystem

class SetGearboxSpeedToHighCMD(Command):
   def __init__(self, pneumaticsubsystem: PneumaticSubsystem, highspeed: bool):
       self.pneumaticsubsystem = pneumaticsubsystem
       self.highspeed = highspeed

       self.addRequirements(self.pneumaticsubsystem)

   def initialize(self):
       super().initialize()

   def execute(self):

        if (self.highspeed):
            self.pneumaticsubsystem.GearboxHighSpeed()
            print ("Gearbox High Speed" )
        else:
            self.pneumaticsubsystem.GearboxLowSpeed()
            print ("Gearbox Low Speed" )



   def isFinished(self) -> bool:
       return True

   def end(self, interrupted: bool):
       pass