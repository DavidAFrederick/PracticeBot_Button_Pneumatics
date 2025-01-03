import wpilib
from commands2 import Command
from pneumaticsubsystem import PneumaticSubsystem


class SetIntakeClosedCmd(Command):
   def __init__(self, pneumaticsubsystem: PneumaticSubsystem):
       self.pneumaticsubsystem = pneumaticsubsystem

       self.addRequirements(self.pneumaticsubsystem)

   def initialize(self):
       super().initialize()

   def execute(self):
       self.pneumaticsubsystem.CloseIntake()
       print ("Intake - Closed")


   def isFinished(self) -> bool:
       return True

   def end(self, interrupted: bool):
       pass